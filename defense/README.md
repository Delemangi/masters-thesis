# Master's thesis presentation

Slidev deck for the master's thesis presentation (English, ~30 min), in the dark FINKI Hub style.

| Command | What it does |
|---|---|
| `pnpm install` | Install dependencies (once) |
| `present.cmd` (double-click) | Offline presentation from `dist/` via a tiny local server (needs Node, no internet). Presenter view: `http://localhost:8080/#/presenter/1` |
| `pnpm exec slidev build --base ./ --out dist` | Rebuild the offline copy after editing |
| `pnpm dev` | Present at http://localhost:3030 — `p` presenter view with notes, `o` overview, `d` dark/light, `f` fullscreen |
| `pnpm export` | PDF backup to `slides-export.pdf` (add `--output out/master-thesis.pdf`) |
| `pnpm exec slidev export --format pptx --output out/master-thesis.pptx` | PowerPoint (slides as images, notes kept) |

- `slides.md` — all content and speaker notes (HTML comments under each slide)
- `style.css` — typography, tables, figures and diagram styles
- `layouts/` — `hub-cover`, `section`, `closing`; `slide-bottom.vue` — branded footer
- `components/` — `HBar`, `StackBar`, `ForestPlot`, `StageChart` (native charts, numbers from the thesis)
- `public/` — logos and screenshots of finki-hub.com and chat.finki-hub.com

"Thank you" is the last slide.

Fonts (Unbounded, Inter) are bundled via `@fontsource`, so nothing loads from the internet. `qa-prep.md` has likely committee questions with short answers and the slide to jump to.
