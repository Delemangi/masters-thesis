# Master's thesis defense

The defense presentation, built with [Slidev](https://sli.dev). It is in English, about 30 minutes long, and uses the FINKI Hub style.

## Run it

```sh
pnpm install
pnpm dev
```

The deck opens at http://localhost:3030. Press `p` for the presenter view with notes, `o` for the overview and `f` for fullscreen.

## Offline copy and exports

| Command | Result |
|---|---|
| `pnpm exec slidev build --base ./ --out dist` | Builds the offline copy |
| `present.cmd` | Serves `dist/` at http://localhost:8080 with no internet needed. Build it first. |
| `pnpm exec slidev export --output out/master-thesis.pdf --timeout 120000` | Exports a PDF |
| `pnpm exec slidev export --format pptx --output out/master-thesis.pptx --timeout 120000` | Exports PowerPoint, with slides as images and notes kept |

## Files

- `slides.md`: slide content and speaker notes
- `style.css`: shared styles
- `layouts/`: slide layouts
- `components/`: charts and diagrams
- `public/`: logos and screenshots
- `qa-prep.md`: likely committee questions with short answers
- `classic/`, `spine/`: earlier design variants, not used by the deck

Fonts are bundled, so the deck loads nothing from the internet.
