# Research checklists

Compact aids the lenses can lean on. **Always confirm the current version of any guideline** (several have
2024–2025 updates) and defer to the journal's or funder's instructions.

## 1. Which reporting guideline?

| Study type | Guideline(s) |
|---|---|
| Randomized trial | CONSORT (2010; 2025 update); protocol: SPIRIT |
| Observational (cohort, case-control, cross-sectional) | STROBE; routinely collected data: RECORD |
| Observational study emulating a target trial | TARGET (check current), plus STROBE/RECORD |
| Systematic review / meta-analysis | PRISMA 2020 (protocol: PRISMA-P) |
| Diagnostic accuracy | STARD |
| Prediction model (development/validation) | TRIPOD+AI; risk of bias: PROBAST (and PROBAST+AI) |
| Prediction/LLM studies | TRIPOD-LLM (check current) |
| AI interventions | CONSORT-AI, SPIRIT-AI, DECIDE-AI (early live evaluation) |
| Qualitative | COREQ, SRQR |
| Mixed methods | GRAMMS |
| Quality improvement | SQUIRE |
| Implementation studies | StaRI |
| Intervention description | TIDieR |
| Economic evaluation | CHEERS |
| Online survey | CHERRIES |
| Measurement instruments (development/validation) | COSMIN (selection and reporting) |
| Complex interventions | MRC/NIHR framework for developing and evaluating complex interventions |

## 2. Causal-claim checklist (Pearl · Hume · Bradford Hill · Buring)

1. State the **estimand**: population, exposure/intervention, comparator, outcome, time horizon, summary measure.
2. Which rung — association, intervention, counterfactual? Does the design reach it?
3. Draw the DAG: confounders, mediators, colliders, selection. What is unmeasured?
4. **Temporality** and **immortal-time / time-varying** problems.
5. Measurement error in exposure, outcome, confounders.
6. Bradford Hill viewpoints: strength, consistency, temporality, gradient, plausibility, coherence, experiment, analogy.
7. Rival explanations: reverse causation, confounding by indication, healthy-user, selection, regression to mean.
8. Triangulation: different designs with different biases (e.g., sibling, negative control, IV/MR, RCT).
9. Would an RCT be feasible/ethical? If not, what is the best emulation?
10. Sensitivity: E-value or equivalent; negative-control outcomes/exposures.

## 3. Buring-style 12-question critique (for any trial or cohort paper)

1. Rationale and specific knowledge gap · 2. Participants and sample size · 3. Exposure/intervention definition ·
4. Assignment (randomization, concealment) · 5. Outcome measurement reliability · 6. Main result ·
7. Role of chance · 8. Effect modification · 9. Generalizability · 10. Ethics · 11. Alternative designs ·
12. Finality — is the question answered?

## 4. Measurement-scale checklist (COSMIN-style order)

1. Construct definition and boundaries; target population and context of use.
2. **Content validity first**: relevance, comprehensiveness, comprehensibility (expert panel + target-population
   cognitive interviews).
3. Translation/adaptation: independent forward translations, reconciliation, back-translation, expert review,
   pre-test.
4. Structural validity: factor analysis with adequate sample; separate samples for EFA and CFA; report fit and
   loadings; sample size relative to number of items.
5. Measurement invariance across relevant groups (e.g., profession, setting, language).
6. Internal consistency per unidimensional subscale (do not report alpha without structural validity).
7. Reliability (test–retest, ICC) and measurement error (SEM, smallest detectable change).
8. Construct validity via a priori hypotheses (direction and magnitude); known-groups; convergent/discriminant.
9. Criterion validity only if a defensible gold standard exists.
10. Interpretability: score distribution, floor/ceiling, minimal important change, norms.
11. Responsiveness (if used for change).
12. Report with COSMIN-aligned reporting; share the instrument and scoring.

## 5. Prediction-model checklist (Kessler · Colditz · Goodfellow · Abbeel)

1. Intended use, user, moment of prediction, action triggered.
2. Predictors available at prediction time; no leakage.
3. Sample size justified for number of candidate parameters and events.
4. Missing data handling; avoid complete-case by default.
5. Shrinkage/regularization; avoid data-driven dichotomization.
6. Internal validation (bootstrap/CV) incl. all modeling steps.
7. **Calibration** (plot, slope, intercept) before discrimination; clinical utility (decision curve).
8. External/temporal/geographic validation; subgroup performance and fairness.
9. Do not interpret predictor coefficients causally.
10. Deployment: workflow integration, alert fatigue, monitoring for drift, update policy, human override.

## 6. Qualitative and mixed-methods checks

Stance and reflexivity · sampling logic and information power/saturation · audit trail from data to theme ·
negative case analysis · credibility (triangulation, member checks) · transferability statement ·
integration point(s) and joint display for mixed methods.

## 7. Ethics and governance prompts (verify local rules)

Ethics-committee approval and scope · informed consent and withdrawal · vulnerable participants · risk
minimization · privacy and de-identification · data storage/transfer/retention · data-sharing plan ·
secondary-use permission · trial registration · conflicts of interest · authorship and AI-use disclosure ·
local law (e.g., personal-information and data-security legislation, human-genetic-resource rules where
applicable).

## 8. Grant proposal sanity checks

- A reader can state the **question, the gap and the hypothesis** in 3 sentences.
- Each aim has a **decision-grade endpoint** and fails/succeeds visibly.
- Aims are independent enough that failure of one does not sink the project.
- Preliminary data show **feasibility of the riskiest step**, not just the easy one.
- Sample size/precision has an explicit rationale; recruitment feasibility is evidenced.
- Timeline vs staffing and equipment is consistent; budget lines map to aims.
- Innovation is stated as *what is new relative to specific prior work*.
- Risks have contingencies; ethics and data governance are concrete.
