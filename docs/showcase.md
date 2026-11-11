# Presentation decisions

The current README uses an approved light document-style banner above GitHub's normal document styling, standard Shields badges, ordinary navigation links, and a Seed Atlas before/after comparison. The earlier chrome-folder banner and custom button-like badges are no longer used in the README or social preview.

## Approved banner

The new banner was previewed and approved before publication. Its light background, clear title, and small blue accent fit the existing repository presentation. The banner is the visible heading, while the project description remains native text below it. [Asset source and brief](assets/README.md#approved-readme-banner).

## Example and provenance

The [Seed Atlas comparison](examples/seedatlas.md) uses author-supplied before/after screenshots. Its static AI-composited illustration has a decorative central handle; unchanged originals are linked for exact evidence. The after screenshot is identified by its workflow banner. The source README response still showed the before text when checked, so this is not claimed as a verified live deployment.


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

The preview was typeset locally using Qt rich text and inspected at desktop and narrow widths in light and dark themes. Chromium could not start because socket creation was restricted. These local checks approximate layout. After the repository became publicly readable, its native GitHub desktop view was inspected: the header, standard badges, text links, code blocks, and audit image rendered correctly. Live mobile/dark-mode behavior and exact browser table scrolling remain unverified.

[Asset sources and maintenance](assets/README.md) · [Validation record](validation.md)
