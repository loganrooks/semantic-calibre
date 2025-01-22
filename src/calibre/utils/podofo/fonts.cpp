/*
 * fonts.cpp
 * Copyright (C) 2019 Kovid Goyal <kovid at kovidgoyal.net>
 *
 * Distributed under terms of the GPL3 license.
 */

#include "global.h"
#include <memory>
#include <string>
#include <stack>

using namespace pdf;

// Helper functions for modern PoDoFo API
namespace pdf {
 
    // Update StreamData class
    class StreamData {
    private:
        std::vector<char> data;
        
    public:
        explicit StreamData(const PdfObject* obj) {
            if (!obj || !obj->GetStream()) return;
            const auto stream = obj->GetStream();
            const auto size = stream->GetLength();
            if (size > 0) {
                data.resize(size);
                stream->GetFilteredCopy(data.data(), size);
            }
        }
        
        const std::vector<char>& getData() const { return data; }
        bool empty() const { return data.empty(); }
        size_t size() const { return data.size(); }
    };

    // Output stream helper
    class PyBytesOutputStream {
    private:
        std::vector<char> buffer;
    public:
        void write(const char* data, size_t size) {
            buffer.insert(buffer.end(), data, data + size);
        }
        
        PyObject* get_or_none() const {
            if (buffer.empty()) Py_RETURN_NONE;
            return PyBytes_FromStringAndSize(buffer.data(), buffer.size());
        }
    };

    // Helper functions
    inline PdfObject* 
    get_font_file(const PdfObject* descriptor) {
        if (!descriptor || !descriptor->IsDictionary()) return nullptr;
        const auto& dict = descriptor->GetDictionary();
        for (const char* key : {"FontFile", "FontFile2", "FontFile3"}) {
            if (auto ff = dict.FindKey(key)) 
                return const_cast<PdfObject*>(ff);
        }
        return nullptr;
    }

static void remove_font(PdfMemDocument& doc, PdfObject* font) {
    if (!font) return;
    auto& objects = doc.GetObjects();
    const auto& dict = font->GetDictionary();
    
    if (auto descriptor = dict.FindKey("FontDescriptor")) {
        if (auto ff = get_font_file(descriptor)) {
            objects.RemoveObject(ff->GetReference());
        }
        objects.RemoveObject(descriptor->GetReference());
    }
    objects.RemoveObject(font->GetReference());
}

void used_fonts_in_canvas(const PdfCanvas& canvas, unordered_reference_set& ans) {
    if (auto resources = canvas.GetResources()) {
        const auto& dict = resources->GetDictionary();
        if (!dict.HasKey("Font")) return;
        
        const auto& fonts = dict.GetKey("Font")->GetDictionary();
        if (auto contents = canvas.GetContentsObject()) {
            PdfContentsTokenizer tokenizer(canvas.GetObject());
            const char* token = nullptr;
            PdfVariant var;
            bool in_text = false;
            
            while (tokenizer.ReadNext(token, var)) {
                if (token) {
                    if (strcmp(token, "BT") == 0) in_text = true;
                    else if (strcmp(token, "ET") == 0) in_text = false;
                    else if (in_text && strcmp(token, "Tf") == 0) {
                        if (auto font = fonts.FindKey(var.GetName())) {
                            ans.insert(font->GetReference());
                        }
                    }
                }
            }
        }
    }
}

static PyObject*
list_fonts(PDFDoc* self, PyObject* args) {
    int get_font_data = 0;
    if (!PyArg_ParseTuple(args, "|p", &get_font_data)) return NULL;

    try {
        pyunique_ptr ans(PyList_New(0));
        if (!ans) return NULL;

        for (auto& obj : self->doc->GetObjects()) {
            if (!obj->IsDictionary()) continue;
            const auto& dict = obj->GetDictionary();
            
            if (!dictionary_has_key_name(dict, "Type", "Font") || 
                !dict.HasKey("BaseFont")) continue;

            const auto& name = dict.GetKey("BaseFont")->GetString();
            const auto& subtype = dict.GetKey("Subtype")->GetString();
            const auto& ref = obj->GetReference();

            PyBytesOutputStream stream_data, to_unicode;
        pyunique_ptr descendant_font, stream_ref, encoding, w, w2;

        // Handle width arrays
        if (auto width_arr = dict.FindKey("W")) {
            w.reset(convert_w_array(width_arr->GetArray()));
            if (!w) return NULL;
        }
        if (auto width2_arr = dict.FindKey("W2")) {
            w2.reset(convert_w_array(width2_arr->GetArray()));
            if (!w2) return NULL;
        }

        // Handle encoding
        if (auto enc = dict.FindKey("Encoding")) {
            if (enc->IsName()) {
                encoding.reset(PyUnicode_FromString(enc->GetName().GetString().c_str()));
                if (!encoding) return NULL;
            }
        }

        // Handle CID to GID mapping
        if (auto cid_map = dict.FindKey("CIDToGIDMap")) {
            if (!cid_map->IsName() || cid_map->GetName().GetString() != "Identity") {
                if (auto stream = cid_map->GetStream()) {
                    stream->CopyToSafe(cid_gid_map);
                }
            }
        }

        // Handle font descriptor and font data
        if (const PdfObject* descriptor = dict.FindKey("FontDescriptor")) {
            if (const PdfObject* ff = get_font_file(descriptor)) {
                stream_ref.reset(ref_as_tuple(ff->GetIndirectReference()));
                if (!stream_ref) return NULL;
                if (get_font_data) {
                    if (auto stream = ff->GetStream()) {
                        stream->CopyToSafe(stream_data);
                    }
                }
            }
        } 
        // Handle descendant fonts and ToUnicode
        else if (auto df = dict.FindKey("DescendantFonts")) {
            const PdfArray& desc_fonts = df->GetArray();
            descendant_font.reset(ref_as_tuple(desc_fonts[0].GetReference()));
            if (!descendant_font) return NULL;

            if (get_font_data && dict.HasKey("ToUnicode")) {
                if (auto unicode = dict.FindKey("ToUnicode")) {
                    if (auto stream = unicode->GetStream()) {
                        stream->CopyToSafe(to_unicode);
                    }
                }
            }
        }

        // Build font info dictionary
        pyunique_ptr font_dict(Py_BuildValue(
            "{ss ss s(kk) sO sO sO sO sO sO sO sO}",
            "BaseFont", name.c_str(),
            "Subtype", subtype.c_str(),
            "Reference", ref.ObjectNumber(), ref.GenerationNumber(),
            "Data", stream_data.get_or_none(),
            "DescendantFont", descendant_font.get_or_none(),
            "StreamRef", stream_ref.get_or_none(),
            "Encoding", encoding.get_or_none(),
            "ToUnicode", to_unicode.get_or_none(),
            "W", w.get_or_none(),
            "W2", w2.get_or_none(),
            "CIDToGIDMap", cid_gid_map.get_or_none()
        ));
        if (!font_dict) return NULL;

        if (PyList_Append(ans.get(), font_dict.get()) != 0) return NULL;
    }

        return ans.release();
    } catch (const PdfError& err) {
        podofo_set_exception(err);
        return NULL;
    }
}

// Rest of the implementation...

typedef std::unordered_map<PdfReference, unsigned long, PdfReferenceHasher> charprocs_usage_map;

void process_type3_font(PdfObject* obj, RefSet& refs) {
    if (!obj || !obj->IsDictionary()) return;
    
    const auto& dict = obj->GetDictionary();
    if (auto charProcs = dict.FindKey("CharProcs")) {
        for (auto& entry : charProcs->GetDictionary()) {
            refs.insert(entry.second->GetReference());
        }
    }
}

static PyObject* remove_unused_fonts(PDFDoc* self, PyObject* args) {
        try {
            auto& doc = *self->doc;
            unsigned long count = 0;
            unordered_reference_set used_fonts;

            // Collect used fonts from pages
            auto& pages = doc.GetPages();
            for (unsigned i = 0; i < pages.GetCount(); i++) {
                used_fonts_in_canvas(pages.GetPageAt(i), used_fonts);
            }

            // Collect used fonts from XObjects
            auto& objects = doc.GetObjects();
            for (auto* obj : objects) {
                if (!obj->IsDictionary()) continue;
                
                const auto& dict = obj->GetDictionary();
                if (!dictionary_has_key_name(dict, PdfName::KeyType, "XObject") ||
                    !dictionary_has_key_name(dict, PdfName::KeySubtype, "Form")) {
                    continue;
                }

                if (auto form = PdfXObject::GetFromObject<PdfXObjectForm>(*obj)) {
                    used_fonts_in_canvas(*form, used_fonts);
                }
            }

            // Remove unused fonts
            unordered_reference_set all_fonts;
            CharProcRefMap charprocs_usage;

            // First pass: collect fonts and usage info
            for (auto* obj : objects) {
                if (!obj->IsDictionary()) continue;
                
                const auto& dict = obj->GetDictionary();
                if (!dictionary_has_key_name(dict, PdfName::KeyType, "Font")) continue;

                const auto& font_type = dict.GetKey(PdfName::KeySubtype)->GetName().GetString();
                const auto ref = obj->GetIndirectReference();

                if (font_type == "Type3") {
                    all_fonts.insert(ref);
                    process_type3_font(obj, charprocs_usage);
                } else if (font_type == "Type0") {
                    all_fonts.insert(ref);
                }
            }

            // Second pass: remove unused fonts
            for (const auto& ref : all_fonts) {
                if (used_fonts.find(ref) != used_fonts.end()) continue;

                auto* font = objects.GetObject(ref);
                if (!font) continue;

                count++;
                remove_font(doc, font);
            }

            cleanup_unused_charprocs(doc, charprocs_usage);

            return Py_BuildValue("k", count);

        } catch (const PdfError& err) {
            podofo_set_exception(err);
            return nullptr;
        } catch (const std::exception& err) {
            PyErr_SetString(Error, err.what());
            return nullptr;
        }
    }

PyObject*
replace_font_data(PDFDoc *self, PyObject *args) {
    const char *data; Py_ssize_t sz;
    unsigned long num, gen;
    if (!PyArg_ParseTuple(args, "y#kk", &data, &sz, &num, &gen)) return NULL;
    const PdfIndirectObjectList &objects = self->doc->GetObjects();
    PdfObject *font = objects.GetObject(PdfReference(num, static_cast<uint16_t>(gen)));
    if (!font) { PyErr_SetString(PyExc_KeyError, "No font with the specified reference found"); return NULL; }
    PdfDictionary *dict;
    if (!font->TryGetDictionary(dict)) { PyErr_SetString(PyExc_ValueError, "Font does not have a descriptor"); return NULL; }
    PdfObject *descriptor = dict->FindKey("FontDescriptor");
    if (!descriptor) { PyErr_SetString(PyExc_ValueError, "Font does not have a descriptor"); return NULL; }
    PdfObject *ff = get_font_file(descriptor);
    PdfObjectStream *stream = ff->GetStream();
    stream->SetData(bufferview(data, sz));
    Py_RETURN_NONE;
}

PyObject*
merge_fonts(PDFDoc *self, PyObject *args) {
    const char *data; Py_ssize_t sz;
	PyObject *references;
    if (!PyArg_ParseTuple(args, "y#O!", &data, &sz, &PyTuple_Type, &references)) return NULL;
    PdfIndirectObjectList &objects = self->doc->GetObjects();
	PdfObject *font_file = NULL;
    PdfDictionary *dict;
	for (Py_ssize_t i = 0; i < PyTuple_GET_SIZE(references); i++) {
		unsigned long num, gen;
		if (!PyArg_ParseTuple(PyTuple_GET_ITEM(references, i), "kk", &num, &gen)) return NULL;
		PdfObject *font = objects.GetObject(PdfReference(num, static_cast<uint16_t>(gen)));
		if (!font) { PyErr_SetString(PyExc_KeyError, "No font with the specified reference found"); return NULL; }

		PdfObject *dobj = NULL;
        if (font->TryGetDictionary(dict)) { dobj = dict->FindKey("FontDescriptor"); }
		if (!dobj) { PyErr_SetString(PyExc_ValueError, "Font does not have a descriptor"); return NULL; }
		if (!dobj->IsDictionary()) { PyErr_SetString(PyExc_ValueError, "Font does not have a dictionary descriptor"); return NULL; }
        PdfDictionary &descriptor = dobj->GetDictionary();
		const char *font_file_key = NULL;
		PdfObject *ff = NULL;
        if ((ff = descriptor.FindKey("FontFile"))) { font_file_key = "FontFile"; }
        else if ((ff = descriptor.FindKey("FontFile2"))) { font_file_key = "FontFile2"; }
        else if ((ff = descriptor.FindKey("FontFile3"))) { font_file_key = "FontFile3"; }
        else { PyErr_SetString(PyExc_ValueError, "Font descriptor does not have file data"); return NULL; }
		if (i == 0) {
			font_file = ff;
			PdfObjectStream *stream = ff->GetStream();
			stream->SetData(bufferview(data, sz));
		} else {
			objects.RemoveObject(object_as_reference(ff)).reset();
			descriptor.AddKey(font_file_key, object_as_reference(font_file));
		}
	}
	Py_RETURN_NONE;
}

// Update CharProc implementation
class CharProc {
private:
    std::vector<char> buf;
    PdfReference ref;
    
public:
    CharProc(const PdfReference& reference, const PdfObject* obj) : ref(reference) {
        if (!obj || !obj->GetStream()) return;
        char* buffer = nullptr;
        pdf_long size = 0;
        obj->GetStream()->GetFilteredCopy(&buffer, &size);
        if (buffer) {
            buf.assign(buffer, buffer + size);
            free(buffer);
        }
    }
        
        CharProc(CharProc&& other) noexcept = default;
        
        CharProc& operator=(CharProc&& other) noexcept = default;
        bool operator==(const CharProc& other) const noexcept {
            return buf == other.buf;
        }

        std::size_t hash() const noexcept {
    return std::hash<std::string_view>{}(std::string_view(buf.data(), buf.size()));
}

        const PdfReference& reference() const noexcept { return ref; }
        
        CharProc(const CharProc&) = delete;
        CharProc& operator=(const CharProc&) = delete;
    };

struct CharProcHasher {
    std::size_t operator()(const CharProc& k) const { return k.hash(); }
};

typedef std::unordered_map<CharProc, std::vector<PdfReference>, CharProcHasher> char_proc_reference_map;

// Update dedup_type3_fonts implementation
static PyObject*
dedup_type3_fonts(PDFDoc* self, PyObject* args) {
    try {
        auto& doc = *self->doc;
        unsigned long count = 0;
        unordered_reference_set all_char_procs;
        unordered_reference_set all_type3_fonts;
        char_proc_reference_map cp_map;

        // Process Type3 fonts
        for (auto& obj : doc.GetObjects()) {
            if (!obj->IsDictionary()) continue;
            const auto& dict = obj->GetDictionary();
            
            if (!dictionary_has_key_name(dict, PdfName::KeyType, "Font")) continue;
            
            const auto& font_type = dict.GetKey(PdfName::KeySubtype)->GetString();
            if (font_type != "Type3") continue;

            all_type3_fonts.insert(obj->GetReference());
            
            if (auto char_procs = dict.FindKey("CharProcs")) {
                for (auto& entry : char_procs->GetDictionary()) {
                    const auto& ref = entry.second->GetReference();
                    if (auto* cpobj = doc.GetObjects().GetObject(ref)) {
                        if (!cpobj->GetStream()) continue;
                        
                        CharProc cp(ref, cpobj);
                        auto [it, inserted] = cp_map.try_emplace(std::move(cp), std::vector<PdfReference>());
                        if (!inserted) {
                            it->second.push_back(ref);
                        }
                    }
                }
            }
        }

        // Deduplication logic
        std::unordered_map<PdfReference, PdfReference, PdfReferenceHasher> ref_map;
        for (const auto& [proc, refs] : cp_map) {
            if (refs.empty()) continue;
            
            const auto& canonical_ref = proc.reference();
            for (const auto& ref : refs) {
                if (ref != canonical_ref) {
                    ref_map[ref] = canonical_ref;
                    doc.GetObjects().RemoveObject(ref);
                    count++;
                }
            }
        }

        // Update references
        if (count > 0) {
            for (const auto& ref : all_type3_fonts) {
                if (auto* font = doc.GetObjects().GetObject(ref)) {
                    auto& dict = font->GetDictionary();
                    if (auto* char_procs = dict.FindKey("CharProcs")) {
                        PdfDictionary new_dict;
                        bool changed = false;

                        for (const auto& entry : char_procs->GetDictionary()) {
                            const auto& key = entry.first;
                            const auto& value = entry.second;
                            
                            if (auto it = ref_map.find(value->GetReference()); 
                                it != ref_map.end()) {
                                new_dict.AddKey(key, PdfObject(it->second));
                                changed = true;
                            } else {
                                new_dict.AddKey(key, *value);
                            }
                        }

                        if (changed) {
                            dict.AddKey("CharProcs", std::move(new_dict));
                        }
                    }
                }
            }
        }

        return PyLong_FromUnsignedLong(count);
    } catch (const PdfError& err) {
        podofo_set_exception(err);
        return nullptr;
    } catch (const std::exception& err) {
        PyErr_SetString(Error, err.what());
        return nullptr;
    }
}

}

PYWRAP(list_fonts)
PYWRAP(merge_fonts)
PYWRAP(remove_unused_fonts)
PYWRAP(dedup_type3_fonts)
PYWRAP(replace_font_data)
