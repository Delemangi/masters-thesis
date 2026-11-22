# A reference architecture for domain-specific RAG assistants

Master's thesis by Stefan Milev, mentored by Prof. Dr. Riste Stojanov, at the Faculty of Computer Science and Engineering (FCSE), Ss. Cyril and Methodius University in Skopje.

The thesis proposes an architecture for chatbots that answer questions from an institution's own documents and data. It is implemented as the [FINKI Hub chatbot](https://chat.finki-hub.com) ([source code](https://github.com/finki-hub/chat-bot)) and evaluated on real student questions in Macedonian. On held-out student emails, AI graders marked 70 to 77% of the answers correct and 1 to 3% wrong.

**Read it:** [thesis (PDF)](https://github.com/Delemangi/masters-thesis/releases/latest/download/master-thesis.pdf) | [defense slides (PDF)](https://github.com/Delemangi/masters-thesis/releases/latest/download/defense-slides.pdf)

## Contents

| Folder | Contents |
|---|---|
| [`thesis/`](thesis/) | Thesis sources |
| [`paper/`](paper/) | Shorter conference paper based on the same experiments |
| [`defense/`](defense/) | Defense presentation, built with Slidev |
| [`tools/`](tools/) | Local LaTeX compiler configuration |

The student questions and research data are private and are not included.

## Build

**Thesis and paper on Overleaf:** use XeLaTeX with BibTeX, and compile the root `main.tex` for the thesis or `paper.tex` for the paper.

**Locally on Windows:** run `./thesis/build.ps1` or `./paper/build.ps1`. Both need Tectonic, as described in [`tools/`](tools/README.md).

**Slides:** see [`defense/`](defense/README.md).

## License

The slide code in `defense/` is available under the [MIT License](defense/LICENSE). The thesis, the paper, and the slide text and images are not licensed for reuse.
