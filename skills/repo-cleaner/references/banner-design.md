# Project-specific banners

Use this when creating, replacing, or auditing a README banner. For composition and prompt starters, use [banner-templates.md](../assets/banner-templates.md). These are design heuristics, not GitHub requirements or evidence of increased adoption.

## Choose what the visual must communicate

Read the README, relevant implementation or skill instructions, examples, existing identity, and available assets. Distinguish a project README from an explicitly requested personal profile. Do not infer public profile content from private memory.

Write a compact brief in working notes or [repo-brief.md](../assets/repo-brief.md):

- **Reader and job:** who uses it, what they provide, what changes, and what they receive.
- **Evidence:** paths or source URLs supporting the depicted capability and any usable outputs. Mark missing evidence.
- **Visual meaning:** map each dominant object or relationship to a verified project fact. A filename alone is not enough; inspect the relevant content.
- **Role:** identity, conceptual illustration, or proof. Keep these distinct even when placed together.
- **Direction:** selected recipe, preserved brand elements, exact text, and the README example or action beside it.

For a new concept, compare a couple of short alternatives before rendering; choose the one that communicates the task most directly. This can remain internal. Reuse settled user choices and authorization. Ask only when a meaningful identity change or missing fact affects the result.

| Available evidence | Prefer | Avoid |
| --- | --- | --- |
| Legible real output or interface | Output-led capture | Generating a substitute screenshot |
| Matched source and improved result | Transformation | Making the before state artificially worse |
| Verified process, but little visual output | Workflow illustration or exact diagram | Inventing a dashboard for a text-only skill |
| Distinctive project object or name/function connection | Domain metaphor | Assuming every AI tool needs a brain, robot, or network |
| Established logo/wordmark and a clear text opening | Identity masthead | Forcing an explanatory collage into a good identity |
| No useful visual evidence or concept | Text-first opening | Adding artwork to satisfy a template |

## Make the meaning specific

Use the project's verbs and objects, not just its category. For an agent skill, depict its task or deliverable rather than the agent host. A documentation skill can show an information hierarchy becoming clearer; a review skill can show a diff with linked findings; a file-based memory skill can show a saved project note being reopened with its source references. Verify those behaviors in the target before depicting them.

Apply two checks before generation:

1. **Title-hidden check:** would the main scene still communicate the intended task, transformation, or domain without its title? It need not identify the exact repository. Established identity-only mastheads are a valid exception; state that role and put the explanation in text.
2. **Swap check:** could the same scene advertise an unrelated project by changing only the name? If yes, replace the generic subject or choose a simpler identity/text opening. A gradient or attractive object cannot carry the missing meaning.

Do not ban a style universally. Pixel art, 3D, a mascot, or abstraction can work when supported by the identity or a clear metaphor. VHS's cassette relates to recording; arbitrary chrome does not acquire meaning because the repository uses AI. Borrow the communication pattern, not another project's character, logo, palette, or composition.

## Compose for a README

- Give the image one main idea and a clear focal point. Avoid a feature list disguised as a banner.
- Show a useful relationship: input and output, a selected path through context, an actual artifact, or a recognizable existing mark. Do not always place a title on the left and a floating object on the right.
- Keep large text to the project name and, when useful, one short supporting line. Keep commands, compatibility lists, metrics, badges, and detailed explanations as selectable README text.
- Start with a shallow canvas, roughly 3:1, when a compact masthead fits. Use a different ratio when the evidence needs it. README images have no universal required banner size; social previews are a separate deliverable governed by [github-discovery.md](github-discovery.md).
- Reserve comfortable margins around the title and main subject; do not rely on cropping away meaningful content. Ask the generator for the intended composition and inspect its actual output dimensions.
- Preserve existing project colours and identity where useful. Use readable contrast, not a mandatory dark/neon AI aesthetic. An opaque background may work in both GitHub themes without duplicate assets.
- Pair the visual with a real text title, a specific purpose, and a first action. Avoid repeating the same tagline in the image, subtitle, and introduction. Link an actual example when the banner only illustrates an idea.

## Generate or construct appropriately

Use the host's available image-generation tool for original artwork. Supply an inspected project-owned reference asset when exact identity continuity matters and the tool supports it. Do not require a paid provider, new key, or fixed generator. If generation is unavailable, deliver the specific prompt and a text-first or existing-asset fallback; report that no image was generated.

Use actual captures for proof and editable vector/layout tools for exact diagrams, marks, labels, and typography. Do not generate terminal output, data plots, UI, or before/after results and pass them off as observed behavior. If a concept resembles an interface, clearly call it an illustration in its caption and provenance. Do not send private code, logs, paths, or personal information to an image service; use an authorized public or synthetic brief.

Build the prompt in this order:

1. Placement, aspect ratio, and role (for example, conceptual README illustration).
2. Verified job, named input/output, and the visual relationship that conveys it.
3. Required objects, each with its meaning; existing identity and supplied references.
4. Composition, focal point, hierarchy, and whitespace.
5. Exact short text or an explicit no-text instruction; style, colour, and lighting.
6. Task-specific exclusions: invented UI, unsupported results, copied marks, unrelated symbols, or unreadable detail.

Generate one selected direction first. Revise against a concrete failed check; produce alternatives when the user requests exploration or a real design ambiguity remains. Avoid default batches of dozens of images. If generated text is unreliable, use an artwork-only version with exact typesetting where the host permits, or put all text in Markdown. Respect the host's image-editing rules.

## Accept only after inspection

| Check | Accept when | If it fails |
| --- | --- | --- |
| Grounding | Dominant objects/relationships trace to project facts or approved identity | Replace the subject, not just the styling |
| Meaning | The intended task survives hiding the title, or an identity-only role is justified | Simplify or choose another recipe |
| Truth | Illustrations, fixture renders, and real captures are accurately distinguished; nothing implies unsupported features | Correct claims or remove the asset |
| Legibility | Main subject and necessary text remain clear at desktop and phone widths | Remove detail, enlarge key forms, or use a compact variant |
| Integration | README purpose and first action work with images disabled; proof is nearby | Repair native text and evidence links |
| Maintenance | Final asset, prompt/source, alt text, origin, and limitations are recorded | Complete provenance before handoff |

Inspect the actual asset and its README placement at approximately 960px and 360px content widths in light and dark surroundings. If detailed evidence is unreadable on a phone, provide a legible excerpt and link the full asset. Check spelling, cropping, proportions, contrast, file size, paths, and alt text. An image viewed at native resolution is not a mobile layout check. Distinguish local previews from live GitHub rendering; report unavailable checks honestly.

Store essential assets in the target repo using relative links; keep editable sources and generation prompts when practical. For theme-specific variants use supported `<picture>` markup with an `<img>` fallback, only when needed. GitHub documents [image and picture support](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#images) and [theme-aware images](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/quickstart-for-writing-on-github#adding-an-image-to-suit-your-visitors).

Keep research notes, discarded candidates, and review evidence outside the installed package. A successful local asset does not authorize publication or update GitHub's social-preview setting.
