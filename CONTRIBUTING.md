# Contributing

Improve a reader's path from discovery to first useful result. Propose an instruction change with the concrete repository or task it helps. Use synthetic or public examples; do not include private source, credentials, signed URLs, or personal screenshots.

## Structure

- `skills/repo-cleaner/`: installable workflow and its supporting resources.
- `docs/`: human-facing installation, usage, discovery, and showcases.
- `docs/assets/`: presentation images, exact vector badges, and provenance.
- `tests/`: package and documentation integrity checks.

Keep public marketing docs outside the skill package. Avoid application-code changes, speculative integrations, and filler docs.

## Verify a change

```sh
python3 -m unittest discover -s tests -v
```

Review links, assets, and claims; inspect changed layouts in light/dark and desktop/mobile views. A local renderer approximates GitHub and must be described that way. If changing installation guidance, check the host's current official documentation and record whether the route was actually exercised inside the host.

For behavioral changes, try a realistic prompt on a fixture and record what happened. Do not report a scenario as passed merely because the instructions mention it. Update screenshots and their source descriptions when visible content changes.

Use a focused pull request explaining the reader-facing problem, change, and verification. Report bugs through [Issues](https://github.com/italixcs/Repo-cleaner/issues), including the prompt, expected result, and a sanitized example.
