# README asset validation — 18 November 2026

Scope: colorful 2D mascot banner, complete mascot-free comparison and provenance. The installable skill package is unchanged.

- `banner-mascots.jpg`: 2172 × 724 RGB, baseline JPEG, 468,035 bytes. Built-in image generation edit using the author-supplied orange block-shaped Claude pet and blue Codex terminal pet references; no name labels. Claude works at a laptop and Codex presents the organized README. No 3D rendering. Both characters belong only to the masthead.
- `seedatlas-comparison-full.jpg`: 1536 × 1024 RGB, baseline JPEG, 621,107 bytes. Format-only export of the complete existing handle-only PNG, with both panels visible and no mascots. The new path avoids reusing the URL of an earlier truncated upload.
- Fully decoded both JPEGs using Pillow, confirmed non-progressive encoding, dimensions and file sizes. Git transport is used for the complete binary assets.
- The unchanged comparison source SHA-256 remains `ff6d45da1064cfe770f2579fc6fea555435d6b73871b5c728016a4599abbacc8`, matching the author's `IMG_0417.png` upload exactly.
- Inspected local asset layout boards at 960px and 360px content widths on white and dark surroundings. The banner title and mascot silhouettes remain recognizable; comparison text needs the full-size source at narrow widths. These boards are asset-layout previews, not full README browser captures.
- Six repository integrity tests passed: `python3 -m unittest discover -s tests -v`. `git diff --check` passed.
- Earlier transparent monochrome banner variants and the handle-only PNG remain historical assets. Discarded generated 3D concepts are not included.

No new SkillSpector scan or host-runtime test is claimed. Live GitHub verification is recorded below after publication to the existing PR branch.
