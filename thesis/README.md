# Full master's thesis — submission version

This is the full master's thesis prepared for submission and approval.

It uses the original template's single-column format: 12-point body text, 1.5 line spacing, the university/faculty title page and preserved margins. It is independent of the ten-page [short draft](../draft/README.md) and reports the same experiments: the retrieval-policy experiment and the prompt comparison.

The thesis focuses on **how effectively FINKI Hub answers student questions and provides useful guidance**. Architecture and retrieval comparisons support that purpose. Administrative workload and staff-time savings are outside scope.

## Read and edit

- [Current PDF](build/main.pdf).
- [Standalone Overleaf source ZIP](overleaf-thesis.zip): import into a separate project, choose `main.tex`, and use XeLaTeX with BibTeX.
- [First-manuscript review and verification](../docs/maintenance/thesis-first-manuscript-2026-09-08/README.md): measured page counts, scientific review, preservation and delivery checks.

| Location | Contents |
|---|---|
| `main.tex`, `setup.tex` | Document entry point, metadata and layout |
| `sections/` | Title page, abstract, scope and data-use statement and terminology |
| `chapters/01_introduction.tex` | Problem, effectiveness questions and contribution |
| `chapters/02_background.tex` | RAG, heterogeneous retrieval, Macedonian and assessment literature |
| `chapters/03_data.tex` | Requirements, correspondence, production questions and source authority |
| `chapters/04_architecture.tex` | Component responsibilities, contracts and variation points |
| `chapters/05_implementation.tex` | Chatbot, document, GPU, MCP and Discord implementation |
| `chapters/06_methodology.tex` | Fixed policies, sampling, replay, judgments, paired analysis and the prompt comparison |
| `chapters/07_results.tex` | Completed outcomes, diagnostics, assessor sensitivity, prompt comparison and delivery observations |
| `chapters/08_discussion.tex`, `09_conclusion.tex` | Findings, limitations and proposed effectiveness extensions |
| `appendices/reproducibility.tex` | Evidence records, executed assessment fields and denominator interpretation |
| `figures/`, `tables/`, `references.bib` | Native architecture diagram, frozen result-table content and audited literature |

## Status and boundaries

The thesis is not an independent validation of the answers. The completed experiments, their unfavorable findings and AI-assessment limitations remain intact. Source inspection is distinguished from deployment verification; controlled retrieval/prompt replay is distinguished from the full live agent, tools and conversation lifecycle.

The mentor's examples guided organization and depth. Their prose, experiments, publication claims and acknowledgements were not copied. The old scaffold is archived in the dated first-manuscript review; the original template remains separately preserved. The short draft is unchanged by this expansion.

Future work, described in the discussion and conclusion, covers reference quality, full conversations and live-tool evaluation. No new paid inference was performed to write these chapters; the prompt-comparison results come from the retained `research/effectiveness_v2` records. Dataset packaging remains deferred.

## Local build and export

From the workspace root in PowerShell:

```powershell
./thesis/build.ps1 -TimeoutSeconds 120
& ./research/draft_evaluation/.venv/Scripts/python.exe -X utf8 thesis/inspect_pdf.py
& ./research/draft_evaluation/.venv/Scripts/python.exe -X utf8 thesis/package.py
```

The build uses the existing local compiler in `draft/tools/`; the exported manuscript compiles independently of those local directories. `inspect_pdf.py` needs the retained research Python environment with PyMuPDF and Pillow; it renders pages and records page bounds. It does not independently validate scientific claims. `package.py` checks source/PDF hashes before writing an exact 22-file manuscript allowlist.

The ZIP contains only active LaTeX sources, two original logo assets, the bibliography and this guide. It excludes private questions, research workbooks, credentials, downloaded theses, unused outline text, build outputs and local tools. Nothing has been uploaded, committed or pushed.
