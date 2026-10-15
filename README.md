# Master's thesis workspace

This repository holds two documents built from the same research:

| Document | Folder | Overleaf entry | Status |
|---|---|---|---|
| **Master's thesis** | [`thesis/`](thesis/README.md) | root `main.tex` | Primary document; submission version, October 2026 |
| Conference paper | [`paper/`](paper/README.md) | root `paper.tex` | Shorter derivative for a later conference submission; work in progress |

The thesis is the priority. The paper reports the same experiments in a ten-page two-column format and adds no separate evidence.

**Naming history.** Older notes, review records and commit messages say "draft" or "short draft" for what is now the conference paper, which lived in `draft/` (earlier `draft-paper/`). "Full thesis" meant what is now simply the thesis. The local study folder `research/draft_evaluation/` keeps its historical name because frozen manifests record its paths.

## Compile in Overleaf

This checkout's `origin` is Overleaf. Select **XeLaTeX** with BibTeX. Use the root `main.tex` for the thesis or the root `paper.tex` for the paper. These entry files use Overleaf's documented `import` approach so each document's sources, figures and bibliography stay in its own folder; do not select the nested `main.tex` files in the combined project. Each folder can also be exported as a standalone source ZIP whose own `main.tex` is the entry point. See [Overleaf's main-document guidance](https://docs.overleaf.com/getting-started/recompiling-your-project/the-main-document#keeping-the-main-document-in-a-folder).

## Repository layout

Only the manuscript folders, `tools/` configuration and root guidance are tracked. Everything else is a local research workspace excluded by `.gitignore`, so links into it work only in the research checkout.

| Location | Purpose | Tracked |
|---|---|---|
| `thesis/` | Master's thesis sources, build and export scripts | Yes |
| `paper/` | Conference paper sources, build and export scripts | Yes |
| `tools/` | Shared local compiler (Tectonic) configuration; binary and cache stay local | Configuration only |
| `research/` | Experiments, protocols, results and private case evidence; start at the [research index](research/README.md) | No |
| `context/` | Registered research scope, architecture review and mentor theses | No |
| `docs/` | Dated maintenance and review records | No |
| `archive/` | Original Overleaf template, superseded manuscripts and old planning | No |
| `scripts/` | Maintenance scripts | No |
| `RESOURCES.md` | SSH/GPU access, datasets, budget and continuation notes | No |

Key evidence for the thesis:

| Location | Contents |
|---|---|
| `research/luna_evaluation/` | Main controlled retrieval-policy experiment with Luna generation; repeated and local AI assessment |
| `research/effectiveness_v2/` | Expanded document collection, prompt comparison and assessment audit ([results](research/effectiveness_v2/RESULTS.md)) |
| `research/draft_evaluation/` | Component study with a local generator, source-authority audit and AI validation |
| `research/production_evaluation/` | Historical production-question analysis supplying the production sample |
| `research/impact_analysis/` | Repository/deployment reconnaissance, email demand and PostHog observations |
| `research/email_evaluation/`, `research/legacy_dataset_review/` | Earlier candidate screening and the historical 194-case workbook review |
| `context/architecture-review/` | Source-level architecture across chatbot, documents, MCP and Discord |

Dated plans and reviews describe earlier stages and are not current instructions. Use `RESOURCES.md` for continuation decisions and the frozen manifests for completed experiments.

## Build and verify locally

From the workspace root in PowerShell:

```powershell
./thesis/build.ps1 -TimeoutSeconds 120
& ./research/draft_evaluation/.venv/Scripts/python.exe -X utf8 ./thesis/inspect_pdf.py
& ./research/draft_evaluation/.venv/Scripts/python.exe -X utf8 ./thesis/package.py
```

The paper builds the same way with `./paper/build.ps1`, `paper/inspect_pdf.py` and `paper/package.py`. Outputs are `<folder>/build/main.pdf` and `thesis/overleaf-thesis.zip` or `paper/overleaf-paper.zip`. Both builds use the shared compiler in [`tools/`](tools/README.md); the exported sources compile without it.

Do not rerun frozen inference or threshold selection to check repository organization, and do not move files inside frozen studies: their manifests record relative paths and hashes. Create a separate study folder for new experiments.

## What belongs in Git

**Tracked:** manuscript sources and build/package scripts in `thesis/` and `paper/`, compiler configuration in `tools/`, the root entry files and this guide. Generated PDFs, ZIPs and the three unused historical paper tables stay ignored.

**Local only:** research scripts, protocols, corpus snapshots, results and reviews (useful evidence, kept out of this Overleaf checkout); private questions, answers and workbooks; registration documents; model weights, environments, compiler binaries and caches.

Ignore rules do not remove tracked files or history, prevent `git add -f`, or govern manual uploads. Never upload the whole repository or a private workbook to Overleaf. `research/draft_evaluation/private/` and the other `private/` folders hold irreplaceable case-level evidence: do not delete them as caches, and back them up separately before any disk cleanup.
