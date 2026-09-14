# Master's thesis draft

This directory contains one standalone, English, two-column draft, currently ten pages including references. The original Overleaf-linked template is preserved separately in `../archive/overleaf-template/`. The [literature audit](../docs/maintenance/literature-audit-2026-09-07/README.md) records publication corrections, claim checks and restored source citations. The preceding [editorial review](../context/architecture-review/shortening-review.md) records the earlier nine-page version; the expanded references now use the tenth page without changing font size or margins.

**Latest revision, 9 September:** Section 6.3 reports the [updated-source evaluation](../research/effectiveness_v2/RESULTS.md): a 32-question diagnostic, 40-question prompt comparison and post-hoc repair of incomplete judge evidence. Neither the original nor the new comparison establishes an improvement in assistance. Original study results and bibliography remain unchanged. The current delivery checks are in `../research/effectiveness_v2/delivery-verification.json`; earlier review hashes below identify earlier versions.

The [8 September language review](../docs/maintenance/language-review-2026-09-08/README.md) replaces dense wording with direct explanations throughout the paper. It preserves the evaluation results, bibliography and study limitations, and records checks for the revised ten-page PDF and source ZIP.

A [second language pass](../docs/maintenance/language-review-2026-09-08/second-pass/README.md) further clarifies the abstract, component descriptions and assessment terminology. Its verification report records that revision's delivery hashes.

The subsequent [content update](../docs/maintenance/draft-content-update-2026-09-08/README.md) adds a data-use/reproducibility statement, an existing authored example and a later reference-quotation diagnostic. Its delivery hashes describe that revision. The original study scores remain unchanged.

The earlier [argument review](../docs/maintenance/draft-argument-review-2026-09-08/README.md) clarifies the architecture's contribution and fallback comparisons, adds a saved answer pair selected without using its outcomes, and states the practical implication. Its verification report records that historical delivery.

## Read or use in Overleaf

The [effectiveness revision](../docs/maintenance/effectiveness-focus-2026-09-08/README.md) puts answering real student questions and providing useful guidance at the center of the abstract, research questions and conclusion. Architecture and the retrieval comparison support that focus. Administrative savings are outside scope.

The [supervisor-review revision](../docs/maintenance/draft-supervisor-revision-2026-09-08/README.md) places the empty-reference sensitivity beside the headline results, adds main-only assistance agreement from saved assessments and an anonymized observed failure, and sharpens scope and reproducibility. Its delivery hashes describe that revision.

The latest [clarity review](../docs/maintenance/draft-clarity-review-2026-09-08/README.md) replaces dense wording, explains assessment terms and separates the research questions and judge comparisons into shorter blocks. It preserves all numerical results, study limits and the ten-page layout. Its verification report identifies the current PDF and source ZIP. No new model calls or human validation were added.

- Read `build/main.pdf` after the final verified build.
- Import `overleaf-draft.zip` into an Overleaf project and select `main.tex` as the main document.
- Use **XeLaTeX** and BibTeX. Tectonic, the local compiler used here, is based on XeTeX. Standard packages are used; no shell escape, API credentials, private datasets, or inference runtime is required to compile the manuscript.
- The source bundle contains only manuscript sources, bibliography and any referenced figure assets. It does not contain the private validation workbook or email questions.

The preceding manuscript was pushed to Overleaf as `f755cdb`. This new revision and its ZIP remain local. In the combined repository, select the root `main.tex`; in the standalone ZIP, select its `main.tex`.

## Local build

`build.ps1` runs the locally retained compiler with a bounded timeout and writes to `build/`. `inspect_pdf.py` checks the page count, renders every page and records text outside page boundaries. Run it using the research environment's Python. Current verification is in `../research/effectiveness_v2/delivery-verification.json`; older studies retain their historical verification records.

## Evidence and interpretation

The current controlled experiment is in `../research/luna_evaluation/`. The previous frozen local study and source-authority audit remain in `../research/draft_evaluation/`. Historical repository, email, deployment and PostHog analyses are in `../research/impact_analysis/`.

The current experiment uses production retrieval and prompt replay with controlled hosted Luna generation: 192 main questions, four prespecified policies, 354 unique main answers and a separate 20-question pilot. It fixes raw-query retrieval and excludes the production agent transport, tools and complete web lifecycle. Primary references and judgments are AI assessments. Repeated Luna and local Qwen assessments are sensitivity checks, not independent human validation. Their original 48-answer subset includes seven pilot answers; the new binary endpoint diagnostic reports the main cases separately. Correct routing and source-supported answering are separate outcomes. Neither establishes staff workload savings or causal impact.

The current confidential workbook is `../research/luna_evaluation/private/review_workbook.xlsx`; the previous study retains `../research/draft_evaluation/private/validation.xlsx`. They contain case-level evidence, answers and assessments and remain separate from the manuscript upload. Optional human-review columns start unreviewed; no human approval has been invented.

The production-question inspection in `../research/production_evaluation/` supplied the selectively logged July demand frame for the new study. Its private workbook is `../research/production_evaluation/private/production_questions.xlsx`. The ten-page architecture draft is preserved in `../archive/draft-2026-09-07-before-concision/`; the pre-architecture, pre-Luna and older deliveries remain in their dated archives.

The architecture account covers web and Discord interfaces, document preparation and provenance, retrieval/GPU services, MCP data adapters, state and telemetry, and a representative request flow. The native TikZ diagram in `architecture.tex` distinguishes source capabilities from the experimentally exercised path. Detailed source references, checkout revisions and deployment qualifications are indexed in [the architecture review](../context/architecture-review/README.md).

After building and inspecting, run `package.py` with the research Python environment. It verifies the build manifest and creates a six-file allowlisted ZIP: `main.tex`, `architecture.tex`, `related_work.tex`, `controlled_results.tex`, `references.bib`, and this guide. The three older results-table files remain for historical compatibility and are not active inputs or included in the current upload bundle. Run both `../research/draft_evaluation/verify_delivery.py` and `../research/luna_evaluation/verify.py` for final delivery verification; these check integrity, not human correctness.
