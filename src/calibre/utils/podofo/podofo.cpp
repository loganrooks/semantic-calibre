/*
 * podofo.cpp
 * Copyright (C) 2019 Kovid Goyal <kovid at kovidgoyal.net>
 *
 * Distributed under terms of the GPL3 license.
 */

#include "global.h"
#include <sstream>

using namespace pdf;

namespace {

static void
impose_page(PdfMemDocument& doc, unsigned int dest_page_num, unsigned int src_page_num) {
    try {
        // Get pages using modern API
        size_t page_count = doc.GetPageCount();
        if (dest_page_num >= page_count || src_page_num >= page_count) {
            throw create_error(EPdfError::ValueOutOfRange, "Page number out of range");
        }

        // Get source and destination pages
        auto& src_page = doc.GetPage(src_page_num);
        auto& dest_page = doc.GetPage(dest_page_num);

        // Create and setup XObject form
        std::unique_ptr<PdfXObjectForm> xobj(new PdfXObjectForm(
            doc,
            src_page.GetMediaBox(),
            PdfName("HeaderFooter")
        ));
        xobj->SetMatrix(src_page.GetMatrix());
        
        // Copy content from source page
        if (auto contents = src_page.GetContents()) {
            xobj->GetContents()->SetValue(contents->GetString());
            xobj->GetResources().GetDictionary() = 
                src_page.GetResources()->GetDictionary();
        }

        // Add resource to destination page
        auto& resources = dest_page.GetOrCreateResources();
        const auto& xobj_ref = xobj->GetObject().GetIndirectReference();
        resources.AddResource(
            PdfName("XObject"),
            xobj->GetIdentifier(),
            xobj_ref
        );

        // Update contents stream with modern string handling
        std::stringstream stream;
        stream << "q\n1 0 0 1 0 0 cm\n/" 
               << xobj->GetIdentifier().GetString() 
               << " Do\nQ\n";

        // Get existing content and append new
        if (auto contents = dest_page.GetContents()) {
            std::string existing = contents->GetString().GetString();
            if (!existing.empty()) {
                stream << existing;
            }
        }

        // Update page contents
        dest_page.GetOrCreateContents()->SetValue(stream.str());

    } catch (const PdfError& err) {
        throw err;
    } catch (const std::exception& err) {
        throw create_error(EPdfError::InvalidHandle, err.what());
    }
}

static PyObject*
impose(PDFDoc* self, PyObject* args) {
    unsigned long dest_page_num, src_page_num, count;
    if (!PyArg_ParseTuple(args, "kkk", &dest_page_num, &src_page_num, &count)) {
        return nullptr;
    }

    if (!self->doc) {
        PyErr_SetString(PyExc_ValueError, "PDF document is null");
        return nullptr;
    }

    try {
        // Validate page numbers
        size_t page_count = self->doc->GetPageCount();
        
        if (dest_page_num == 0 || src_page_num == 0 ||
            dest_page_num > page_count || src_page_num > page_count) {
            throw create_error(EPdfError::ValueOutOfRange, "Invalid page numbers");
        }

        // Perform imposition
        for (unsigned long i = 0; i < count; i++) {
            impose_page(*self->doc, dest_page_num - 1 + i, src_page_num - 1 + i);
        }

        // Remove original pages with bounds checking
        while (count-- && src_page_num <= page_count) {
            self->doc->DeletePage(src_page_num - 1);
            page_count--;
        }

        Py_RETURN_NONE;

    } catch (const PdfError& err) {
        podofo_set_exception(err);
        return nullptr;
    } catch (const std::exception& err) {
        PyErr_SetString(PyExc_RuntimeError, err.what());
        return nullptr;
    }
}

} // anonymous namespace

PYWRAP(impose)