/*
 * outlines.cpp
 * Copyright (C) 2019 Kovid Goyal <kovid at kovidgoyal.net>
 *
 * Distributed under terms of the GPL3 license.
 */

#include "global.h"
using namespace pdf;

// Forward declarations
static PyObject* create_outline_node();

PyObject* 
create_outline(pdf::PDFDoc* self, PyObject* args) {
    const char *title;
    unsigned int pagenum;
    double left = 0, top = 0, zoom = 0;

    if (!PyArg_ParseTuple(args, "sI|ddd", &title, &pagenum, &left, &top, &zoom))
        return nullptr;

    try {
        auto& outlines = get_outlines(self->doc);
        const PdfPage* page = get_page_at(self->doc, pagenum - 1);
        if (!page) {
            PyErr_Format(Error, "Invalid page number: %u", pagenum);
            return nullptr;
        }
        
        // Create destination using modern API
        auto dest = create_destination(page, left, top, zoom);
        outlines.CreateChild(PdfString(title), *dest);
        Py_RETURN_NONE;
    } catch(const PdfError & err) {
        podofo_set_exception(err);
        return nullptr;
    } catch(const std::exception & err) {
        PyErr_Format(Error, "Error creating outline: %s", err.what());
        return nullptr;
    }
}

static void 
convert_outline(PDFDoc *self, PyObject *parent, PdfOutlineItem *item) {
    if (!item) return;

    pyunique_ptr node(create_outline_node());
    if (!node) return;

    try {
        const PdfString& title = item->GetTitle();
        pyunique_ptr title_obj(podofo_convert_pdfstring(title));
        if (!title_obj) return;
        
        if (PyDict_SetItemString(node.get(), "title", title_obj.get()) != 0)
            return;

        // Handle destination using modern API
        if (auto dest = item->GetDestination(self->doc)) {
            if (auto page = dest->GetPage(self->doc)) {
                const long pnum = page->GetPageNumber() + 1;
                pyunique_ptr d(Py_BuildValue(
                    "{sl sd sd sd}", 
                    "page", pnum,
                    "top", dest->GetTop(),
                    "left", dest->GetLeft(),
                    "zoom", dest->GetZoom()
                ));
                if (!d) return;
                if (PyDict_SetItemString(node.get(), "dest", d.get()) != 0)
                    return;
            }
        }

        PyObject *children = PyDict_GetItemString(parent, "children"); 
        if (!children || PyList_Append(children, node.get()) != 0) 
            return;

        // Handle outline hierarchy using modern API
        if (auto first = item->First())
            convert_outline(self, node.get(), first);
        if (PyErr_Occurred()) return;

        if (auto next = item->Next())
            convert_outline(self, parent, next);

    } catch (const PdfError&) {
        PyErr_WarnEx(PyExc_RuntimeWarning, "Error processing outline item", 1);
    }
}

static PyObject*
create_outline_node() {
    pyunique_ptr ans(PyDict_New());
    if (!ans) return nullptr;
    
    pyunique_ptr children(PyList_New(0));
    if (!children) return nullptr;
    
    if (PyDict_SetItemString(ans.get(), "children", children.get()) != 0)
        return nullptr;
        
    return ans.release();
}

static PyObject*
get_outline(PDFDoc *self, PyObject *args) {
    try {
        auto& outlines = get_outlines(self->doc);
        if (!outlines.First())
            Py_RETURN_NONE;

        PyObject *ans = create_outline_node();
        if (!ans) return nullptr;

        convert_outline(self, ans, outlines.First());
        if (PyErr_Occurred()) {
            Py_DECREF(ans);
            return nullptr;
        }

        return ans;
    } catch(const PdfError & err) {
        podofo_set_exception(err);
        return nullptr;
    } catch(const std::exception & err) {
        PyErr_Format(Error, "Error getting outline: %s", err.what());
        return nullptr;
    }
}

PYWRAP(create_outline)
PYWRAP(get_outline)