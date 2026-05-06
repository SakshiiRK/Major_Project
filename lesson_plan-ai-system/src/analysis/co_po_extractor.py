import re

def extract_co_po(text):
    """
    Extracts CO and PO from lesson text.

    Returns:
        dict
    """

    text_lower = text.lower()

    co = []
    po = []

    # Simple patterns (works for most academic formats)
    co_matches = re.findall(r"co\s*\d*[:\-]?\s*(.+)", text_lower)
    po_matches = re.findall(r"po\s*\d*[:\-]?\s*(.+)", text_lower)

    for c in co_matches:
        co.append(c.strip())

    for p in po_matches:
        po.append(p.strip())

    return {
        "co": co if co else ["Not explicitly mentioned"],
        "po": po if po else ["Not explicitly mentioned"]
    }