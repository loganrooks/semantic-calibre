#include "global.h"

namespace {

void impose_page(PdfMemDocument& doc, unsigned int dest_num, unsigned int src_num) {
    auto* src_page = pdf::PageManager::getPage(&doc, src_num);
    auto* dest_page = pdf::PageManager::getPage(&doc, dest_num);
    
    if (!src_page || !dest_page) {
        throw pdf::PdfException("Invalid page number");
    }

    // Create form XObject
    auto form = doc.CreateXObject(src_page->GetRect());
    form->CopyContentsFromPage(*src_page);
    
    // Update destination page
    auto contents = dest_page->GetContents();
    std::stringstream stream;
    
    // Preserve existing content
    if (contents && !contents->GetStream()->GetLength()) {
        pdf::StreamData data(contents);
        if (!data.empty()) {
            stream.write(data.data(), data.size());
        }
    }
    
    // Add new content
    stream << "q\n1 0 0 1 0 0 cm\n/" 
           << form->GetIdentifier().GetName()
           << " Do\nQ\n";
           
    contents->GetStream()->SetData(stream.str());
}

} // anonymous namespace

PYWRAP(impose) {
    unsigned long dest_page_num, src_page_num, count;
    if (!PyArg_ParseTuple(args, "kkk", &dest_page_num, &src_page_num, &count)) {
        return nullptr;
    }
    
    try {
        for (unsigned long i = 0; i < count; i++) {
            impose_page(*self->doc, dest_page_num + i - 1, src_page_num + i - 1);
        }
        
        // Remove original pages
        while (count--) {
            pdf::PageManager::deletePage(self->doc, src_page_num - 1);
        }
        
        Py_RETURN_NONE;
    } catch (const pdf::PdfException& e) {
        PyErr_SetString(PyExc_RuntimeError, e.what());
        return nullptr;
    }
}