#!/usr/bin/env bash
# Install the Fusion Intelligence skill for Claude Code, Codex and/or Antigravity.
#
#   scripts/install.sh                      # user-level, all three platforms
#   scripts/install.sh --claude --codex     # only those platforms
#   scripts/install.sh --project ~/myrepo   # project-level instead of user-level
#   scripts/install.sh --link               # symlink (stays up to date with git pull)
#   scripts/install.sh --uninstall          # remove what this script installed
#   scripts/install.sh --dry-run            # print actions only
set -euo pipefail

NAME="fusion-intelligence"
SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PAYLOAD=(SKILL.md references agents examples NOTICE.md LICENSE)

do_claude=0; do_codex=0; do_anti=0
project=""; link=0; uninstall=0; dry=0

usage() { sed -n '2,10p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; }

while [[ $# -gt 0 ]]; do
  case "$1" in
    --claude) do_claude=1 ;;
    --codex) do_codex=1 ;;
    --antigravity) do_anti=1 ;;
    --all) do_claude=1; do_codex=1; do_anti=1 ;;
    --project) project="${2:?--project needs a directory}"; shift ;;
    --link) link=1 ;;
    --uninstall) uninstall=1 ;;
    --dry-run) dry=1 ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage; exit 2 ;;
  esac
  shift
done

if (( do_claude + do_codex + do_anti == 0 )); then do_claude=1; do_codex=1; do_anti=1; fi

run() { if (( dry )); then echo "[dry-run] $*"; else eval "$@"; fi; }

targets=()
if [[ -n "$project" ]]; then
  project="$(cd "$project" && pwd)"
  (( do_claude )) && targets+=("$project/.claude/skills/$NAME")
  (( do_codex ))  && targets+=("$project/.agents/skills/$NAME")
  (( do_anti ))   && targets+=("$project/.agent/skills/$NAME")
else
  (( do_claude )) && targets+=("$HOME/.claude/skills/$NAME")
  (( do_codex ))  && targets+=("$HOME/.agents/skills/$NAME")
  (( do_codex )) && [[ -d "$HOME/.codex/skills" ]] && targets+=("$HOME/.codex/skills/$NAME")
  (( do_anti ))   && targets+=("$HOME/.gemini/antigravity/skills/$NAME")
fi

for dest in "${targets[@]}"; do
  if (( uninstall )); then
    if [[ -e "$dest" || -L "$dest" ]]; then
      run "rm -rf \"$dest\""; echo "removed  $dest"
    else
      echo "absent   $dest"
    fi
    continue
  fi

  run "mkdir -p \"$(dirname "$dest")\""
  run "rm -rf \"$dest\""
  if (( link )); then
    run "ln -s \"$SRC\" \"$dest\""
    echo "linked   $dest -> $SRC"
  else
    run "mkdir -p \"$dest\""
    for item in "${PAYLOAD[@]}"; do
      [[ -e "$SRC/$item" ]] && run "cp -R \"$SRC/$item\" \"$dest/\""
    done
    echo "installed $dest"
  fi
done

if (( ! uninstall )); then
  echo
  echo "Done. Restart your agent (or open a new session) so the skill list refreshes."
  echo "  Claude Code : /fusion-intelligence   (or just describe the task)"
  echo "  Codex       : \$fusion-intelligence   (or /skills)"
  echo "  Antigravity : describe the task; the skill description routes it"
fi
