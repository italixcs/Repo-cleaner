# Validation record

Checked on 2026-11-10. This is a record of the first review version, not a benchmark or a universal compatibility claim.

## 0.2.0 presentation review

The second version replaces the chrome-led opening and custom buttons with a native header, ordinary flat badges, and a task example. A source review covers 123 README entries, of which 122 returned nonempty content. This is source/structure coverage, not 122 live visual audits. See [the coverage record](research/README.md) and [per-source notes](research/source-notes.md).

A fresh small Python utility fixture requested ordinary GitHub presentation and documentation-only changes. The updated skill replaced generic slogans and a forced feature table with concrete requirements, copy/import setup, function behavior, and sample input/output. It added no artwork, badges, dependencies, tests, or application-source changes. Examples were manually checked against the source; no host runtime was exercised.

The installed skill package validates. The six existing integrity checks cover the revised files. Local previews use actual downloaded standard Shields images. The final native GitHub desktop view was also inspected after the repository became publicly readable: the header, standard badges, navigation, code blocks, and audit image displayed correctly. Mobile and dark-mode checks remain local approximations.

GitHub reported public during the final read-back; no visibility mutation was performed. The settings handoff records the difference from the earlier private-review preference.

## 0.1.0 baseline

## Package and documentation checks

`python3 -m unittest discover -s tests -v` passes six checks covering the installable package, local links/anchors, complete Codex and Claude Code folder-copy commands, existing-install protection, topic syntax/declared visibility metadata, social image dimensions/size, and static vector labels. The skill creator's package validator also passes on the installed skill source.

The folder-copy checks run the documented shell commands with an isolated temporary home directory, compare every copied file by hash, and confirm a second run refuses to overwrite the installation. They do not launch Codex or Claude Code. PowerShell commands were reviewed but not executed on Windows.

## Behavioral smoke checks

Two fresh agent tasks used the skill with local synthetic repositories, without the author's intended answers. They were instructed to use only the fixture evidence and avoid external services.

### 1. Audit-only notes app

Input: a README with “Coverage 100%” and “All agents supported” static badges, an `npm run start` instruction, a manifest exposing only `dev` and `build`, and metadata describing a plain JavaScript/localStorage notes app with no tests, CI, AI integration, or screenshots. Topics included `react`, `ai`, `chatgpt`, and `notes`; the social preview was unknown.

Request: audit only, return prioritized findings, a README outline, and proposed settings; do not modify files or settings.

Observed output:

- Identify the missing start script and recommend `npm run dev`, while marking execution unverified.
- Remove unsupported coverage and agent badges.
- Replace unrelated framework/AI topics with evidence-backed notes/JavaScript/localStorage/Vite topics.
- Recommend actual product proof rather than a generated screenshot.
- Keep unknown settings unknown and preserve private visibility.
- Return recommendations without changing files or settings.

### 2. Implement a small CLI makeover

Input: a two-line README and a small inspected Python CLI that counts lines in one UTF-8 file. Maintainer instructions specified Python 3.10+, no packages, a simple text-first direction, unchanged source, no chosen license, and no external services or metadata access.

Request: implement a complete small README/docs makeover and verify safe examples; modify documentation only.

Observed output: a clear README, one focused usage guide, and a two-line sample. The agent exercised the sample, counting cases, help and error behavior, and checked links and source preservation. It reported Python 3.12.14 as the exercised runtime rather than claiming every supported version was tested. It did not access external services or change application source.

These checks show useful behavior on two small tasks. Larger repositories, other models, settings writes, and native agent-host execution still require their own evidence.

## Visual checks and limits

The generated banner was visually inspected. Local Qt rich-text previews were inspected at widths of 960px and 390px in light/dark themes. The social PNG is 1280 × 640 and below 1 MB. See [asset provenance](assets/README.md).

Chromium could not start because socket creation was restricted. Qt previews approximate layout; live GitHub rendering, its HTML sanitizer, browser table scrolling, native agent discovery, Windows execution, and applied metadata settings remain unverified. The GitHub connector can write content but exposes no metadata update operation; the browser session was signed out. [Exact settings are prepared](github-settings.md).

## 2026-11-17 banner and section-icon update

The structural validator passes on the installed candidate. Six repository integrity tests pass, covering package/links, complete folder-copy installation, existing-install protection, metadata, social image specification, and historical SVG labels. Heading-anchor handling was adapted to ignore decorative HTML image tags. No product runtime support is inferred.

Manual review exercised three decisions: the worked Repo Cleaner transformation brief maps visual elements to repository evidence; a synthetic file-based memory skill supports a saved-note handoff concept without invented vector/cloud services; the tiny LineCount fixture needs a text-first opening and real command/output rather than artwork. A safe two-line input returned `2` under Python. These are author reviews, not independent behavioral evidence. Three fresh-agent checks were attempted but each stopped at the host usage limit before producing results. They remain blocked; no A/B improvement claim is made.

The seven icon SVGs parse, contain no script/foreignObject/external references, and use explicit strokes. Calculated contrast against white and GitHub-dark backgrounds exceeds 4:1 for each colour (minimum approximately 4.08:1). Shape and heading text preserve meaning without colour. Licensed upstream geometry is unchanged.

Local Qt rich-text previews were inspected at 960px and 360px in light/dark surroundings. The heading icons remain recognizable and align with their text. These are approximations: network badges were omitted, code wrapping and alert treatment differ from GitHub, and the showcase requires its linked originals for phone reading. Chromium could not launch because socket creation was denied. Native GitHub rendering and actual anchor behavior remain unverified for this revision.

No new banner was generated. The worked example validates the concept/prompt stage only; the approved existing artwork remains. The [focused research](research/banner-and-icons.md) distinguishes source review from seven actual asset inspections.

The [final static scan](security/banner-update.md) fully inspected 19/19 files with zero findings. A prose apostrophe that confused the shell parser was rephrased without changing the prompt meaning. Earlier incomplete scans remain private evidence; no suppression or caller exclusion was added. The prior 0.2.1 report is historical only.
