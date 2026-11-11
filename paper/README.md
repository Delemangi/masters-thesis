# Conference paper

This folder holds a shorter conference paper derived from the master's thesis in [`../thesis/`](../thesis/README.md). The thesis is the primary document; this paper is planned for later submission and is not part of the thesis submission. Until then, treat it as a work in progress that may lag behind the thesis.

It is a standalone, English, two-column manuscript, currently ten pages including references. It matches the thesis (deployed agent, live-system evaluation, graph-based and agentic RAG related work), describes only the current state of the system and reports the same experiments, adding no separate evidence. Before submission it needs to be fitted to the chosen venue's template and page limit.

Earlier revisions of this manuscript were called "the draft" in older notes, commit messages and review records, and the folder was named `draft/` (and before that `draft-paper/`). Those records describe this paper. The local study folder `research/draft_evaluation/` keeps its historical name because frozen manifests record its paths.

## Read or use in Overleaf

- In the combined Overleaf project, compile the root `paper.tex` with XeLaTeX and BibTeX.
- Alternatively import `overleaf-paper.zip` into a separate project and select its `main.tex`.
- Standard packages are used; no shell escape, credentials, private datasets or inference runtime are required.

## Local build

From the workspace root in PowerShell:

```powershell
./paper/build.ps1 -TimeoutSeconds 120
& ./research/draft_evaluation/.venv/Scripts/python.exe ./paper/inspect_pdf.py
& ./research/draft_evaluation/.venv/Scripts/python.exe ./paper/package.py
```

The build uses the shared local compiler in [`../tools/`](../tools/README.md) and writes to `build/`. `package.py` verifies the build manifest and writes a six-file allowlisted ZIP: `main.tex`, `architecture.tex`, `related_work.tex`, `controlled_results.tex`, `references.bib` and this guide. The three older results-table files (`answer_results.tex`, `results.tex`, `retrieval_results.tex`) were moved to `archive/` and are not part of the manuscript or the ZIP; they are kept for historical verification only.

## Evidence

The experiments are documented in the local research workspace: `../research/luna_evaluation/` (retrieval-policy experiment), `../research/effectiveness_v2/` (prompt comparison) and `../research/draft_evaluation/` (component study). Dated review records in `../docs/maintenance/` describe earlier revisions of this paper.
