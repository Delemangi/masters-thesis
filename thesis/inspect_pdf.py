"""Render the thesis and record page bounds; no private research inputs required."""
import hashlib
import json
from pathlib import Path

import pymupdf
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent
build = ROOT / 'build'
pdf = pymupdf.open(build / 'main.pdf')
details = []
for index, page in enumerate(pdf):
    outside = [list(b[:4]) for b in page.get_text('blocks')
               if b[0] < 0 or b[1] < 0 or b[2] > page.rect.width + 1 or b[3] > page.rect.height + 1]
    details.append({'page': index + 1, 'words': len(page.get_text('words')), 'outside_page_blocks': outside})
    page.get_pixmap(matrix=pymupdf.Matrix(0.9, 0.9)).save(build / f'page-{index+1:03}.png')
for start in range(0, len(pdf), 6):
    sheet = Image.new('RGB', (1080, 1554), '#d6d6d6')
    draw = ImageDraw.Draw(sheet)
    for offset in range(min(6, len(pdf)-start)):
        im = Image.open(build / f'page-{start+offset+1:03}.png').convert('RGB')
        im.thumbnail((520, 735))
        x = (offset % 2) * 540 + 10
        y = (offset // 2) * 518 + 24
        im.thumbnail((510, 480))
        sheet.paste(im, (x + (510-im.width)//2, y))
        draw.text((x, y-18), f'PDF page {start+offset+1}', fill='black')
    sheet.save(build / f'contact-{start//6+1:02}.png')
toc = pdf.get_toc()
intro = next(row[2] for row in toc if row[1] == 'Introduction')
references = next(row[2] for row in toc if row[1] == 'References')
report = {
    'pages': len(pdf), 'front_matter_pages': intro-1,
    'main_chapter_pages': references-intro,
    'reference_pages': len(pdf)-references+1,
    'pdf_sha256': hashlib.sha256((build / 'main.pdf').read_bytes()).hexdigest(),
    'pages_detail': details, 'table_of_contents': toc,
}
(build / 'pdf-inspection.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
(build / 'extracted.txt').write_text('\n\f\n'.join(page.get_text() for page in pdf), encoding='utf-8')
print(json.dumps({key: value for key,value in report.items() if key not in {'pages_detail','table_of_contents'}}, indent=2))
if len(pdf) < 50 or any(p['outside_page_blocks'] for p in details):
    raise SystemExit('Inspect thesis page-count or page-bound failures.')
