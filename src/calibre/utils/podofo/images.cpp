namespace pdf {

class Image {
private:
    std::vector<char> buf;
    int64_t width, height; 
    PdfReference ref;
    PdfReference smask;
    bool is_valid;
    size_t content_hash, overall_hash;

    Image(const Image&) = delete;
    Image& operator=(const Image&) = delete;

public:
    Image(const PdfReference& reference, const PdfObject* obj,
          std::unordered_map<PdfReference, size_t, PdfReferenceHasher>& hash_cache)
        : width(0), height(0), ref(reference), is_valid(false) {
        
        try {
            if (const auto stream = obj->GetStream()) {
                const auto size = stream->GetLength();
                if (size > 0) {
                    buf.resize(size);
                    stream->CopyToSafe(buf.data(), size);
                    is_valid = true;
                }
            }

            const auto& dict = obj->GetDictionary();
            width = dict.GetKeyAs<int64_t>("Width", 0);
            height = dict.GetKeyAs<int64_t>("Height", 0);
            
            if (auto smask_obj = dict.FindKey("SMask")) {
                if (smask_obj->IsReference()) {
                    smask = smask_obj->GetReference();
                }
            }

            auto it = hash_cache.find(reference);
            if (it == hash_cache.end()) {
                content_hash = std::hash<std::string_view>{}(
                    std::string_view(buf.data(), buf.size())
                );
                hash_cache.emplace(reference, content_hash);
            } else {
                content_hash = it->second;
            }

            overall_hash = std::hash<std::string>{}(
                std::to_string(width) + " " + 
                std::to_string(height) + " " + 
                (smask.ObjectNumber() ? smask.ToString() : "") + " " +
                std::to_string(content_hash)
            );

        } catch (...) {
            is_valid = false;
            buf.clear();
        }
    }

    Image(Image&& other) noexcept = default;

    bool operator==(const Image& other) const noexcept {
        return is_valid && other.is_valid &&
               width == other.width &&
               height == other.height && 
               smask == other.smask &&
               buf == other.buf;
    }

    std::size_t hash() const noexcept { return overall_hash; }
    const PdfReference& reference() const noexcept { return ref; }
};

struct ImageHasher {
    std::size_t operator()(const Image& k) const noexcept { return k.hash(); }
};

using ImageMap = std::unordered_map<Image, std::vector<PdfReference>, ImageHasher>;

static unsigned long
run_one_dedup_pass(PDFDoc* self, std::unordered_map<PdfReference, size_t, PdfReferenceHasher>& hash_cache) {
    unsigned long count = 0;
    auto& objects = self->doc->GetObjects();
    ImageMap image_map;
    std::unordered_map<PdfReference, PdfReference, PdfReferenceHasher> ref_map;

    // Find all image objects
    for (auto* obj : objects) {
        if (!obj || !obj->IsDictionary()) continue;
        const auto& dict = obj->GetDictionary();
        if (dictionary_has_key_name(dict, "Type", "XObject") && 
            dictionary_has_key_name(dict, "Subtype", "Image")) {
            const auto ref = obj->GetReference();
            Image img(ref, obj, hash_cache);
            auto [it, inserted] = image_map.try_emplace(std::move(img), std::vector<PdfReference>());
            if (!inserted) it->second.push_back(ref);
        }
    }

    // Update references
    for (const auto& [img, refs] : image_map) {
        if (!refs.empty()) {
            const auto& canonical_ref = img.reference();
            for (const auto& ref : refs) {
                if (ref != canonical_ref) {
                    ref_map[ref] = canonical_ref;
                    objects.RemoveObject(ref);
                    count++;
                }
            }
        }
    }

    // Update resources
    if (count > 0) {
        for (auto* obj : objects) {
            if (!obj || !obj->IsDictionary()) continue;
            auto& dict = obj->GetDictionary();
            
            if (auto* resources = dict.FindKey("Resources")) {
                if (resources->IsDictionary()) {
                    auto& res_dict = resources->GetDictionary();
                    if (auto* xobject = res_dict.FindKey("XObject")) {
                        if (xobject->IsDictionary()) {
                            bool changed = false;
                            PdfDictionary new_xobj;
                            
                            for (auto& entry : xobject->GetDictionary()) {
                                const auto& value = entry.second;
                                if (value->IsReference()) {
                                    auto it = ref_map.find(value->GetReference());
                                    if (it != ref_map.end()) {
                                        new_xobj.AddKey(entry.first, PdfObject(it->second));
                                        changed = true;
                                        continue;
                                    }
                                }
                                new_xobj.AddKey(entry.first, *value);
                            }
                            
                            if (changed) res_dict.AddKey("XObject", std::move(new_xobj));
                        }
                    }
                }
            }
        }
    }
    
    return count;
}

} // namespace pdf

// Python wrapper
static PyObject* 
dedup_images(pdf::PDFDoc* self, PyObject* args) {
    unsigned long count = 0;
    std::unordered_map<PdfReference, size_t, pdf::PdfReferenceHasher> hash_cache;

    try {
        count += pdf::run_one_dedup_pass(self, hash_cache);
        count += pdf::run_one_dedup_pass(self, hash_cache); // Second pass for cascaded duplicates
        return Py_BuildValue("k", count);
    } catch (const PdfError& err) {
        pdf::podofo_set_exception(err);
        return NULL;
    } catch (const std::exception& err) {
        PyErr_Format(pdf::Error, "Error deduplicating images: %s", err.what());
        return NULL;
    }
}

PYWRAP(dedup_images) {
    return dedup_images(self, args);
}