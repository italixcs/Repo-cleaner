# Banner and section-icon research

Reviewed 2026-11-17. This focused follow-up reuses the [earlier 123-entry inventory](README.md) and revisits relevant examples alongside additional AI projects, agent skills, and templates. It does not repeat that entire census. Thirteen repository references were inspected, plus OPC's banner-authoring workflow and supporting platform/accessibility documentation.

Seven linked identity/hero assets were downloaded and visually inspected. Other observations below concern README or SVG source. No upstream README or visual asset is redistributed in this notebook. The reusable icon set comes separately from Lucide with its license. Product commands, adoption effects, and compatibility claims were not tested.

## The missing decision

The existing skill preferred useful visuals over decoration but did not explain how to derive a scene from the repository. A name, tagline, and attractive object could satisfy its advice while communicating little about the actual task.

The revision adds an evidence-to-concept step, five adaptable recipes, and acceptance checks. Style remains flexible: 3D, mascots, or abstraction can work when they have a specific connection to the project. Existing identity and no banner remain valid choices.

## Source observations

| Reference | Observed | Decision and limits |
| --- | --- | --- |
| [Understand Anything](https://github.com/Egonex-AI/Understand-Anything) | Inspected hero turns tangled code documents into ordered graph views, with a guided process and mascot | Illustrate the actual transformation; this is conceptual artwork, not a screenshot. Do not copy its character, gold identity, dense labels, or compatibility claims |
| [VHS](https://github.com/charmbracelet/vhs) | Inspected cassette artwork; README links terminal GIFs to tape sources | A name/function metaphor can be specific. Keep demo sources; the cassette itself is not proof |
| [Markdownify](https://github.com/amitmerchant1990/electron-markdownify) | Source separates small identity from editor GIF and setup | Product output can carry the explanation. Animation frames and old setup claims were not verified |
| [Anthropic Skills](https://github.com/anthropics/skills) | Text-led explanation of skill folders, examples, and installation | A skill catalog can work without a bespoke hero. Do not invent a dashboard for a folder of instructions |
| [Superpowers](https://github.com/obra/superpowers) | Text-led workflow and host-specific installation navigation | Explain the actual task sequence; a decorative superhero is unnecessary |
| [Browser Use](https://github.com/browser-use/browser-use) | Inspected wordmark and theme variants; separately linked task demonstration | Separate recognition from demonstration. This review did not execute its demo or verify product claims |
| [Dify](https://github.com/langgenius/dify) | Inspected cover primarily uses wordmark, type, and blue accent | Identity-only is a valid choice; a branded cover does not prove functionality |
| [Ollama](https://github.com/ollama/ollama) | Inspected llama mark above native title and commands | Preserve an established mark; do not borrow its mascot or infer capabilities from it |
| [smolagents](https://github.com/huggingface/smolagents) | Inspected wordmark integrates the established Hugging Face character; source follows with code demo | Playful identity can coexist with practical evidence; the character does not explain code-agent behavior alone |
| [Best README Template](https://github.com/othneildrew/Best-README-Template) | Source separates logo, purpose, navigation, and screenshot slots | Reserve space for relevant proof; omit placeholders and unnecessary sections |
| [Standard Readme specification](https://github.com/RichardLitt/standard-readme/blob/main/spec.md) | Banner is optional and distinct from title | Keep real text and stable local assets; its library-oriented section order is not universal |
| [OPC Skills](https://github.com/ReScienceLab/opc-skills) | Inspected pixel identity; banner workflow offers format/style iteration | Preserve identity coherence. Do not adopt its default 20-image batch, new API-key requirement, or assume its 2:1 choice is a GitHub rule |
| [Modern Web Guidance](https://github.com/GoogleChrome/modern-web-guidance-src) | Headings use 24px outline SVGs; terminal, bulb, and shield sources share blue stroke | Adopt semantic landmarks beside text. Our multi-colour mapping is an adaptation; do not copy Google branding or depend on inline CSS |

The previous notebook described Understand Anything's image broadly as a product visual. This inspection establishes that its current hero is conceptual artwork. Historical source-review notes remain dated evidence, not verification of the current asset as a real capture.

## Rules adopted

1. Derive the scene from verified input, operation, output, or established identity. Explain each dominant object's meaning.
2. Choose output-led, transformation, workflow/context, domain metaphor, or existing identity. Preserve the text-first fallback.
3. Check a new illustrative concept with its title hidden and an unrelated name substituted. Revise when only the title makes it relevant.
4. Distinguish concept art, identity, fixture renders, and real proof. Capture actual results and construct exact diagrams.
5. Use one main idea, little embedded text, and native first-use instructions. Inspect phone/desktop and light/dark placement.
6. Use small consistent outline icons for useful section landmarks. Map shapes to topics and colours to a stable palette; communicate importance and risk in words too.
7. Preserve asset sources, prompts, licenses, and maintenance information. Avoid mandatory mass generation or new paid services.

These are design decisions, not statistical evidence of improved traffic, stars, adoption, or agent quality.

## Section palette

Repo Cleaner's example uses blue for first use/distribution, violet for purpose/output, teal for research, and gray for reference/security/license. The plain gray shield identifies a topic without implying a passed audit. Actual caveats remain explicit text and use suitable native alerts when needed.

The [Lucide asset notice](../assets/icons/NOTICE.md) retains source hashes, modifications, and the complete license. These SVGs have matching geometry and explicit colours. They were obtained separately from Lucide; Google/Chrome marks are not included.

## Platform evidence

- [GitHub image syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#images) and [theme-aware pictures](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github#adding-an-image-to-suit-your-visitors).
- [GitHub markup pipeline](https://github.com/github/markup): sanitization removes inline styles.
- [W3C use of colour](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) and [icon contrast](https://www.w3.org/WAI/WCAG21/Techniques/general/G207): colour cannot be the only meaning; necessary icons need at least 3:1 against adjacent colours.

See the [worked banner brief](../examples/banner-brief.md) and [validation record](../validation.md).
