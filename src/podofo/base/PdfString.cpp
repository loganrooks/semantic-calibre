#include "PdfString.h"

namespace PoDoFo {

// ...existing code...

PdfString::PdfString(const std::string& sString, const PdfEncoding* const pEncoding)
    : m_bHex(false),
      m_bUnicode(false) 
{
    if (!sString.empty()) {
        // Check for UTF-16BE BOM
        if (sString.length() >= 2 && 
            static_cast<unsigned char>(sString[0]) == 0xFE && 
            static_cast<unsigned char>(sString[1]) == 0xFF) {
            // Handle as UTF-16BE
            m_bUnicode = true;
            m_sString = sString;
        } else {
            // Use provided encoding or default to PdfDocEncoding
            const PdfEncoding* pEnc = pEncoding ? pEncoding : PdfDocEncoding::Instance();
            m_sString = pEnc->ConvertToUnicode(sString);
        }
    }
}

// ...existing code...

} // namespace PoDoFo
