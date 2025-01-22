/*
 * utils.cpp
 * Copyright (C) 2012 Kovid Goyal <kovid at kovidgoyal.net>
 *
 * Distributed under terms of the GPL3 license.
 */

#include "global.h"
#include <sstream>
#include <stdexcept>
#include <string_view>

namespace pdf {

void podofo_set_exception(const PdfError &err) {
    const char *msg = err.what();
    ::std::stringstream stream;
    stream << msg << "\n";
    
    const auto& call_stack = err.GetCallstack();
    for (const auto& info : call_stack) {
        stream << "File: " << info.GetFilename()
              << " Line: " << info.GetLine() 
              << " Info: " << info.GetInformation() 
              << "\n";
    }
    PyErr_SetString(Error, stream.str().c_str());
}

PyObject* podofo_convert_pdfstring(const PdfString &s) {
    const std::string& str = s.GetString();
    return PyUnicode_FromStringAndSize(str.data(), str.length());
}

const PdfString podofo_convert_pystring(PyObject *val) {
    Py_ssize_t len;
    const char *data = PyUnicode_AsUTF8AndSize(val, &len);
    if (!data) {
        throw ::std::runtime_error(
            "Failed to convert python string to UTF-8, possibly not a string object"
        );
    }
    return PdfString(std::string(data, len));
}

const PdfObject* get_stream_object(const PdfObject* obj) {
    if (!obj || !obj->IsArray()) {
        return nullptr;
    }
    return obj;
}

bool
copy_stream_data(const PdfObject* stream_obj, std::vector<char>& buffer) {
    if (!stream_obj) return false;
    
    try {
        const auto* stream = stream_obj->GetStream();
        if (!stream) return false;

        const size_t size = stream->GetLength();
        if (size == 0) return false;
        
        buffer.resize(size);
        char* temp_buffer;
        pdf_long actual_size;
        stream->GetFilteredCopy(&temp_buffer, &actual_size);
        
        if (temp_buffer) {
            buffer.assign(temp_buffer, temp_buffer + actual_size);
            free(temp_buffer);
            return true;
        }
        return false;
    } catch (const PdfError&) {
        buffer.clear();
        return false;
    }
}

std::string 
get_string_value(const PdfString& str) {
    return str.GetString();
}

PdfString make_pdf_string(const std::string& str) {
    return PdfString(str);
}

PyObject* convert_array(const PdfArray& arr) {
    PyPtr list(PyList_New(arr.GetSize()));
    if (!list) return nullptr;
    
    for (size_t i = 0; i < arr.GetSize(); i++) {
        const auto& item = arr[i];
        PyObject* value = nullptr;
        
        if (item.IsNumber()) {
            value = PyLong_FromLong(item.GetNumber());
        } else if (item.IsReal()) {
            value = PyFloat_FromDouble(item.GetReal());
        } else {
            continue;
        }
        
        if (!value || PyList_SetItem(list.get(), i, value) < 0) {
            return nullptr;
        }
    }
    
    return list.release();
}

PyObject* ref_to_tuple(const PdfReference& ref) {
    return Py_BuildValue("(kk)", ref.ObjectNumber(), ref.GenerationNumber());
}

} // namespace pdf