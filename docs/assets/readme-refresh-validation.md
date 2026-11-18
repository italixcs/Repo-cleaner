# README asset validation — 18 November 2026

Scope: README banner, refreshed Seed Atlas comparison and their provenance documents. The installed `skills/repo-cleaner/` package is unchanged.

- Inspected local asset layout boards at 960px and 360px content widths on light (`#ffffff`) and dark (`#0d1117`) backgrounds. These are image-layout previews, not screenshots of GitHub or a full rendered README.
- The banner wordmark and document transformation remain recognizable at phone width. Screenshot text in the two-panel comparison requires opening the full-size source; the README explains the change in native text and links the unchanged upload.
- Both banner PNGs are 2172 × 724 RGBA with transparent canvas and document interiors. The black source contains 1,418,308 fully transparent pixels out of 1,572,528. The white variant is an Inkscape PNG export of the included SVG tint wrapper. Its alpha channel is pixel-identical to the black source and its RGB channels are pure white.
- The SVG embeds the original PNG and applies an SVG source-alpha filter. It is self-contained and recolorable through `flood-color`; there are no scripts or remote asset dependencies. GitHub consumes PNGs, so rendering does not depend on SVG filter support.
- Both the comparison source and AI-edited display image are 1536 × 1024. The original upload is copied unchanged. The generated display image is explicitly labeled AI-edited, with a decorative, non-interactive center handle.
- Source-read the Seed Atlas default-branch README through GitHub and confirmed the new concept banner, v0.5.0 badges, feature overview and guide navigation.
- Reviewed the exact diff and preserved the MIT license, attribution, skill package and existing release.

Local Chromium could not launch because socket creation was denied by the environment. Full README browser layout and live GitHub theme switching were therefore not exercised. Theme selection was checked in the source markup; local image boards verified the selected assets' appearance. This refresh does not claim a new SkillSpector scan or host-runtime test.

Required repository integrity command: `python3 -m unittest discover -s tests -v` — 6 tests passed, covering package structure, local document links, copy-only installation commands, metadata constraints, social preview dimensions and historical badge SVGs.
