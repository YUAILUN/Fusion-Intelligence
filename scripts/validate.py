#!/usr/bin/env python3
"""Validate the Fusion Intelligence skill package.

Checks:
  * SKILL.md frontmatter (name, description limits, portable fields only)
  * every relative file path mentioned in SKILL.md / AGENTS.md exists
  * lens library: 80 upstream lenses + 7 role lenses, unique ids
  * every lens id used in panel-presets.md exists in the library; panel sizes are sane
  * relative markdown links resolve
  * no machine-specific absolute paths

Usage:  python3 scripts/validate.py
Exit code is non-zero on any error.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
errors: list[str] = []
warnings: list[str] = []


def err(msg: str) -> None:
    errors.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def read(rel: str) -> str:
    p = ROOT / rel
    if not p.is_file():
        err(f"missing file: {rel}")
        return ""
    return p.read_text(encoding="utf-8")


# ---------------------------------------------------------------- frontmatter
skill = read("SKILL.md")
m = re.match(r"---\n(.*?)\n---\n", skill, re.S)
if not m:
    err("SKILL.md: no YAML frontmatter")
else:
    fm = m.group(1)
    name_m = re.search(r"^name:\s*(\S+)\s*$", fm, re.M)
    if not name_m:
        err("SKILL.md: missing name")
    else:
        name = name_m.group(1)
        if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name) or len(name) > 64:
            err(f"SKILL.md: invalid name {name!r}")
    desc_m = re.search(r"^description:\s*(>-?|\|-?)?\s*\n((?:[ \t]+.*\n?)+)", fm + "\n", re.M)
    if not desc_m:
        err("SKILL.md: missing description")
    else:
        desc = " ".join(line.strip() for line in desc_m.group(2).splitlines()).strip()
        if len(desc) > 1024:
            err(f"SKILL.md: description is {len(desc)} chars (> 1024)")
        if "<" in desc or ">" in desc:
            err("SKILL.md: description must not contain angle brackets")
        if len(desc) < 80:
            warn("SKILL.md: description is very short; routing may suffer")
    extra = [k for k in re.findall(r"^([A-Za-z_-]+):", fm, re.M) if k not in ("name", "description")]
    if extra:
        warn(f"SKILL.md: non-portable frontmatter keys {sorted(set(extra))}")

# ------------------------------------------------------------ referenced paths
for doc in ("SKILL.md", "AGENTS.md", "README.md", "README.zh-CN.md"):
    text = read(doc)
    for rel in set(re.findall(r"`((?:references|examples|scripts|agents)/[A-Za-z0-9_.\-/]+)`", text)):
        if rel.endswith("/"):
            if not (ROOT / rel).is_dir():
                err(f"{doc}: directory not found: {rel}")
        elif not (ROOT / rel).exists():
            err(f"{doc}: file not found: {rel}")

# ------------------------------------------------------------------ lens ids
lib = read("references/lens-library.md")
ids = re.findall(r"^\|\s*`([A-Za-z0-9][A-Za-z0-9-]*)`\s*\|", lib, re.M)
dups = {i for i in ids if ids.count(i) > 1}
if dups:
    err(f"lens-library: duplicate ids {sorted(dups)}")
role = [i for i in ids if re.fullmatch(r"R\d-.+", i, re.I)]
upstream = [i for i in ids if i not in role]
if len(upstream) != 80:
    err(f"lens-library: expected 80 upstream lenses, found {len(upstream)}")
if len(role) != 7:
    err(f"lens-library: expected 7 role lenses, found {len(role)}")
known = set(ids)

# ------------------------------------------------------------------ presets
presets = read("references/panel-presets.md")
blocks = re.split(r"^## ", presets, flags=re.M)[1:]
preset_names = []
for b in blocks:
    head = b.splitlines()[0]
    pm = re.match(r"`([a-z0-9-]+)`", head)
    if not pm:
        continue
    pname = pm.group(1)
    preset_names.append(pname)
    pm2 = re.search(r"\*\*Panel \((\d+)\):\*\*\s*(.+)", b)
    if not pm2:
        err(f"panel-presets: {pname} has no Panel line")
        continue
    declared = int(pm2.group(1))
    used = re.findall(r"`([A-Za-z0-9][A-Za-z0-9-]*)`", pm2.group(2))
    if len(used) != declared:
        err(f"panel-presets: {pname} declares {declared} lenses but lists {len(used)}")
    for u in used:
        if u not in known:
            err(f"panel-presets: {pname} uses unknown lens id {u}")
    if "R2-red-team" not in used and pname != "general-8":
        err(f"panel-presets: {pname} has no red-team lens (R2)")
    if pname == "general-8" and "R2-red-team" not in used:
        err("panel-presets: general-8 must include the red-team lens")

# the router table in SKILL.md must only use known presets
for p in set(re.findall(r"\|\s*`([a-z0-9-]+)`\s*\|\s*$", skill, re.M)):
    if p not in preset_names:
        err(f"SKILL.md router: preset {p!r} not defined in panel-presets.md")

# quick-mode table ids
qm = presets.split("## Quick-mode reductions", 1)
if len(qm) == 2:
    for u in set(re.findall(r"`([A-Za-z0-9][A-Za-z0-9-]*)`", qm[1])):
        if u not in known:
            err(f"panel-presets quick table: unknown lens id {u}")

# ---------------------------------------------------------- markdown links
for path in ROOT.rglob("*.md"):
    if ".git" in path.parts:
        continue
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", text):
        if re.match(r"[a-z]+:", target):
            continue
        if not (path.parent / target).exists():
            err(f"{path.relative_to(ROOT)}: broken link {target}")

# ------------------------------------------------------------ hygiene
for path in ROOT.rglob("*"):
    if path.is_dir() or ".git" in path.parts or path.suffix not in (".md", ".sh", ".py", ".yaml", ".yml"):
        continue
    if path.name == "validate.py":
        continue
    text = path.read_text(encoding="utf-8")
    if re.search(r"/Users/[A-Za-z0-9_.-]+/", text):
        err(f"{path.relative_to(ROOT)}: contains a machine-specific absolute path")

# ------------------------------------------------------------------ report
for w in warnings:
    print("WARN ", w)
for e in errors:
    print("ERROR", e)
print(
    f"\n{len(upstream)} upstream lenses, {len(role)} role lenses, "
    f"{len(preset_names)} presets, {len(errors)} error(s), {len(warnings)} warning(s)"
)
sys.exit(1 if errors else 0)
