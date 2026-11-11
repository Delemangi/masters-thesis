# Master's thesis

This folder is the master's thesis prepared for submission and approval (November 2026). It is the primary document in this repository. The conference paper in [`../paper/`](../paper/README.md) is a separate, shorter derivative planned for later.

It uses the original template's single-column format: 12-point body text, 1.5 line spacing, the university/faculty title page and preserved margins. It reports two controlled experiments (the retrieval-policy experiment and the prompt comparison) and a live-system evaluation of the deployed agent on held-out emails. The manuscripts describe only the current state of the system, without dated change history.

The thesis focuses on **how effectively FINKI Hub answers student questions and provides useful guidance**. Architecture and retrieval comparisons support that purpose. Administrative workload and staff-time savings are outside scope.

## Read and edit

- [Current PDF](build/main.pdf) (local build output).
- In the combined Overleaf project, compile the root `main.tex` with XeLaTeX and BibTeX.
- [Standalone Overleaf source ZIP](overleaf-thesis.zip): import into a separate project, choose `main.tex`, and use XeLaTeX with BibTeX.

| Location | Contents |
|---|---|
| `main.tex`, `setup.tex` | Document entry point, metadata and layout |
| `sections/` | Title page, abstract and terminology |
| `chapters/01_introduction.tex` | Problem, effectiveness questions and contribution |
| `chapters/02_background.tex` | RAG, heterogeneous retrieval, Macedonian and assessment literature |
| `chapters/03_data.tex` | Data sources, correspondence, production questions and source authority |
| `chapters/04_architecture.tex` | Component responsibilities, contracts and variation points |
| `chapters/05_implementation.tex` | Chatbot, document, GPU, MCP and Discord implementation |
| `chapters/06_methodology.tex` | Fixed policies, sampling, replay, judgments, paired analysis and the prompt comparison |
| `chapters/07_results.tex` | Completed outcomes, diagnostics, judge sensitivity, prompt comparison and delivery observations |
| `chapters/07b_live_evaluation.tex` | Live-system evaluation of the deployed agent on tuned and held-out emails, A/B changes, error analysis and limits |
| `chapters/08_discussion.tex`, `09_conclusion.tex` | Findings, limitations and proposed effectiveness extensions |
| `figures/`, `tables/`, `references.bib` | Native architecture diagram, controlled result-table content and audited literature |

## Status and boundaries

The thesis is not an independent validation of the answers. The completed experiments, their unfavorable findings and AI-assessment limitations remain intact. Source inspection is distinguished from deployment verification; controlled retrieval/prompt replay is distinguished from the full live agent, tools and conversation lifecycle.

The mentor's examples guided organization and depth. Their prose, experiments, publication claims and acknowledgements were not copied.

The live-system evaluation (chapter "Live-system evaluation on held-out emails") is a separate, non-pre-registered engineering evaluation. Remaining work, described in the discussion and conclusion, covers human validation of labels, reference quality, a retrieval-disabled baseline in the live setting, a graph-based RAG comparison and conversation-level evaluation. The prompt-comparison results come from the retained `research/effectiveness_v2` records.

## Local build and export

From the workspace root in PowerShell:

```powershell
./thesis/build.ps1 -TimeoutSeconds 120
& ./research/draft_evaluation/.venv/Scripts/python.exe -X utf8 thesis/inspect_pdf.py
& ./research/draft_evaluation/.venv/Scripts/python.exe -X utf8 thesis/package.py
```

The build uses the shared local compiler in [`../tools/`](../tools/README.md); the exported manuscript compiles independently of it. `inspect_pdf.py` needs the retained research Python environment with PyMuPDF and Pillow; it renders pages and records page bounds. It does not validate scientific claims. `package.py` checks source/PDF hashes before writing an exact 21-file manuscript allowlist.

The ZIP contains only active LaTeX sources, two original logo assets, the bibliography and this guide. It excludes private questions, research workbooks, credentials, downloaded theses, build outputs and local tools.
