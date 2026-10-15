# Report templates (Step 7)

Pick one. Keep the bottom line first. Match language to the user; the Chinese headings below are provided
for Chinese-language reports. Length must fit the mode.

---

## T1 — Full Fusion Report (`standard` / `deep`)

```markdown
# Fusion Report — <topic>
**Mode:** standard | deep · **Date:** <YYYY-MM-DD> · **Panel:** <n> lenses, <k> families

## Bottom line
<≤ 5 lines: the answer, the main reason, the main caveat>
**Confidence:** High | Moderate | Low | Unknown — <why>

## 1. Question brief & assumptions
<question · decision it feeds · type · constraints · assumptions A1…>

## 2. Panel
| Lens | Why it is here |
|---|---|

## 3. Where the panel agrees
| # | Claim | Evidence | Families converging | Confidence |
|---|---|---|---|---|

## 4. Where it splits
| # | Claim | Camp A (reason) | Camp B (reason) | Crux type | What resolves it |
|---|---|---|---|---|---|

## 5. Blind spots & missing evidence
- <G1 …>

## 6. Recommended path
**No-regret moves**
1. …
**Conditional moves**
- If <crux K#> resolves to X → …

## 7. What would change this conclusion
- <falsifier 1> …

## 8. Next steps
| # | Action | Owner | Effort | Resolves |
|---|---|---|---|---|

## 9. Evidence ledger
| ID | Claim | Source | Design & N | Strength | Verified |
|---|---|---|---|---|---|

## Appendix A — Per-lens positions
<one short block per lens>

## Appendix B — Method note
Mode · panel · tools used · retrieval date · limits (e.g., Chinese databases not searched) ·
"Generated with AI-assisted multi-lens reasoning; claims tagged E/R/A; verify before use."
```

### 中文版（完整融合报告）
```markdown
# 融合智能报告 — <主题>
**模式：** 标准 | 深度 · **日期：** · **面板：** <n> 个视角 / <k> 个学科族

## 结论先行
<≤5 行：答案、主要理由、主要保留意见>
**置信度：** 高 | 中 | 低 | 未知 — <原因>

## 一、问题简述与前提假设
## 二、评议面板（视角—入选理由）
## 三、一致之处（主张｜证据｜收敛的学科族｜置信度）
## 四、分歧所在（主张｜甲方理由｜乙方理由｜分歧类型｜如何裁决）
## 五、盲点与缺失证据
## 六、建议路径（无悔行动｜条件行动）
## 七、什么会改变这个结论（证伪条件）
## 八、下一步（行动｜负责人｜工作量｜解决的分歧）
## 九、证据清单（ID｜主张｜来源｜设计与样本量｜强度｜是否核实）
## 附录 A　各视角立场　　附录 B　方法说明
```

---

## T2 — One-page brief (`quick`)

```markdown
**Fusion brief — <topic>** · quick · <date>
**Answer:** <2–3 sentences>  **Confidence:** <level> — <why>
**Panel:** <4 lenses>
**Agree:** • … • …
**Split:** • <claim>: A vs B — crux <type> — resolve by <test>
**Do now:** 1) … 2) … 3) …
**Would change this:** …
**Not checked:** <what was not retrieved/verified>
```

---

## T3 — Grant pre-review scorecard (`grant-prescreen`)

```markdown
# Pre-review — <project title> · <funder/program if given>
**Overall:** <fundable as is | fundable with revisions | major rework> · Confidence: <level>
| Criterion | Score 1–5 | Evidence in text | Fix |
|---|---|---|---|
| Significance & knowledge gap | | | |
| Hypothesis / aims clarity | | | |
| Innovation (new vs incremental) | | | |
| Approach rigor (design, measures, analysis) | | | |
| Feasibility & preliminary data | | | |
| Team / platform fit | | | |
| Risks & contingency | | | |
| Outputs & translation | | | |
| Ethics, data governance, budget realism | | | |
**Top 3 reviewer attacks (and a one-line defense each)**
**Rewrite priorities (ordered):**
**Aim-level notes:** Aim 1 … Aim 2 …
```
If the funder's own criteria are supplied, use them as rows instead.

---

## T4 — Reviewer-2 report (`manuscript-reviewer2`)

```markdown
# Referee report — <title>
**Summary of the submission** (3–4 sentences, neutral)
**Overall assessment** (contribution · soundness · clarity)
**Major concerns**
1. <concern> — why it matters — what would address it (analysis/data/wording)
**Minor concerns**
**Reporting-guideline check:** <CONSORT/STROBE/…> — items missing: …
**Statistics and measurement:** …
**Claims vs evidence table**
| Claim in text | Supporting analysis | Verdict (supported / overstated / unsupported) |
**Recommendation:** accept | minor | major | reject — <one-line reason>
```

---

## T5 — Study-design memo (`study-design`, `measurement-scale`, `clinical-prediction-model`)

```markdown
# Design memo — <study>
**Estimand / target of inference:** population · exposure/intervention · comparator · outcome · timing · summary measure
**Recommended design:** … **Why not alternatives:** …
**Threats to validity → countermeasures**
| Threat | Likelihood × impact | Countermeasure |
**Measurement plan:** constructs → instruments → validity/reliability evidence needed
**Sample & precision:** assumptions · target N · sensitivity to assumptions
**Analysis plan skeleton:** primary · secondary · sensitivity · missing data
**Ethics & governance:** …
**Reporting guideline:** … **Pre-registration:** …
**Feasibility:** time · staff · cost · critical path
**Decision gates:** go / revise / stop criteria
```

---

## T6 — AI-use disclosure snippet (for methods/ethics sections)

> "A structured multi-perspective reasoning workflow (Fusion Intelligence, <date>) using <model/tool> was used
> to pressure-test the study design and identify weaknesses. All content was reviewed by the authors; no
> identifiable participant data were entered; the authors take full responsibility for the final text."

Adapt to the journal/funder policy; verify its required wording.
