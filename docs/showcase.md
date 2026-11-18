# Presentation decisions

The current README uses transparent monochrome document artwork above GitHub's normal document styling, standard Shields badges, ordinary navigation links, and the refreshed Seed Atlas before/after comparison. The earlier light banner, chrome-folder banner and custom button-like badges are retained as historical assets.

## Transparent banner

The banner illustrates a dense Markdown document becoming a clearer README with a visual example and sections. It is conceptual artwork, not a screenshot. Black ink on transparency is used for light themes; white ink on transparency is selected for dark themes through `<picture>`. The reusable PNGs, editable SVG tint wrapper and the [generation brief and prompts](assets/readme-refresh-prompts.md) are included. The project description and first-use instructions remain native text below it.

## Example and provenance

The [Seed Atlas comparison](examples/seedatlas.md) uses the updated author-supplied comparison from 18 November 2026. Its static AI-edited display image has a decorative central handle; the unchanged source is linked for exact evidence. A GitHub source read confirmed the refreshed banner and README sections on the default branch; no new live browser capture is claimed.


The [notes-app example](examples/notes-app-audit.md) condenses an actual audit-only smoke check. Its image is a local typeset view of that documented output, not a product screenshot or a live GitHub capture. It shows findings and their evidence rather than an invented interface.

## What changed after the first review

- Replace custom SVG buttons with ordinary flat badges linking to the license, package, and installation guides.
- Use one title and a direct description instead of repeating a slogan inside and below a large banner.
- Put a small first-use route and a Seed Atlas before/after comparison ahead of a feature inventory.
- Use normal headings and lists instead of turning every explanation into a table or a marketing section.
- Keep visuals tied to a task or result; retain historical assets for provenance without displaying them as the current design.
- Add [source-by-source research](research/source-notes.md) and fold its reusable lessons into the skill.

## Design inputs

Hallmark informed the restraint, specificity, avoidance of fake interface chrome, and review of repeated structure. GPT Taste informed hierarchy, readable text, and removal of generic decorative labels. Their web-only CSS, custom typography, layout randomization, and animation prescriptions do not apply to a GitHub README. GitHub controls fonts, themes, layout behavior, and link interaction here.

The user's requested direction is a familiar repository README, informed by [Understand Anything](https://github.com/Egonex-AI/Understand-Anything) and [Awesome README](https://github.com/matiassingers/awesome-readme). Personal profile imagery and colors are not a default design system for this skill or its target projects.

## Verification limits

For the 18 November refresh, see the [current asset validation](assets/readme-refresh-validation.md). The following describes earlier releases:

The preview was typeset locally using Qt rich text and inspected at desktop and narrow widths in light and dark themes. Chromium could not start because socket creation was restricted. These local checks approximate layout. After the repository became publicly readable, its native GitHub desktop view was inspected: the header, standard badges, text links, code blocks, and audit image rendered correctly. Live mobile/dark-mode behavior and exact browser table scrolling remain unverified.

[Asset sources and maintenance](assets/README.md) · [Validation record](validation.md)
