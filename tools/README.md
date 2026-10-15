# Local manuscript compiler

Shared by `../thesis/build.ps1` and `../paper/build.ps1`. The verified local executable is `tectonic.exe`, version **0.17.0**. Both build scripts require it at this exact location and use `cache/` and `fonts.conf` from this folder. `runtime-manifest.json` records hashes of the retained executable, original download archive and font configuration.

`tectonic.exe` and `cache/` are ignored machine-local dependencies and do not belong in Overleaf. `fonts.conf` is maintained configuration, currently using `C:/Windows/Fonts` and an absolute path to this workspace's font cache; review that path in a fresh checkout. The manifest records observed bytes; it is not an installer or an independently authenticated download record.

Overleaf does not need any of this: select XeLaTeX with BibTeX and compile the root `main.tex` (thesis) or `paper.tex` (conference paper).
