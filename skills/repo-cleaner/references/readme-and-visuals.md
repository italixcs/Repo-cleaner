# README and visual direction

## Shape the first screen around a decision

Answer: What is this? Who is it for? What can I see or try? Keep the promise and primary action as selectable text even if a banner repeats them. Put proof near the top and keep the shortest useful installation route easy to find. Add a short navigation row if needed.

Choose sections from the project rather than filling a fixed template:

| Project | Useful proof | First action | Later detail |
| --- | --- | --- | --- |
| Agent skill | Real input, output, and changed files | Load skill and try a prompt | Platforms, permissions, examples |
| CLI or library | Terminal output or runnable example | Install and run one command | API, options, troubleshooting |
| App | Actual screenshot or short task recording | Open demo or download | Setup, configuration, deployment |
| Research or data | Reproducible figure or sample | Reproduce or inspect data | Method, provenance, limitations |

Prefer a banner, one useful showcase, and a small badge row over decorative repetition. Omit sections that add no decision value. Avoid empty roadmaps, uninformative star charts, unused docs folders, and community links with no destination.

## Choose a visual direction

Reuse the project's identity. If none exists, choose typography, palette, composition, and asset style from its audience and purpose. Ask before a meaningful rebrand when preferences are unresolved. Do not copy another project's logo, imagery, or wording.

- Prefer native Markdown for explanation and simple tables. Use supported HTML only when it helps.
- Do not depend on scripts, custom CSS, iframes, or autoplay in a README. Verify Mermaid support in the target surface before using it.
- Keep long text out of images. Write descriptive alt text and explain key evidence nearby.
- Use responsive image markup and bounded widths. Avoid wide multi-column layouts that become unreadable on phones.
- Test light and dark backgrounds. An opaque banner can work in both; do not create redundant variants automatically.
- Keep essential assets in the repo, such as `docs/assets/`. Avoid temporary chat links, signed download URLs, and remote hotlinks for core proof.
- Crop screenshots to the useful action. Exclude credentials, private paths, names, source, and unrelated tabs from public images.

## Produce the right asset

Use image generation for requested original bitmap artwork when available. Use editable SVG for exact marks and diagrams. Use the actual product or rendered document for screenshots and recordings. Never generate fake screenshots and call them evidence.

| Asset | Purpose | Checks |
| --- | --- | --- |
| Banner | Recognition | Readable crop; promise also in text |
| Screenshot | Show a real result | Actual output; caption; legible at README width |
| Before/after | Explain an improvement | Same source and comparable viewport; label reconstruction |
| GIF or video | Demonstrate interaction | Short, useful, with a static fallback or linked thumbnail |
| Social preview | Recognize shared links | Prepare separately and upload through settings |

Optimize expensive images and record dimensions and size. Retain editable sources when practical. For social preview limits, check current GitHub docs in `github-discovery.md`. Keep important content away from crop edges.

## Badges and platform claims

Use a few badges with real destinations: license, actual CI, package version, or a documented install route. Static labels may describe documented properties but must not imply automated validation. Omit invented coverage, downloads, popularity, certifications, and endorsements.

Distinguish compatibility levels:

1. **Tested:** exercised in the named host/version with evidence and date.
2. **Documented route:** packaging and official discovery instructions checked; runtime behavior not exercised.
3. **Manual use:** agent can read instructions, but automatic discovery is unverified.

An Agent Skills folder does not establish a native plugin, marketplace entry, MCP server, or universal host support. Link host names to installation details instead of building a badge farm.

## Guides and organization

Keep the shortest first success in the README. Move platform variants, troubleshooting, and long walkthroughs to linked docs. Maintain one canonical instruction source.

For a single skill, prefer `skills/<name>/SKILL.md` and its supporting resources. Keep the public README, contributing guide, changelog, and gallery outside the installable package. Do not move source modules, rename packages, or add deployment infrastructure as presentation cleanup. Explain structural changes that would affect links or distribution before making them.

For every showcase, retain its source and capture method, including whether it is a concept, local render, or live result. Refresh related screenshots after visible changes. Remove stale proof when it cannot be updated.
