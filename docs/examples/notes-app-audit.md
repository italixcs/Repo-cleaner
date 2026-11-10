# Notes-app audit example

This is a condensed presentation of an actual audit-only smoke check from 2026-11-10. The repository was a synthetic local fixture, not an external user's project. The agent received the README, package manifest, and recorded repository state; it did not run the app or access external services.

## Request

```text
Audit this repository's presentation. Return prioritized findings,
a proposed README outline, and recommended GitHub settings.
Do not change files or settings.
```

## Available evidence

- The README instructed users to run `npm install` and `npm run start`.
- The manifest defined `dev: vite` and `build: vite build`, with no `start` script.
- The README included static badges claiming full coverage and support for all agents.
- The recorded inventory described a plain JavaScript/localStorage notes app, without tests, CI, or AI integration.
- Topics were `react`, `ai`, `chatgpt`, and `notes`; visibility was private; the social preview was unknown.

## Condensed output

| Priority | Finding | Recommendation |
| --- | --- | --- |
| P0 | `npm run start` has no matching script. | Document `npm run dev`; verify it in a full checkout before claiming it works. |
| P0 | Coverage and universal-agent badges lack evidence. | Remove those badges. |
| P0 | Framework and AI topics conflict with the observed project. | Keep relevant notes topics; propose JavaScript, localStorage, and Vite topics. |
| P1 | The description and demo do not show what users can do. | Explain browser-local notes and capture the actual app when available. |

Settings were **prepared only**. The agent retained private visibility, kept unknown settings unknown, and changed no files or settings. This demonstrates an audit response; it does not establish native Codex/Claude Code discovery or behavior on every project.
