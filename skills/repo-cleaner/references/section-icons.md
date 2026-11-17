# Section icons and colour

Use small outline icons beside major README headings when requested or when they improve navigation. The reference is [Modern Web Guidance](https://github.com/GoogleChrome/modern-web-guidance-src): its Quickstart, Why, package, evaluation, and privacy headings pair literal text with 24px SVGs. Its inspected icons use one blue; the colour mapping below is an adaptation, not an upstream rule.

## Choose a consistent system

- Use one outline family, a 24 × 24 viewBox, roughly 2px strokes, and matching line caps. Display at about 20–24px beside H2 headings. Do not mix emoji, filled icons, 3D renders, and thin outlines in the same heading system.
- Match the shape to the subject: terminal for running a command, package for distribution, book for guides, flask for evaluation, plain shield for security discussion. A shield with a checkmark implies a result; use it only when the adjacent text substantiates that result.
- Apply icons consistently at the chosen heading level or to a clearly selected group of reader landmarks. Do not automatically decorate every subsection, paragraph, badge, or link. Short READMEs may need none.
- Use an existing project icon family first. Otherwise the bundled [Lucide outline assets](../assets/section-icons/NOTICE.md) provide a small starting set. Recolour those SVGs rather than image-generating tiny icons. Copy only the needed icons and their license into the target repo.

## Choose colour from theme and meaning

Start from the existing project accent. Choose one mapping for the README and keep it stable: the same topic/role keeps its colour. Usually one primary accent, one or two related topic accents, and a neutral are enough. Use more only for a useful explicit topic scheme, not to give every section an unrelated colour.

| Role | Suggested treatment | Example icon | Meaning boundary |
| --- | --- | --- | --- |
| First action or most useful starting point | Primary project accent | Terminal or package | Emphasis, not an error/severity level |
| Concepts, features, or output | Related topic accent | Lightbulb or file | Group by topic; avoid a rainbow of priorities |
| Research and evaluation | Distinct related accent | Flask | An evaluation section does not imply passing results |
| General documentation and license | Neutral or subdued project accent | Book or file | Maintain readable contrast |
| Security/privacy information | Topic accent or neutral | Plain shield | No green certification signal by default |
| Actual prerequisite, caveat, or risk | Amber with explicit wording or a suitable native alert | Warning symbol if needed | Do not mark ordinary setup as dangerous |
| Destructive action, failure, or serious warning | Red with explicit text | Alert symbol if needed | Never use red merely for “most important” |

Importance should also be apparent from order, heading wording, and concise emphasis. Topic colour and severity colour are different meanings: do not assign red to ordinary research and also use it to mean failure in the same README. If the brand is red, keep brand identity recognizable and distinguish warning sections by explicit labels, shape, and native alerts rather than colour alone.

For a blue developer-tool identity, these are starting swatches, not mandatory values: primary `#1f6feb`, concept `#8957e5`, evaluation `#16856b`, neutral `#6e7781`, caution `#9a6700`, danger `#cf222e`. Check them against the actual light/dark backgrounds; adjust tones or use theme variants as needed. A green evaluation icon categorizes the topic; any pass claim still needs dated evidence in text.

## Use GitHub-compatible markup

Copy the selected icon to a stable local path, set an explicit `stroke` colour in its SVG, and keep the text heading. An SVG loaded through `<img>` does not inherit the surrounding heading's `currentColor`. Do not rely on CSS filters or inline `style` attributes to recolour or align icons; GitHub sanitizes inline styles. Use width/height attributes and inspect the result.

Example after copying the files into the target repository:

```markdown
## <img src="docs/assets/icons/terminal.svg" width="24" height="24" alt=""> Getting started

Run the shortest verified example.

## <img src="docs/assets/icons/flask-conical.svg" width="24" height="24" alt=""> Evaluation

Describe the method, dated result, scope, and limits.
```

Use empty alt text for decorative icons already explained by the adjacent heading. If an icon adds information, put that meaning in visible text as well. Keep heading names readable when images fail or are disabled. Avoid replacing whole headings with SVG images of text. Recheck navigation fragments after adding images; do not assume a hand-written slug matches GitHub's generated anchor.

Use explicit light/dark SVG variants with a `<picture>` fallback only if one colour cannot remain clear in both themes. Keep script, foreignObject, remote fonts, and external dependencies out of icon assets. Do not add runtime packages or an icon CDN just to display a few symbols.

## Verify and retain provenance

Inspect headings at desktop and phone widths, light and dark, with particular attention to wrapping, icon size, baseline alignment, and visibility. Check contrast against adjacent backgrounds. Aim for at least 3:1 for icons even when decorative; when an icon is necessary to understand content, this is the relevant non-text contrast threshold, not a blanket accessibility certification. Preserve real heading hierarchy and readable text.

Keep the source family/version or file hashes, license, and any modifications. The bundled assets are Lucide icons recoloured for README use; the Google/Chrome project logo is not included. Do not imply endorsement by the reference project. Keep colour choices in the asset notes or brief so later sections use the same system.

Sources: [GitHub sanitization pipeline](https://github.com/github/markup), [GitHub theme-aware images](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github#adding-an-image-to-suit-your-visitors), [W3C use of colour](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html), [W3C icon contrast](https://www.w3.org/WAI/WCAG21/Techniques/general/G207), and [Lucide licensing](https://github.com/lucide-icons/lucide/blob/main/LICENSE).
