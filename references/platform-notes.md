# Platform notes

Fusion Intelligence is a plain Agent Skill (`SKILL.md` + `references/`), so it runs anywhere the open
Agent Skills layout is read. Behavioural differences are only in *where it is installed*, *how it is
invoked*, and *whether parallel agents exist*.

## Install locations

| Platform | User-level (all projects) | Project-level | Explicit invocation |
|---|---|---|---|
| **Claude Code** | `~/.claude/skills/fusion-intelligence/` | `<project>/.claude/skills/fusion-intelligence/` | `/fusion-intelligence` or just describe the task |
| **Codex** (CLI / IDE / app) | `~/.agents/skills/fusion-intelligence/` | `<project>/.agents/skills/fusion-intelligence/` | `$fusion-intelligence` or `/skills` |
| **Antigravity** | `~/.gemini/antigravity/skills/fusion-intelligence/` | `<project>/.agent/skills/fusion-intelligence/` | describe the task; the agent matches the skill description |
| Other agents (Gemini CLI, Cursor, Copilot CLI, Aider …) | per their docs | per their docs | put `AGENTS.md` at the project root as a fallback |

Run `scripts/install.sh` to place the files; run it with `--project <dir>` for project-level installs.
Codex's older location `~/.codex/skills/` is also supported by the installer when that folder exists.
Antigravity paths are community-documented; if your build reads another folder, copy the same directory there.

Restart the agent (or open a new session) after installing so the skill list refreshes.

## Parallelism

| Capability | Do |
|---|---|
| Subagent tool available (Claude Code `Agent`, Codex subagents, Antigravity Manager agents) | In `deep`/`pantheon`, launch lens passes in one batch; pass only brief + ledger + card |
| No subagents | Run lens passes inline, sequentially, under separate headings; never edit a finished pass |
| User did not ask for agents and mode is `quick`/`standard` | Inline is fine and cheaper |

**Cost guard:** `deep` ≈ 10–16 passes + audit; `pantheon` ≈ 80 short passes in 4 batches. Warn once, then proceed.

## Tool use

- Literature/evidence: use any connected PubMed/literature/search tool; otherwise ask the user for papers.
- Files: read the user's draft/protocol first; write reports to `fusion-report-<slug>.md` only if asked or if
  the report exceeds a few screens.
- Do not execute code or modify the user's files as part of a panel run unless asked; this skill is
  deliberative.

## Trigger tuning

The `description` in `SKILL.md` is the router. If the skill fires too often, remove the Chinese trigger words
or the "whenever the user asks for…" clause; if too rarely, add the user's own phrasing. In Codex you can set
`policy.allow_implicit_invocation: false` in `agents/openai.yaml` to require `$fusion-intelligence`.

## AGENTS.md fallback

For agents that do not load skills, copy `AGENTS.md` to the project root. It contains the compact workflow and
points at the same `references/` files (copy them next to it, e.g. to `docs/fusion/`, and adjust paths).

## Compatibility checklist

- [x] Frontmatter has only `name` and `description` (portable across Claude Code, Codex, Antigravity)
- [x] `name` is lowercase-hyphen, ≤ 64 chars; `description` ≤ 1024 chars, no angle brackets
- [x] No platform-specific tool names required; subagents are optional
- [x] All paths inside the skill are relative
- [x] No scripts are executed by the skill itself
