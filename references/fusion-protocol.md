# Fusion protocol (Step 6)

"Fusion" means *integrating by structure*, not concatenating or averaging. The output is a map of the
question: what is settled, what is contested and why, what is missing, and what to do under each reading.

## 1. Extract and normalize claims

From every lens pass (and cross-examination), pull **atomic claims** — one proposition each — and merge
paraphrases. Give them ids `K1…Kn`. Keep the evidence tags (`[E#]`, `[R]`, `[A]`).

## 2. Build the support matrix

|  | `lens-a` | `lens-b` | `lens-c` | … | families that support | evidence |
|---|---|---|---|---|---|---|
| K1 | + | + | – | | A, C | E2, E5 |
| K2 | + | 0 | 0 | | A | [R] |

`+` supports · `–` opposes · `0` silent. A lens that is silent has *not* agreed.

## 3. Classify

| Class | Rule | Treatment |
|---|---|---|
| **Consensus** | supported by ≥ 2 independent families **and** no evidence-backed objection | state as the working conclusion; list the evidence |
| **Contested** | credible opposition from ≥ 1 lens with reasons | go to §4 |
| **Single-lens hypothesis** | one lens/family only | flag as hypothesis; say what test would promote it |
| **Blind spot** | needed for the decision, addressed by no lens | name it; assign a lens or a data need |
| **Echo** | supported only by lenses sharing the same premise | discount; do not count as independent |

*Independent families* means lenses whose reasoning does not depend on the same premise or the same single
source. Two epidemiology lenses citing the same cohort are one voice.

## 4. Diagnose each divergence (crux typing)

| Crux | Signature | What resolves it |
|---|---|---|
| **Factual (F)** | disagree on what is the case | a specific datum, analysis or experiment — name it |
| **Methodological (M)** | disagree on what counts as proof | agree a pre-specified standard (e.g., design, estimand, threshold) |
| **Values / priorities (V)** | same facts, different weight on outcomes | make the trade-off explicit; ask the decision-owner |
| **Definitional (D)** | same word, different meaning | fix the definition; re-ask the question |
| **Scope / population (S)** | both right in different settings | state the boundary conditions of each claim |
| **Time horizon (T)** | short-term vs long-term | state both and the discount implied |

Write each as: *claim · camp A (lenses, reason) vs camp B (lenses, reason) · crux type · what resolves it.*
If you cannot type a divergence, you have not understood it — re-read the passes.

## 5. Calibrate confidence

| Level | Requirements |
|---|---|
| **High** | ≥ 2 independent evidence sources of strength A/B, ≥ 3 families converge, red-team found no surviving evidence-backed rival |
| **Moderate** | evidence of strength B/C *or* families converge but a methodological caveat is open |
| **Low** | rests on reasoning/assumptions or a single weak source; credible rival remains |
| **Unknown** | decisive information missing — state exactly which |

Rules: never "High" on lens agreement alone · lower one level if the red-team objection is unanswered · lower
one level if the conclusion depends on an unverified assumption `[A]` · say confidence **per claim**, then overall.

## 6. Derive the recommendation

- **No-regret moves:** actions that are good under every credible reading (cheap, reversible, informative).
- **Conditional moves:** `If crux K# resolves to X → do Y; if it resolves to Z → do W.`
- **Decisive next test:** the single cheapest analysis/experiment/expert conversation that would collapse the
  largest uncertainty. Name it, estimate effort, say which crux it resolves.

## 7. Falsifiers ("What would change this conclusion")

For the top 3 conclusions: the observation, result or constraint that would flip them. If you cannot write a
falsifier, the conclusion is not yet a finding — downgrade it.

## 8. Anti-patterns (do not do)

| Anti-pattern | Why it fails | Instead |
|---|---|---|
| Averaging positions | produces a bland answer nobody holds | keep the split; type the crux |
| Majority = truth | same-model lenses correlate | weigh by independent evidence |
| False balance | gives a weak rival equal weight | grade by evidence strength |
| Laundering speculation | an `[A]` becomes "consensus" by repetition | keep tags through to the report |
| Burying dissent | the best objection disappears | keep the strongest minority argument |
| Over-precision | numbers without a basis | give ranges, or none |
| Citation theatre | refs that do not support the claim | R1 audit; drop or flag |

## 9. Consensus quality score (optional, for `deep`)

Report four numbers (0–3) so the reader can see how much to trust the map:
**Evidence depth** (E strength) · **Family diversity** (independent families) · **Adversarial pressure**
(did the red team and cross-exam bite?) · **Coverage** (blind spots closed). Sum ≥ 9 = robust; 6–8 = usable;
≤ 5 = provisional.
