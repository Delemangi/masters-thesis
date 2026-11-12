"""Package only current manuscript inputs; no private research or unused tables."""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parent
FILES = ('main.tex', 'setup.tex', 'references.bib', 'sections/titlepage.tex', 'sections/abstract.tex','sections/abbreviations.tex', 'chapters/01_introduction.tex', 'chapters/02_background.tex', 'chapters/03_data.tex', 'chapters/04_architecture.tex', 'chapters/05_implementation.tex', 'chapters/06_controlled_experiment.tex', 'chapters/07b_live_evaluation.tex','chapters/08_discussion.tex', 'chapters/09_conclusion.tex', 'figures/architecture.tex', 'figures/live_holdout.tex', 'figures/roadmap.tex', 'figures/rag_variants.tex', 'figures/rag_lewis.tex', 'figures/prompt_assembly.tex', 'figures/state_stores.tex', 'figures/encoders.tex', 'figures/agent_flow.tex', 'figures/assessment_pipeline.tex', 'figures/judgment_example.tex', 'figures/policy_effects.tex', 'figures/outcome_bars.tex', 'figures/live_stages.tex', 'figures/live_ab.tex', 'figures/failure_taxonomy.tex', 'figures/failure_location.tex', 'figures/eval_dataflow.tex', 'figures/recall_heatmap.tex', 'figures/recall_context.tex', 'figures/error_attribution.tex', 'tables/controlled_results.tex','assets/Logo-Ukim.png', 'assets/Logo-Finki.jpg', 'README.md')

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
