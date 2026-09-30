import re, html, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

path = sys.argv[1]
if path.lower().endswith('.html'):
    data = open(path, encoding='utf-8', errors='replace').read()
    text = re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>', ' ', data)
    text = re.sub(r'<[^>]+>', ' ', text)
    text = html.unescape(text)
    text = re.sub(r'[ \t\r\f\v]+', ' ', text)
    text = re.sub(r'\n ', '\n', text)
    text = re.sub(r'\n\s*\n+', '\n\n', text)
    print(text.strip())
