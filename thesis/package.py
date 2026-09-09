"""Package only current manuscript inputs; no private research or unused tables."""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parent
FILES = ('main.tex', 'setup.tex', 'references.bib', 'sections/titlepage.tex', 'sections/abstract.tex', 'sections/status.tex', 'sections/abbreviations.tex', 'chapters/01_introduction.tex', 'chapters/02_background.tex', 'chapters/03_data.tex', 'chapters/04_architecture.tex', 'chapters/05_implementation.tex', 'chapters/06_methodology.tex', 'chapters/07_results.tex', 'chapters/08_discussion.tex', 'chapters/09_conclusion.tex', 'figures/architecture.tex', 'tables/controlled_results.tex', 'appendices/reproducibility.tex', 'assets/Logo-Ukim.png', 'assets/Logo-Finki.jpg', 'README.md')

def main():
    manifest = json.loads((ROOT / 'build/source-manifest.json').read_text(encoding='utf-8-sig'))
    for name, expected in manifest['source_sha256'].items():
        if hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != expected:
            raise SystemExit('Rebuild the PDF before packaging changed manuscript sources.')
    if set(manifest['source_sha256']) != set(FILES) - {'README.md'}:
        raise SystemExit('Build manifest does not cover the exact active manuscript inputs.')
    if hashlib.sha256((ROOT / 'build/main.pdf').read_bytes()).hexdigest() != manifest['pdf_sha256']:
        raise SystemExit('PDF differs from the build manifest.')
    with zipfile.ZipFile(ROOT / 'overleaf-thesis.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
        for name in FILES:
            archive.write(ROOT / name, name)
    print(json.dumps({'bundle': 'thesis/overleaf-thesis.zip', 'files': list(FILES)}))

if __name__ == '__main__':
    main()
