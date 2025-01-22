/*
 * outline.cpp
 * Copyright (C) 2012 Kovid Goyal <kovid at kovidgoyal.net>
 *
 * Distributed under terms of the GPL3 license.
 */

#include "global.h"
#include <memory>

using namespace pdf;

namespace {

void dealloc(PDFOutlineItem* self) {
    self->item = nullptr;
    Py_TYPE(self)->tp_free((PyObject*)self);
}

PyObject* 
create(PDFOutlineItem *self, PyObject *args) {
    PyObject *as_child;
    PDFOutlineItem *ans = nullptr;
    unsigned int num;
    double left = 0, top = 0, zoom = 0;
    PyObject *title_buf;

    if (!PyArg_ParseTuple(args, "UIO|ddd", &title_buf, &num, &as_child, &left, &top, &zoom)) 
        return nullptr;

    try {
        ans = PyObject_New(PDFOutlineItem, &PDFOutlineItemType);
        if (!ans) return nullptr;
        ans->doc = self->doc;
        pyunique_ptr decref_ans_on_exit((PyObject*)ans);

        // Convert title using modern API
        PdfString title = pdf::podofo_convert_pystring(title_buf);

        // Get target page using modern API
        if (num == 0 || num > ans->doc->GetPageCount()) {
            throw ::std::runtime_error("Invalid page number: " + ::std::to_string(num));
        }
        const PdfPage& page = ans->doc->GetPage(num - 1);

        // Create destination with proper memory management
        auto dest = std::make_unique<PdfDestination>(
            const_cast<PdfPage*>(&page), 
            left, top, zoom
        );

        // Create outline item
        ans->item = PyObject_IsTrue(as_child) ? 
            self->item->CreateChild(title, *dest) :
            self->item->CreateNext(title, *dest);

        if (!ans->item) {
            throw ::std::runtime_error("Failed to create outline item");
        }

        return decref_ans_on_exit.release();

    } catch (const PdfError &err) {
        podofo_set_exception(err);
        return nullptr;
    } catch (const ::std::exception &err) {
        PyErr_Format(PyExc_ValueError, "Error creating outline: %s", err.what());
        return nullptr;
    }
}

PyObject*
erase(PDFOutlineItem *self, PyObject *args) {
    try {
        if (!self->item) {
            throw ::std::runtime_error("No valid outline item");
        }

        self->item->Erase();
        self->item = nullptr;

        Py_RETURN_NONE;

    } catch (const PdfError &err) {
        podofo_set_exception(err);
        return nullptr;
    } catch (const ::std::exception &err) {
        PyErr_Format(PyExc_ValueError, "Error erasing outline: %s", err.what());
        return nullptr;
    }
}

PyObject*
new_item(PyTypeObject *type, PyObject *args, PyObject *kwds) {
    PDFOutlineItem *self = (PDFOutlineItem*)type->tp_alloc(type, 0);
    if (self) {
        self->item = nullptr;
        self->doc = nullptr;
    }
    return (PyObject*)self;
}

static PyMethodDef methods[] = {
    {"create", (PyCFunction)create, METH_VARARGS,
     "Create a new outline item. Return a new outline item object."},
    {"erase", (PyCFunction)erase, METH_NOARGS,
     "Erase this outline item."},
    {nullptr, nullptr, 0, nullptr}
};

PyTypeObject PDFOutlineItemType = {
    PyVarObject_HEAD_INIT(nullptr, 0)
    .tp_name = "outline.PDFOutlineItem",
    .tp_basicsize = sizeof(PDFOutlineItem),
    .tp_dealloc = (destructor)dealloc,
    .tp_flags = Py_TPFLAGS_DEFAULT,
    .tp_doc = "PDF Outline items",
    .tp_methods = methods,
    .tp_new = new_item,
};

} // anonymous namespace