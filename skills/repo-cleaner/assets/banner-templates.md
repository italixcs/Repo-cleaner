# Banner recipes

Choose one recipe using [banner-design.md](../references/banner-design.md). Replace bracketed fields from inspected project evidence; remove unused fields. These are adaptable composition and prompt templates, not ready-made branding or mandatory sections. Do not paste unresolved placeholders into a target repo.

## 1. Output-led

**Use:** apps, CLI tools, generators, or skills with a useful real result.

**Need:** authorized screenshot/render/output, source revision or fixture, and capture method.

**Composition:** make one meaningful result dominant. Use a small identity area only if needed. Crop irrelevant space without changing what the result says. Keep small text outside the image or link a larger view.

**Capture brief — not an image-generation prompt:**

> Show [specific task result] from [source path/revision or authorized fixture].
> Capture [view/state] at [viewport]; retain [details needed to understand it].
> Exclude private data and unrelated UI. Preserve the content of the result.
> Place [optional existing mark/name] beside the capture without covering proof.
> Caption it as [actual capture / local render / synthetic fixture output].
> Keep the source and capture method with the delivered asset.

**README pairing:** one sentence describing the task, a link to the example, and a first-use action. Do not invent a screenshot when capture is unavailable; choose a conceptual recipe instead.

## 2. Transformation

**Use:** formatting, refactoring, document design, repository presentation, or conversion where the change is the point.

**Need:** verified input and output; for proof, use the same source and comparable scale. If only the capability is known, choose an explicitly conceptual illustration.

**Composition:** two comparable states joined by the visible operation. Keep the essential material recognizable across them. Show what improves rather than adding meaningless sparkle.

**Illustration prompt:**

> Create a [ratio] conceptual README illustration for [project].
> It [verified action] on [input] to produce [output].
> Depict [specific initial arrangement] becoming [specific final arrangement].
> Keep [shared elements] recognizable in both states. The visual change is
> [verified improvement], not deletion of the source or an invented feature.
> Use [existing project visual language], one clear focal relationship,
> large simple forms, and generous margins. Exact text: [name / short labels / none].
> Exclude fake application chrome, metrics, badges, and [unrelated motifs].
> This is an illustration, not a screenshot or measured before/after result.

**README pairing:** label the concept and link a real before/after when available. For evidence, render the actual pair deterministically instead of using this prompt.

## 3. Workflow or context

**Use:** agent skills, retrieval tools, orchestration, review, or project memory with little UI.

**Need:** the real steps, boundaries, and deliverables from instructions or implementation.

**Composition:** emphasize one useful connection or handoff, such as a source note carried into a resumed task. Include only enough stages to explain the capability; avoid an architecture poster in the header.

**Illustration prompt:**

> Create a [ratio] README concept for [project], which [verified job].
> Show [concrete input] connected through [actual operation] to [concrete output].
> The dominant relationship is [why this connection matters to the user].
> Use these objects only: [object = project meaning; object = project meaning].
> Make [important connection] visually dominant and [secondary material] quieter.
> Preserve [existing identity]. Exact short text: [text / none].
> Use [style justified by the project] and keep the main idea clear at phone width.
> Exclude invented integrations, generic AI circuitry, and [unsupported capability].
> This is conceptual art; exact topology and operational detail stay in text.

**README pairing:** a short task/example and its actual output. Use an exact SVG/Mermaid diagram instead if readers must trust the number, order, or meaning of connections.

## 4. Domain metaphor

**Use:** a distinctive domain object or a name that meaningfully connects to the function.

**Need:** an explicit mapping between the object, its action, and the verified project job. A decorative name association alone is weak evidence for a capability illustration.

**Illustration prompt:**

> Create an original [ratio] README banner for [project].
> Use [domain object] as a metaphor for [verified function], because [specific link].
> Show it [action that expresses the function], with [relevant project detail].
> Make the object/action the focal point. Use [established style or suitable medium],
> [palette], and room for [exact name / native Markdown title outside the image].
> Avoid [unrelated generic tech motifs], copied mascots, fake UI, and extra slogans.
> This is identity/concept art, not evidence of a real product result.

**README pairing:** explain the actual function in plain text and place a real example nearby. A recording cassette can fit a recording tool; it would not explain an arbitrary agent skill.

## 5. Existing identity

**Use:** a recognizable, approved project mark or wordmark that already does the recognition work.

**Need:** the actual project-owned asset and any established usage constraints. Do not invent a mascot or redesign a logo to fill this recipe.

**Layout brief:**

> Build a compact [ratio or natural asset dimensions] masthead using [asset path].
> Preserve the mark, proportions, lettering, and established colours.
> Give it clear space and a background compatible with [light/dark requirements].
> Use [exact short supporting text / no extra text]. Keep the purpose and example
> in native README text. Do not add decorative objects to simulate functionality.

Prefer placing the original asset with exact layout tools. If new surrounding artwork is requested, pass the inspected asset to the available image tool and verify fidelity. Do not regenerate a precise logo from a verbal description.

**README pairing:** a direct description, a useful example or demo, and the first action. This recipe is intentionally about recognition; it does not pass as visual proof.

## No-banner fallback

Use a text title, a specific one-sentence purpose, a small working example, and the first action. If the user explicitly requested a banner but evidence is incomplete, provide a grounded concept/prompt with the missing facts identified; use a modest title treatment only if that satisfies their request. Do not silently replace a requested deliverable with nothing.
