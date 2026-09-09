import json
import hashlib
from pathlib import Path
import pymupdf as fitz
root = Path(__file__).resolve().parent
pdf = fitz.open(root / 'build' / 'main.pdf')
report = {'pages': len(pdf), 'pdf_sha256': hashlib.sha256((root / 'build' / 'main.pdf').read_bytes()).hexdigest(), 'pages_detail': []}
for i,page in enumerate(pdf):
    text=page.get_text()
    rect=page.rect
    outside=[]
    for block in page.get_text('blocks'):
        if block[0]<0 or block[1]<0 or block[2]>rect.width+1 or block[3]>rect.height+1:
            outside.append(block[:4])
    report['pages_detail'].append({'page':i+1,'characters':len(text),'outside_page_blocks':outside})
    page.get_pixmap(matrix=fitz.Matrix(1.1,1.1)).save(root/'build'/f'page-{i+1:02}.png')
(root/'build'/'pdf-inspection.json').write_text(json.dumps(report,indent=2))
(root/'build'/'extracted.txt').write_text('\n\f\n'.join(p.get_text() for p in pdf),encoding='utf-8')
print(json.dumps(report,indent=2))
if len(pdf)>10:
    raise SystemExit('Paper exceeds the 10-page limit')

