# Fusion Intelligence — agent instructions

Applies when the user asks for several expert perspectives, a panel/council, a stress-test, a pre-review, a
"Reviewer 2" pass, or a decision under uncertainty about research (design, grant, manuscript, measurement,
prediction model, AI use, ethics, direction). 中文触发：多视角、专家会诊、圆桌、融合分析、课题预审、压力测试。
For lookups, arithmetic or routine coding, ignore this file.

Full skill: `SKILL.md` and `references/` (read them when present). Compact version below.

## Rules
1. Lenses are frameworks, not people: never speak as or invent quotes for a real person; write "after Pearl".
2. Evidence before opinion: never invent citations or numbers; tag claims `[E#]` evidence · `[R]` reasoning ·
   `[A]` assumption.
3. Headcount is not evidence: lenses share one model. Consensus needs independent evidence and a surviving
   red-team attack.
4. Write each lens independently; preserve dissent; always include a red-team lens.
5. Not medical/legal/financial advice; no identifiable participant data. Reply in the user's language.

## Procedure
1. **Brief** (≤ 8 lines): question · decision it feeds · type · stakes · constraints · user's prior · deliverable.
2. **Mode:** `quick` 4 lenses · `standard` 6–8 · `deep` 10–16 + cross-exam · `pantheon` all 80 in batches.
3. **Panel:** ≥ 1 methodologist, ≥ 1 domain, ≥ 1 red team, ≥ 1 outside lens, ≥ 1 implementation realist.
   Pick from `references/lens-library.md`; presets in `references/panel-presets.md`
   (idea-stress-test, study-design, causal-claim-check, grant-prescreen, manuscript-reviewer2,
   measurement-scale, clinical-prediction-model, real-world-database, intervention-implementation,
   ai-in-research, research-ethics, direction-selection, discrepant-results, qualitative-mixed-methods,
   public-health-policy, translation-commercial, general-8).
4. **Ground:** evidence ledger E1…En (claim · source · design/N · strength A–D) and gaps G1…Gn.
5. **Lens passes:** position · ≤ 3 tagged claims · what it sees that others miss · strongest objection to itself ·
   decisive test · confidence · one action. Parallel agents only for `deep`/`pantheon` or on request.
6. **Fuse:** claim × lens matrix → Consensus / Contested / Single-lens hypothesis / Blind spot / Echo;
   type each divergence (Factual, Methodological, Values, Definitional, Scope, Time) and say what resolves it;
   calibrate confidence (never High on lens agreement alone); no-regret vs conditional moves; falsifiers.
7. **Deliver:** bottom line first → agree → split (with crux) → blind spots → path → what would change this →
   next steps → ledger. Offer ≤ 3 follow-ups.

## Limits
A panel of model-generated lenses structures thinking; it adds no independent expertise or data. Say so.
