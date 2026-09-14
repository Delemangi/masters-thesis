# Master's thesis workspace

## Compile this repository in Overleaf

Select **XeLaTeX** and use the top-level **`main.tex`** for the short draft. Select **`full-thesis.tex`** for the working thesis, which remains marked TODO. These entry files use Overleaf's documented `import` approach so sources, figures and bibliographies can stay in `draft/` and `thesis/`. Do not select the nested `main.tex` files for this combined repository. The separate source ZIPs still use their own `main.tex`.

See [Overleaf's main-document guidance](https://docs.overleaf.com/getting-started/recompiling-your-project/the-main-document#keeping-the-main-document-in-a-folder). Local research links below refer to ignored files available only in the research checkout.

**Start here:** [current draft PDF](draft/build/main.pdf), [Overleaf source ZIP](draft/overleaf-draft.zip), and [resources / next evaluation work](RESOURCES.md).

**9 September update:** the [new evaluation](research/effectiveness_v2/RESULTS.md) uses the expanded document collection, a 32-question diagnostic and a separate 40-email prompt comparison. It also repairs incomplete judge evidence. The draft includes both the initial and post-hoc results; no reliable prompt improvement is established. The local chatbot prompt is an evaluated candidate, not a deployed change. The preceding manuscript was pushed as `f755cdb`; this follow-up remains uncommitted and unpushed. Older review links below describe their dated versions.

The [current effectiveness revision](docs/maintenance/effectiveness-focus-2026-09-08/README.md) centers the draft on answering real student questions and providing useful guidance. The user has excluded staff-time savings and other administrative metrics from the research scope. Architecture and retrieval comparisons support the effectiveness analysis.

The active work is the short thesis draft (maximum ten pages) and its supporting evaluations. The full master's thesis now has a substantial first manuscript in `thesis/`: 78 PDF pages, including 62 pages of main chapters. Historical templates and planning are separated in `archive/`. Everything remains local unless explicitly authorized for publication.

This checkout's `origin` is **Overleaf**, not a separate research Git repository. The portable `.gitignore` excludes research, context (including mentor theses), archives, maintenance notes/scripts and `RESOURCES.md`, along with private directories, spreadsheets, credentials and generated artifacts. The local `.git/info/exclude` repeats the workspace exclusions as a backup; protection no longer depends on that local file. See the [9 September pre-push audit](docs/maintenance/overleaf-preflight-2026-09-09.md) for the current scope and limitations.

The [latest ignored-file recheck](docs/maintenance/publication-recheck.md) additionally inventories accessible files, checks first-party contents and Git history for credential patterns, compares private questions against staging candidates, and verifies both manuscript ZIPs. It records two inaccessible dependency directories and the limits of heuristic content checks.

For the two-document workflow, `draft/` contains the completed short paper; `thesis/` contains the first full-thesis manuscript in the original template's different format. Each has its own `main.tex`, build and explicit manuscript-only export. Use those exports for two Overleaf projects. The full-thesis PDF is clearly labeled as a first working manuscript, with completed evidence and remaining work distinguished. Do not sync this entire research workspace to either project. Historical records may still use the former `draft-paper/` path; current commands and entry points use `draft/`.

The [fresh literature audit](docs/maintenance/literature-audit-2026-09-07/README.md) checks all 22 bibliography entries against primary sources and maps the cited claims to relevant passages. Publication/author corrections and restored institutional citations make the current draft ten pages including references. The evaluation results are unchanged.

For what remains to improve and where each result is documented, use the [current readiness and evidence map](docs/maintenance/draft-readiness-review.md). It also distinguishes original assessment proposals from what was actually executed.

The latest [language review](docs/maintenance/language-review-2026-09-08/README.md) simplifies the draft's prose while preserving the study and citations. The revised draft remains ten pages including references.

The subsequent [content update](docs/maintenance/draft-content-update-2026-09-08/README.md) adds a worked example, data-use statement and an offline diagnostic of rejected reference quotations. The [evaluation extension](research/evaluation_extension/README.md) contains the completed reference audit and preparation for a future study; it does not replace the frozen answer-quality results.

## Where to look

The latest [argument review](docs/maintenance/draft-argument-review-2026-09-08/README.md) sharpens the architecture contribution, corrects the scope of the fallback interpretation and adds an observed paired illustration. The ten-page draft retains the frozen results.

| Location | Purpose | Status / entry point |
|---|---|---|
| `research/effectiveness_v2/` | Updated corpus, prompt experiment, assessment audit and deployment component checks | [Results](research/effectiveness_v2/RESULTS.md), [protocol](research/effectiveness_v2/protocol.md), [file index](research/effectiveness_v2/README.md) |
| `draft/` | Current short draft, LaTeX tables, bibliography and build scripts | [Build and manuscript guide](draft/README.md); working entry point is `draft/main.tex` |
| `thesis/` | Separate full-thesis manuscript, title page and nine substantive chapters | [Thesis guide](thesis/README.md); entry point `thesis/main.tex`; first working manuscript, not final submission |
| `RESOURCES.md` | SSH/GPU access, credential provenance, datasets, budget and next steps | [Current continuation guide](RESOURCES.md); dated observations must be rechecked |
| `context/` | Registered research scope and private registration documents | [Research context](context/research-context.md) |
| `context/architecture-review/` | Source-level architecture across chatbot, documents, MCP and Discord | [Evidence index and scope](context/architecture-review/README.md); includes current local repository/worktree revisions |
| `context/mentor-theses/` | Previous theses and lessons for evaluation/writing | [Reference collection](context/mentor-theses/README.md) and [analysis](context/mentor-theses/analysis.md); full PDFs/text stay local |
| `research/impact_analysis/` | Repository/deployment reconnaissance, email demand and PostHog observations | [Evidence overview](research/impact_analysis/README.md) |
| `research/email_evaluation/` | Earlier candidate screening and proposed pilot/reference queues | [Screening guide](research/email_evaluation/README.md); not the completed 320-case experiment |
| `research/draft_evaluation/` | Frozen local retrieval/generation experiment, source audit and AI validation | [Completed results](research/draft_evaluation/EVALUATION_SUMMARY.md) and [reproduction guide](research/draft_evaluation/README.md) |
| `research/luna_evaluation/` | Completed controlled production retrieval/prompt replay with Luna; repeated and local AI assessment | [Results and reproduction](research/luna_evaluation/README.md) |
| `research/production_evaluation/` | Historical production-question analysis supplying the new study frame | [Results and limitations](research/production_evaluation/README.md) |
| `research/legacy_dataset_review/` | Assessment of the historical 194-case extraction workbook | [Dataset review](research/legacy_dataset_review/README.md); same cases as `llms-evaluation`, not a new sample |
| `archive/` | Original Overleaf template, previous draft, imported planning and historical reviews | [Archive index](archive/README.md); not current results or instructions |
| `scripts/maintenance/` | Reviewed cleanup operation; dry run by default | [Deletion script](scripts/maintenance/cleanup-local-artifacts.ps1) |
| `docs/` | Repository maintenance notes | [Current reorganization/deletion status](docs/maintenance/reorganization-2026-09-07.md) |

For code navigation, start with the [research index](research/README.md). The frozen study keeps its internal paths; the new folder boundaries distinguish active work, historical material and disposable dependencies.

## Read the research in this order

1. [Registered scope](context/research-context.md) and [resource/status guide](RESOURCES.md).
2. [Operational and demand evidence](research/impact_analysis/README.md).
3. [Completed local study](research/draft_evaluation/EVALUATION_SUMMARY.md), [frozen protocol](research/draft_evaluation/protocol.md) and [verification](research/draft_evaluation/verification.md).
4. [Production-question extension](research/production_evaluation/README.md) and [historical dataset assessment](research/legacy_dataset_review/README.md).
5. [Controlled Luna evaluation](research/luna_evaluation/README.md) and [evidence review](research/luna_evaluation/evidence_review.md).
6. [Updated-source follow-up and assessment audit](research/effectiveness_v2/RESULTS.md).
7. [Current manuscript](draft/main.tex).

The earlier completed local study uses a quantized Qwen generator and simplified component path. The new study uses actual production retrieval and prompts with controlled Luna generation; it excludes the live agent transport and tools. Its AI judgments are not human validation or deployed Luna results. The source/label disagreements and unfavorable answer findings are retained. Neither email counts nor telemetry establish avoided contacts or staff savings.

Older plans, reviews and access reports are dated evidence of earlier stages. They are not all current instructions: notably, the earlier SSH failure was resolved, and old candidate/pilot queues are not the protected test set. Use `RESOURCES.md` for current continuation decisions and the frozen manifests for the completed experiment.

## What belongs in Git versus local storage

**Eligible for ordinary staging in this Overleaf checkout:** active sources and build/package tools in `draft/` and `thesis/`, plus root guidance. The three unused historical draft tables and generated PDFs/ZIPs remain ignored. Nothing has been newly committed or staged.

**Retain locally for research review:** original template copies, analysis/test scripts, dependencies, protocols, public corpus snapshots/vectors, source-authority records, aggregate results, execution manifests and scientific reviews. These are useful evidence, but the portable ignore rules keep their parent folders out of this Overleaf checkout. A separate research repository or reviewed export would need an explicit publication decision and its own exclusions.

**Keep local and ignored:** private questions/answers/workbooks; registration and imported conversation files; model weights and working environments; compiler binaries/cache; generated PDF/ZIP; previous delivery copies; live editor indexes. Ignored means excluded from ordinary Git staging, not anonymized or backed up.

Ignore rules do not remove tracked files or Git history, prevent `git add -f`, or govern manual uploads. The original template is already in the one existing commit; downloaded reference theses and private study data are not tracked. `.git/info/exclude` applies only to this checkout and must be reviewed if the workspace is recreated. The manuscript ZIP remains protected separately by an exact file allowlist.

`research/draft_evaluation/private/` contains irreplaceable case-level evidence. Do not delete it as a cache. Pinned model weights, installed runtimes and download-verification metadata support reproduction. The completed cleanup removed 24,318 disposable files (1.33 GB of logical file size), including redundant installation ZIPs, package-download caches, bytecode and temporary outputs. Normal tool use can regenerate caches; see the [cleanup record](docs/maintenance/reorganization-2026-09-07.md).

The manuscript upload ZIP is an explicit allowlist of six manuscript/guide files, including the native architecture diagram. Never upload the whole repository or a private workbook to Overleaf. Local research evidence needs a separately managed backup before any future disk cleanup.

## Build and verify

From this workspace in PowerShell:

```powershell
./draft/build.ps1 -TimeoutSeconds 120
& ./research/draft_evaluation/.venv/Scripts/python.exe ./draft/inspect_pdf.py
& ./research/draft_evaluation/.venv/Scripts/python.exe ./draft/package.py
& ./research/draft_evaluation/.venv/Scripts/python.exe ./research/draft_evaluation/verify_delivery.py
& ./research/draft_evaluation/.venv/Scripts/python.exe ./research/luna_evaluation/verify.py
```

The existing compiler and Python environment are local dependencies, not bundled source; see [compiler details](draft/tools/README.md). The PDF, source ZIP and manifest must be regenerated together when manuscript content changes; `verify_delivery.py` detects mismatches. The [draft guide](draft/README.md) explains the Overleaf XeLaTeX/BibTeX setup.

Build the separate full-thesis structure with `./thesis/build.ps1 -TimeoutSeconds 120`, then package it with `research/draft_evaluation/.venv/Scripts/python.exe thesis/package.py`. Its outputs are `thesis/build/main.pdf` and `thesis/overleaf-thesis.zip`. The local compiler/cache are reused from `draft/`; exported LaTeX sources compile independently. See the [folder transition record](docs/maintenance/document-folders.md).

Do not rerun frozen inference or threshold selection merely to check repository organization. Do not move files inside frozen studies casually: manifests record relative paths and hashes. Create a separate study/version for new experiments.
