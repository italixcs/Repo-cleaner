# Asset sources and maintenance

| Asset | Origin | Purpose |
| --- | --- | --- |
| `hero.jpg` | Original AI-generated artwork created for Repo Cleaner; JPEG delivery conversion | README identity |
| `badge-skill.svg`, `badge-license.svg`, `badge-install.svg` | Original editable vector labels | Links to the skill, real license, and installation guide |
| `readme-before.png` | Qt rich-text render of the verbatim original README | Before state |
| `readme-after.png` | Qt rich-text render of the current README's first screen | After state |
| `readme-transformation.png` | Equal-scale layout of the two actual local captures | Comparable showcase |
| `social-preview.png` | Separate 1280 × 640 layout using the original banner and selectable-layout footer | Prepared GitHub social image |

All assets were made for this project. No third-party repository screenshots, brand marks, or artwork were reused. The original source remains the linked Markdown; badges are directly editable SVG. Generated artwork is decorative, not evidence of a working product.

## Banner prompt

Created with OpenAI's built-in image generation on 2026-11-10 using this prompt:

> Use case: ads-marketing. Create a refined ultrawide GitHub README banner for a developer agent skill called Repo Cleaner. Exact headline text: “REPO CLEANER”. Exact subtitle: “Give good projects a better first impression.” Exact small label: “A REPOSITORY PRESENTATION SKILL”. Dark charcoal almost black background, clean silver and off-white editorial typography, exceptionally crisp legible letters. On the right, an abstract polished chrome folded page / open repository folder sculpture with fine illuminated edges and three subtle horizontal page lines. Left two thirds holds text with spacious intentional composition. Premium minimalist developer tool identity, quiet studio lighting, monochrome, subtle fine grain. Flat front-facing marketing graphic, horizontal 3:1 ratio, no web browser frame, no fake screenshots, no extra badges, no other logos, no watermark. Make this feel carefully designed and restrained, professional rather than gaming.

## Recreate the previews

1. Render [the preserved original README](../examples/original-readme.md) and [the current README](../../README.md) to HTML with a Markdown parser.
2. Resolve image paths relative to the repository root; use Qt 5 QTextDocument with Liberation Sans, 16px body text, a 32px document margin, and charcoal/light variants approximating GitHub's document colors.
3. Capture the first 960 × 760 pixels of each document at the same scale. Lay the captures side by side with equal dimensions on a 1600 × 800 canvas. Label them as local rich-text previews.
4. Inspect the full document at widths of 960px and 390px in both themes. This approximates layout; it does not test GitHub's HTML sanitizer, actual browser behavior, or horizontal table scrolling.
5. Lay out the unmodified banner on an opaque 1280 × 640 background for the social card. Keep its title and subtitle inside the canvas, with the project footer below. Verify the PNG remains under 1 MB.

The initial Chromium attempt was blocked by this environment's socket restriction. These assets therefore use a Qt document renderer and are explicitly labelled. A future live GitHub capture can replace them once authenticated browser access is available. Keep the same source and viewport when comparing versions.
