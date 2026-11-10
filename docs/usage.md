# Usage and prompts

Choose a repository the agent can access. Give it the audience and constraints you already know; the skill asks about missing facts and meaningful design choices.

## Audit only

```text
Use repo-cleaner to audit this repository's public presentation.
Do not change files or GitHub settings. Prioritize gaps in the first
screen, proof, installation, documentation navigation, and discovery.
For every finding, show its evidence and a concrete recommendation.
```

Expect prioritized findings, a proposed README outline, an asset plan, and specific metadata suggestions. Unknown settings should remain unknown; the agent should not invent missing data.

## Full makeover

```text
Use repo-cleaner to improve this repository's README, useful visuals,
guides, and GitHub metadata. Keep the existing identity where it works.
Create actual showcases from the project. Ask about missing facts or
consequential design choices. Preserve application behavior, license,
and visibility. Verify the finished reader path.
```

Expect implemented presentation files, verification evidence, and a short handoff separating applied settings from prepared or blocked ones. Commit/push follows your authorization and project workflow.

## Publish an AI skill clearly

```text
Use repo-cleaner on this skill repository. Show a real task and output,
keep the installable package separate from the public guides, and
check installation paths for each documented host. Distinguish runtime
tests from documented compatibility. Recommend only topics we can
support with evidence.
```

## Improve discovery without rewriting everything

```text
Use repo-cleaner to improve discovery only. Review the About text,
homepage, topics, and social preview. Give exact proposed settings
and an evidence-based reason for every topic. Preserve visibility
and relevant existing metadata.
```

## Keep proof current

```text
Use repo-cleaner to refresh this repository after its latest changes.
Check screenshots, installation commands, links, badges, and platform
claims against the current version. Remove stale proof and update
only presentation files that need it.
```

## Expected handoff

| Result | What should be included |
| --- | --- |
| Changes | Files and reader-facing improvements |
| Verification | Links, commands, images, desktop/mobile, light/dark, and exact limits |
| GitHub settings | Applied, prepared, or blocked; exact values |
| Remaining work | A few concrete priorities, if any |

The workflow adapts to the repository; it does not impose Repo Cleaner's charcoal and silver style on your projects.
