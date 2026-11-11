# Security scan

On 2026-11-11, the maintainer ran [NVIDIA SkillSpector](https://github.com/NVIDIA/SkillSpector) 2.12.0 against the complete `skills/repo-cleaner/` package at [commit a6c41a0](https://github.com/italixcs/Repo-cleaner/commit/a6c41a0a2b813fe7b41ad232e3232ec9948c11b2).

| Result | Reported value |
| --- | --- |
| Active findings | 0 |
| Suppressed findings | 0 |
| Risk score | 0/100, LOW |
| Scanner recommendation | SAFE |
| Configured scan coverage | 7/7 files, complete |
| Mode | Static analysis; LLM analysis disabled |
| Caller exclusions / baseline | None / none |
| Exit code | 0 with failure-on-findings and failure-on-incomplete enabled |

[Unmodified JSON report](skillspector-v0.2.1.json) · [Run metadata and SHA-256 hashes](scan-record-v0.2.1.json)

Previous scan: [0.2.0 report](skillspector-2026-11-11.json) · [previous run record](scan-record.json).

## Scope and limits

The result means SkillSpector found no matching issues in this revision under its configured static checks. Its 100% coverage value describes file inspection for that configuration, not coverage of every possible security risk. The report lists which analyzers completed, were disabled, or did not apply. The package contains seven Markdown/YAML files and no executable scripts according to the scanner.

LLM semantic analysis was disabled with `--no-llm`; no model inference was performed. This run did not execute the skill in an agent host, test every possible tool action, follow transitive external resources, or scan the whole repository and its development environment. The installable package contains no dependency manifest; dependency-artifact inspection was not requested. Future revisions and the agent host's permissions require their own review.

This is a maintainer-run result from NVIDIA's open-source tool, not an independent audit, NVIDIA endorsement, catalog verification, signing, or certification. A clean scan does not prove that a skill is harmless.

## Reproduce

Requires Python 3.12+ and uv. The scanner's pinned lockfile is used to reproduce its dependency set. From an empty working directory:

```sh
git clone https://github.com/NVIDIA/SkillSpector.git skillspector-source
git -C skillspector-source checkout 86d46b1721f029819020df396e8fa1c96eb83236
git clone https://github.com/italixcs/Repo-cleaner.git repo-cleaner
git -C repo-cleaner checkout a6c41a0a2b813fe7b41ad232e3232ec9948c11b2
cd skillspector-source
uv sync --frozen --no-dev
LANGSMITH_TRACING=false LANGCHAIN_TRACING_V2=false \
  .venv/bin/skillspector scan ../repo-cleaner/skills/repo-cleaner \
  --no-llm --fail-on-incomplete --fail-on-findings \
  --format json --output ../skillspector.json
```

Reports contain a local source path and timestamp, so their raw file hashes will vary across machines. Compare package hashes, scanner revision, findings, and analysis-completeness fields. No suppression baseline or file exclusions were used. The original JSON is preserved as emitted, including its original local source path and configured model labels; those labels do not indicate model execution (`llm_requested` and `llm_available` are both false).
