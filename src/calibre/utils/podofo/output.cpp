/*
 * output.cpp
 * Copyright (C) 2012 Kovid Goyal <kovid at kovidgoyal.net>
 *
 * Distributed under terms of the GPL3 license.
 */

#include "global.h"
#include <stdexcept>

namespace pdf {

class MyOutputDevice final : public PdfOutputDevice {
private:
    PyObject* stream;
    
public:
    explicit MyOutputDevice(PyObject* s) : stream(s) {
        if (!stream || !PyObject_HasAttrString(stream, "write")) {
            throw std::runtime_error("Invalid stream object");
        }
        Py_INCREF(stream);
    }
    
    ~MyOutputDevice() override {
        PyGILState_STATE gil = PyGILState_Ensure();
        Py_DECREF(stream);
        PyGILState_Release(gil);
    }

    // Prevent copying
    MyOutputDevice(const MyOutputDevice&) = delete;
    MyOutputDevice& operator=(const MyOutputDevice&) = delete;
    
    void Write(const char* buffer, size_t size) override {
        if (!buffer || !size) return;
        
        PyGILState_STATE gil = PyGILState_Ensure();
        
        try {
            pyunique_ptr result(PyObject_CallMethod(stream, "write", "y#", 
                buffer, static_cast<Py_ssize_t>(size)));
            if (!result) {
                throw PdfError(EPdfError::InvalidHandle, 
                    "Failed to write to Python stream");
            }
        } catch (...) {
            PyGILState_Release(gil);
            throw;
        }
        
        PyGILState_Release(gil);
    }
    
    void Flush() override {
        if (!PyObject_HasAttrString(stream, "flush")) return;
        
        PyGILState_STATE gil = PyGILState_Ensure();
        
        try {
            pyunique_ptr result(PyObject_CallMethod(stream, "flush", nullptr));
            if (!result) {
                throw PdfError(EPdfError::InvalidHandle, 
                    "Failed to flush Python stream");
            }
        } catch (...) {
            PyGILState_Release(gil);
            throw;
        }
        
        PyGILState_Release(gil);
    }
};

PyObject* 
write_doc(PdfMemDocument* doc, PyObject* stream) {
    if (!doc) {
        PyErr_SetString(PyExc_ValueError, "Invalid PDF document");
        return nullptr;
    }

    try {
        MyOutputDevice device(stream);
        doc->Write(&device);
        Py_RETURN_NONE;
    } catch(const PdfError& error) {
        podofo_set_exception(error);
        return nullptr;
    } catch(const std::exception& error) {
        PyErr_Format(PyExc_ValueError, "Error writing PDF: %s", error.what());
        return nullptr;
    } catch(...) {
        PyErr_SetString(PyExc_ValueError, "Unknown error writing PDF");
        return nullptr;
    }
}

} // namespace pdf