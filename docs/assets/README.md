# Asset sources and maintenance

| Asset | Origin | Purpose |
| --- | --- | --- |
| `banner.png` | Approved original light banner, generated for this project | Current README masthead |
| `hero.jpg` | Original AI-generated artwork created for Repo Cleaner; JPEG delivery conversion | Historical 0.1 identity; not used in the current README |
| `badge-skill.svg`, `badge-license.svg`, `badge-install.svg` | Original editable vector labels | Historical 0.1 custom labels; replaced by standard badges |
| `readme-before.png` | Qt rich-text render of the verbatim original README | Before state |
| `readme-after.png` | Qt rich-text render of the 0.1 README’s first screen | Historical 0.1 after state |
| `readme-transformation.png` | Equal-scale layout of the two actual local captures | Historical 0.1 comparison |
| `social-preview.png` | Native document typography on an opaque 1280 × 640 canvas, refreshed for 0.2 | Prepared GitHub social image |
| `audit-example.png` | Local typesetting of the condensed actual audit output | Current README example |
| `audit-example-source.md` | Editable text behind the current example image | Source for regeneration |

The README now uses ordinary live Shields badges. The older custom vector labels and generated banner are retained only as historical assets. Current audit and social images were typeset for this project. No third-party repository screenshots, brand marks, or artwork were reused. The original source remains the linked Markdown; badges are directly editable SVG. Generated artwork is decorative, not evidence of a working product.

## Historical 0.1 banner prompt

Created with OpenAI's built-in image generation on 2026-11-10 using this prompt:

> Use case: ads-marketing. Create a refined ultrawide GitHub README banner for a developer agent skill called Repo Cleaner. Exact headline text: “REPO CLEANER”. Exact subtitle: “Give good projects a better first impression.” Exact small label: “A REPOSITORY PRESENTATION SKILL”. Dark charcoal almost black background, clean silver and off-white editorial typography, exceptionally crisp legible letters. On the right, an abstract polished chrome folded page / open repository folder sculpture with fine illuminated edges and three subtle horizontal page lines. Left two thirds holds text with spacious intentional composition. Premium minimalist developer tool identity, quiet studio lighting, monochrome, subtle fine grain. Flat front-facing marketing graphic, horizontal 3:1 ratio, no web browser frame, no fake screenshots, no extra badges, no other logos, no watermark. Make this feel carefully designed and restrained, professional rather than gaming.

## Historical 0.1 preview method

1. Render [the preserved original README](../examples/original-readme.md) and [the current README](../../README.md) to HTML with a Markdown parser.
2. Resolve image paths relative to the repository root; use Qt 5 QTextDocument with Liberation Sans, 16px body text, a 32px document margin, and charcoal/light variants approximating GitHub's document colors.
3. Capture the first 960 × 760 pixels of each document at the same scale. Lay the captures side by side with equal dimensions on a 1600 × 800 canvas. Label them as local rich-text previews.
4. Inspect the full document at widths of 960px and 390px in both themes. This approximates layout; it does not test GitHub's HTML sanitizer, actual browser behavior, or horizontal table scrolling.
5. Lay out the unmodified banner on an opaque 1280 × 640 background for the social card. Keep its title and subtitle inside the canvas, with the project footer below. Verify the PNG remains under 1 MB.

The initial Chromium attempt was blocked by this environment's socket restriction. These assets therefore use a Qt document renderer and are explicitly labelled. A future live GitHub capture can replace them once authenticated browser access is available. Keep the same source and viewport when comparing versions.

## Current 0.2 previews

The audit image uses [its editable text](audit-example-source.md), condensed from [the actual fixture audit](../examples/notes-app-audit.md). It is typeset at 680px width with 20px body text and normal document headings. It is a source-based audit excerpt, not a fake application interface or a live GitHub screenshot.

README previews use the current Markdown and actual standard badge SVGs downloaded from the four Shields URLs referenced by the README. The downloads succeeded; preview caches are not part of the distributable. Source and local-layout checks covered widths 320, 375, 414, 768, and 960px in light/dark themes. The current native GitHub desktop view was subsequently inspected successfully; live mobile/dark-mode rendering remains unverified.

The new social PNG uses ordinary typography and the project’s purpose, with no chrome-folder illustration. Its dimensions and size are checked by the existing integrity test. Uploading the file to GitHub’s Social preview setting remains a separate action.

## Approved README banner

The current [banner](banner.png) was generated with OpenAI’s built-in image generation and approved in the conversation before publication. It is an original flat document illustration with a light background, charcoal title, and blue accent. It depicts Markdown headings, text, links, and an image placeholder; it is decorative identity, not a screenshot or evidence of application behavior. The original PNG is included without pixel edits.

The generation brief specified a 3:1 README masthead with the exact text “Repo Cleaner” and “READMEs · Examples · Guides”, a restrained document illustration, generous margins, and no badges, third-party logos, fake interface chrome, or 3D rendering. The native project description, ordinary badges, and navigation remain outside the image.

## Seed Atlas comparison

Added 2026-11-11. `seedatlas-before.jpeg` and `seedatlas-after.jpeg` are unchanged author-supplied screenshots (IMG_0370.jpeg and IMG_0369.jpeg respectively). `seedatlas-comparison.png` is an AI-composited illustration produced from those two images: before left, banner version after right, proportional panels, small labels, center divider and decorative slider handle. Originals remain the exact evidence. See [comparison provenance](../examples/seedatlas.md).
