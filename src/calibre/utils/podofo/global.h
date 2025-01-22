/*
 * global.h
 * Copyright (C) 2012 Kovid Goyal <kovid at kovidgoyal.net>
 *
 * Distributed under terms of the GPL3 license.
 */
#pragma once


#include <Python.h>

#include <podofo/podofo.h>
#include <unordered_set>
#include <unordered_map>
#include <string>
#include <memory>
#include <string_view>
#include <vector>
#include <stdexcept>

namespace pdf {

// Module exception types
extern PyObject *Error;

// Document types and utilities  
typedef struct {
    PyObject_HEAD
    PdfMemDocument *doc;
    PyObject *load_buffer_ref;
} PDFDoc;

typedef struct {
    PyObject_HEAD
    PdfMemDocument *doc;
    PdfOutlineItem *item;
} PDFOutlineItem;

extern PyTypeObject PDFDocType;
extern PyTypeObject PDFOutlineItemType;

// Modern PoDoFo helper functions
void podofo_set_exception(const PdfError &err);
PyObject* podofo_convert_pdfstring(const PdfString &s);

template<typename T>
bool dictionary_has_key_name(const PdfDictionary& dict, T key, const char* name) {
    const auto* val = dict.FindKey(key);
    return val && val->IsName() && val->GetName() == name;
}

inline const PdfPage* 
get_page(const PdfObject* doc_obj, const PdfReference& ref) {
    if (!doc_obj) return nullptr;
    auto* owner = doc_obj->GetOwner();
    if (!owner) return nullptr;
    auto* doc = owner->GetParentDocument();
    if (!doc) return nullptr;
    return doc->GetPage(ref.ObjectNumber() - 1);
}

// Modern page handling
class PageManager {
public:
    static PdfPage* getPage(PdfMemDocument* doc, size_t index);
    static void deletePage(PdfMemDocument* doc, size_t index);
    static PdfObject* createPageFromTemplate(PdfMemDocument* doc, const PdfPage* tmpl);
};

// inline const PdfPage* 
// get_page(const PdfDocument* doc, const PdfReference& ref) {
//     if (!doc) return nullptr;
//     return doc->GetPage(ref.ObjectNumber() - 1);
// }

inline const PdfPage* 
get_page_at(PdfMemDocument* doc, size_t index) {
    return doc->GetPage(index);
}

inline PdfReference 
object_as_reference(const PdfObject* obj) {
    return obj ? obj->GetReference() : PdfReference();
}

inline PdfReference
object_as_reference(const PdfObject& obj) {
    return obj.GetReference();
}

// Modern outline handling
inline PdfOutlines& 
get_outlines(PdfMemDocument* doc) {
    auto* outlines = doc->GetOutlines();
    if (!outlines) {
        // Modern API uses CreateOutlines() directly on catalog
        doc->GetCatalog()->CreateOutlines();
        outlines = doc->GetOutlines();
    }
    return *outlines;
}

// Error handling
class PdfException : public std::runtime_error {
    using std::runtime_error::runtime_error;
};


// Modern destination creation
inline std::unique_ptr<PdfDestination>
create_destination(const PdfPage* page, double left, double top, double zoom) {
    return std::make_unique<PdfDestination>(const_cast<PdfPage*>(page), left, top, zoom);
}

// Modern stream handling
class StreamData {
private:
    std::vector<char> buffer;
    
public:
    explicit StreamData(const PdfObject* obj);
    const char* data() const { return buffer.data(); }
    size_t size() const { return buffer.size(); }
    bool empty() const { return buffer.empty(); }
};

// Smart pointer utilities
struct PyObjectDeleter {
    void operator()(PyObject* p) const noexcept {
        Py_XDECREF(p);
    }
};

using PyPtr = std::unique_ptr<PyObject, PyObjectDeleter>;
using RefSet = std::unordered_set<PdfReference, PdfReferenceHasher>;


// Add new utilities:
namespace utils {
    PdfObject* getIndirectObject(const PdfDocument* doc, const PdfReference& ref);
    void copyStream(PdfStream* dest, const PdfStream* src);
    PyObject* objectToDict(const PdfObject* obj);
}

// Modern CharProc implementation
class CharProc {
private:
    std::vector<char> buf;
    PdfReference ref;

public:
    CharProc(const PdfReference& reference, const PdfObject* obj) : ref(reference) {
        if (!obj || !obj->GetStream()) return;
        StreamData data(obj);
        buf = data.getData();
    }

    CharProc(CharProc&& other) noexcept = default;
    CharProc& operator=(CharProc&& other) noexcept = default;
    CharProc(const CharProc&) = delete;
    CharProc& operator=(const CharProc&) = delete;

    bool operator==(const CharProc& other) const noexcept {
        return buf == other.buf;
    }

    std::size_t hash() const noexcept {
        return std::hash<std::string_view>()(
            std::string_view(buf.data(), buf.size())
        );
    }

    const PdfReference& reference() const noexcept { return ref; }
};

// Modern hash implementations
struct CharProcHasher {
    std::size_t operator()(const CharProc& k) const noexcept { 
        return k.hash(); 
    }
};

// Modern hash implementation for PdfReference
struct PdfReferenceHasher {
    std::size_t operator()(const PdfReference& ref) const noexcept {
        return std::hash<size_t>{}(ref.ObjectNumber());
    }
};

// Type aliases for modern API
using unordered_reference_set = std::unordered_set<PdfReference, PdfReferenceHasher>;

// Function declarations
void podofo_set_exception(const PdfError& err);
PyObject* podofo_convert_pdfstring(const PdfString& s);
PyObject* convert_w_array(const PdfArray& arr);
PyObject* ref_as_tuple(const PdfReference& ref);
void process_type3_font(PdfObject* obj, std::unordered_map<PdfReference, unsigned long, PdfReferenceHasher>& usage);
void cleanup_unused_charprocs(PdfMemDocument& doc, const std::unordered_map<PdfReference, unsigned long, PdfReferenceHasher>& usage);


// Function declarations
extern "C" {
    PyObject* py_list_fonts(PDFDoc*, PyObject*);
    PyObject* py_remove_unused_fonts(PDFDoc*, PyObject*);
    PyObject* py_merge_fonts(PDFDoc*, PyObject*);
    PyObject* py_replace_font_data(PDFDoc*, PyObject*);
    PyObject* py_dedup_type3_fonts(PDFDoc*, PyObject*);
    PyObject* py_impose(PDFDoc*, PyObject*);
    PyObject* py_dedup_images(PDFDoc*, PyObject*);
    PyObject* py_create_outline(PDFDoc*, PyObject*);
    PyObject* py_get_outline(PDFDoc*, PyObject*);
}

} // namespace pdf

// Error handling wrapper macro
#define PYWRAP(name) extern "C" PyObject* py_##name(PDFDoc *self, PyObject *args) { \
    try { \
        return name(self, args); \
    } catch (const PdfError &err) { \
        pdf::podofo_set_exception(err); \
        return NULL; \
    } catch (const ::std::exception &err) { \
        PyErr_Format(pdf::Error, "Error in " #name "(): %s", err.what()); \
        return NULL; \
    } catch (...) { \
        PyErr_SetString(pdf::Error, "An unknown error occurred in " #name); \
        return NULL; \
    } \
}