# Local manuscript compiler

The verified local executable is `tectonic.exe`, version **0.17.0**. `../build.ps1` requires it at this exact location and sets the cache and font configuration paths. `runtime-manifest.json` records hashes of the retained executable, original download archive and font configuration.

`tectonic.exe` is an ignored machine-local dependency retained for the existing build. The redundant `tectonic.zip` download and disposable `uv-cache/` were deleted during cleanup; the manifest preserves the archive's historical hash and records its removal. These local artifacts do not belong in the Overleaf ZIP. `fonts.conf` is maintained configuration, currently using `C:/Windows/Fonts` and this workspace's font cache. A fresh checkout needs the compiler installed here and any path changes reviewed before a local build. The manifest records observed bytes; it is not an installer or an independently authenticated download record.

For a portable source-only route, import `../overleaf-draft.zip` into Overleaf and select XeLaTeX/BibTeX. The standard manuscript sources do not require the local compiler, cache, research data or an API key there.
