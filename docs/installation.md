# Installation

Repo Cleaner is a portable folder of agent instructions, not a native plugin or MCP server. Start with the manual route if you want to inspect it before installing.

## Prerequisites

Use an agent that can read local Markdown and supporting files. Editing repositories requires file access; applying GitHub settings requires authorized GitHub access. Original generated artwork or screenshots need suitable optional tools. This skill itself has no service, backend, paid subscription, or extra API key. Your agent/model and optional tools may have their own costs.

While this repository is private, Git cloning requires an account with access. Do not paste a token into commands or prompts; use your normal GitHub authentication.

## Manual use in any capable agent

```sh
git clone https://github.com/italixcs/Repo-cleaner.git
cd Repo-cleaner
```

Ask: “Read `skills/repo-cleaner/SKILL.md` and its referenced resources, then audit the presentation of my repository.” Copying just SKILL.md loses its supporting resources. Manual use does not establish automatic host discovery.

## Codex — documented installation route

From the cloned repository, install the complete folder for your user:

```sh
test ! -e "$HOME/.agents/skills/repo-cleaner" &&
  mkdir -p "$HOME/.agents/skills" &&
  cp -R skills/repo-cleaner "$HOME/.agents/skills/repo-cleaner"
```

The first check prevents overwriting an existing installation. If it exists, use the update instructions below. Open a new session in your target project, check that the skill is listed, and invoke:

```text
$repo-cleaner Audit this repository's presentation before making changes.
```

For a project-scoped installation, copy the folder to `.agents/skills/repo-cleaner/` in the target project instead. Codex discovers repository skills through `.agents/skills` and user skills through `~/.agents/skills` in the [official skill guide](https://developers.openai.com/codex/skills).

## Claude Code — documented installation route

From the cloned repository:

```sh
test ! -e "$HOME/.claude/skills/repo-cleaner" &&
  mkdir -p "$HOME/.claude/skills" &&
  cp -R skills/repo-cleaner "$HOME/.claude/skills/repo-cleaner"
```

Open a local Claude Code session in the target project and invoke:

```text
/repo-cleaner Audit this repository's presentation before making changes.
```

For project scope, use `.claude/skills/repo-cleaner/` in the target project. This is a local Claude Code route; cloud/Cowork sessions have different loading rules. See the [official skills guide](https://code.claude.com/docs/en/skills).

## Windows PowerShell

After cloning, run this from `Repo-cleaner`. This example chooses the Codex user location; for local Claude Code, change `.agents` to `.claude` in the first line.

```powershell
$skillParent = Join-Path $HOME '.agents/skills'
$skillTarget = Join-Path $skillParent 'repo-cleaner'
if (Test-Path $skillTarget) { throw 'Repo Cleaner is already installed; review the update guide.' }
New-Item -ItemType Directory -Force -Path $skillParent | Out-Null
Copy-Item -Recurse -Path './skills/repo-cleaner' -Destination $skillTarget
```

The commands have been reviewed, not executed in Windows or either agent host.

## Compatibility status

| Host or method | Status | Evidence |
| --- | --- | --- |
| Codex local skill discovery | Documented route | Official location and invocation checked on 2026-11-10; folder-copy smoke check performed; no host runtime session exercised |
| Claude Code local skill discovery | Documented route | Official location and invocation checked on 2026-11-10; folder-copy smoke check performed; no host runtime session exercised |
| Other file-reading agents | Manual use | Read the complete package; native discovery and host behavior unverified |

No marketplace registration, native plugin package, or automatic support for other hosts is claimed. Add a new host only with a concrete installation route and recorded evidence.

## Update or remove

1. In your clone, run `git pull --ff-only` and read [CHANGELOG.md](../CHANGELOG.md).
2. Compare the installed folder with `skills/repo-cleaner/`. Preserve any local edits.
3. Move the installed `repo-cleaner` folder to a backup location outside the host's scanned skills directory, then copy in the complete new folder using the relevant route above.
4. Open a new session and check discovery again.

To remove the skill, remove only its installed `repo-cleaner` folder from the host's skills location. This does not delete repository presentation changes you previously made.

## Troubleshooting

- **Clone denied:** the repo is private; check that your authenticated account has access.
- **Skill absent:** check `repo-cleaner/SKILL.md`, exact host location, workspace trust/settings, and a fresh session. Do not put the repository root where the skill folder belongs.
- **Resources missing:** copy the entire package, including `references/`, `assets/`, and `agents/`.
- **Cannot change topics:** use the prepared values in [GitHub settings](github-settings.md); a text file cannot apply them.
- **No image tool:** reuse owned artwork or create exact vector assets. Capture actual output for screenshots; do not call a placeholder a verified demo.
