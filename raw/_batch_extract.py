import re, html, sys, os
import fitz  # pymupdf
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

RAW = os.path.dirname(os.path.abspath(__file__))

def extract_html(path):
    data = open(path, encoding='utf-8', errors='replace').read()
    text = re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>', ' ', data)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = html.unescape(text)
    text = re.sub(r'[ \t\r\f\v]+', ' ', text)
    text = re.sub(r'\n ', '\n', text)
    text = re.sub(r'\n\s*\n+', '\n\n', text)
    return text.strip()

def extract_pdf(path):
    doc = fitz.open(path)
    parts = []
    for page in doc:
        parts.append(page.get_text())
    doc.close()
    text = "\n".join(parts)
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n\s*\n+', '\n\n', text)
    return text.strip()

for year in range(2001, 2025):
    html_p = os.path.join(RAW, f"{year}.html")
    pdf_p = os.path.join(RAW, f"{year}.pdf")
    out_p = os.path.join(RAW, f"_{year}.txt")
    if os.path.exists(html_p):
        txt = extract_html(html_p)
    elif os.path.exists(pdf_p):
        txt = extract_pdf(pdf_p)
    else:
        print(f"MISSING {year}")
        continue
    open(out_p, "w", encoding="utf-8").write(txt)
    print(f"{year}: {len(txt):>7} chars -> _{year}.txt")
