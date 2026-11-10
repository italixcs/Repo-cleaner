# GitHub discovery and settings

## Read the existing state

Inspect visibility, About description, homepage, topics, default branch, releases, license, and existing social preview. Use connected tools or CLI first. If a setting cannot be read, mark it unknown rather than absent. Committing a settings proposal does not apply it.

## Write useful metadata

Write an About sentence combining project type, concrete result, and audience. Use words people plausibly search for rather than repeated synonyms. Set a homepage only when a real, useful demo/docs/site exists; do not invent a website or add a circular link just to fill it.

Read current GitHub topic rules before publishing. The official page below currently allows up to 20 topics, each at most 50 characters, using lowercase letters, numbers, and hyphens. Prefer a focused set, usually 6–12, rather than filling the limit.

Record why each topic fits:

| Candidate | Evidence | Decision |
| --- | --- | --- |
| `agent-skills` | Real SKILL.md and resources | Include for a skill package |
| Specific agent name | Documented install route with accurate support status | Include if substantiated |
| Unrelated popular framework | No actual relationship | Exclude |

Cover project type, main task, audience, and verified ecosystem. Do not add every agent name for traffic. Preserve relevant existing topics when replacing a list. Identify misleading topics for removal. Do not promise ranking or stars.

Private repos remain accessible only to authorized users. Topic names themselves are public. Keep visibility unchanged unless explicitly authorized; review private information before an authorized publication.

## Prepare, apply, and read back

1. Prepare exact description, homepage, topics, and social image path.
2. Apply with authorized tools when settings are in scope. Read fresh state before writing and preserve unrelated values.
3. Use a browser when connector/CLI lack the operation. If neither works, provide copyable values and the exact settings page.
4. Read back applied values. Report **applied**, **prepared**, or **blocked**, with the reason. Never imply that an asset committed to the repo is a configured preview.

GitHub's documented social upload is Settings → General → Social preview. Check private repo eligibility: GitHub currently permits first upload for public repos, or a private repo with a previously uploaded image. Do not make a repo public to bypass that restriction.

Prepare an opaque PNG/JPG/GIF under 1 MB, preferably 1280 × 640; verify current requirements first. Test the crop. Report an ineligible first private upload as prepared for publication.

## Beyond metadata

Recommend a few substantiated next actions: a useful release with notes, readable examples, a reproducible demo, working docs, or a contribution path. Edit profile pins only if requested. Suggest suitable directories or communities without posting, messaging, or submitting listings unless authorized.

If asked to measure results, compare available traffic and referrals over comparable periods; report when data are unavailable. Treat stars as observations rather than proof of causation. Do not schedule follow-ups unless requested.

## Official references

Checked 2026-11-10; verify again before applying time-sensitive requirements.

- [Topics](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics)
- [Social preview](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview)
- [READMEs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes)
- [Repository topics API](https://docs.github.com/en/rest/repos/repos#replace-all-repository-topics)
