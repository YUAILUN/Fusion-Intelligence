# Panel presets

Ready-made panels for common research tasks. Lens ids come from `lens-library.md`
(`R1`–`R7` are role lenses). Each preset lists a **core panel**, what the panel must **settle**, and
**checks** to run. Tune: swap in domain lenses, drop to 4 in `quick` mode, extend in `deep` mode.

Composition always satisfies the rules in `SKILL.md` §3 Step 2 (methodologist · domain · skeptic · outside ·
implementation).

---

## `idea-stress-test` — 研究想法压力测试
**Panel (8):** `socrates` · `david-hume` · `judea-pearl` · `julie-e-buring` · `eric-s-lander` · `warren-buffett` · `R2-red-team` · `R6-implementation-realist`
**Settle:** Is the question well-posed? What is the real knowledge gap? What would a decisive result look like?
**Checks:** definitions pinned (Wittgenstein-style) · causal or descriptive aim declared · smallest convincing
study · opportunity cost · who else is doing this · kill criteria.

## `study-design` — 研究设计
**Panel (9):** `julie-e-buring` · `judea-pearl` · `meir-j-stampfer` · `terrie-e-moffitt` · `ronald-c-kessler` · `R4-statistics-measurement` · `R5-ethics-integrity` · `R6-implementation-realist` · `R2-red-team`
**Settle:** Design fit to question · estimand · confounding strategy · measurement · sample/precision · feasibility.
**Checks:** estimand and comparator explicit · DAG or equivalent · exposure/outcome measurement error ·
missing-data plan · sensitivity analyses · reporting guideline chosen (`research-checklists.md`).

## `causal-claim-check` — 因果主张审查
**Panel (8):** `judea-pearl` · `david-hume` · `meir-j-stampfer` · `julie-e-buring` · `dorret-i-boomsma` · `terrie-e-moffitt` · `R1-evidence-auditor` · `R2-red-team`
**Settle:** Is the claim causal, associational, or predictive? What assumptions carry it? Which alternative explanations survive?
**Checks:** ladder rung · confounding/colliders/mediators · temporality · dose-response · consistency across designs ·
family/sibling controls · negative controls · what an RCT would show.

## `grant-prescreen` — 基金/课题申报预审（国自然、学会课题、省部级等）
**Panel (9):** `eric-s-lander` · `robert-langer` · `julie-e-buring` · `aristotle` · `warren-buffett` · `R2-red-team` · `R3-pre-mortem` · `R6-implementation-realist` · `R7-patient-practitioner-voice`
**Settle:** Is the scientific question important and specific? Is the approach rigorous and feasible with this team and budget? What is genuinely new?
**Rubric (score 1–5 each, with reason):** significance & gap · hypothesis/aims clarity · innovation (what is new vs
incremental) · approach rigor · feasibility & preliminary data · team/platform fit · risk & contingency ·
outputs & translation · ethics, data governance & budget realism.
**Checks:** aims are independent but coherent · each aim has a decision-grade endpoint · Gantt vs staffing ·
rival explanations addressed · "so what" paragraph · rhetoric (ethos/pathos/logos) of the opening.
**Note:** apply the *funder's* published criteria if the user supplies them; they override the generic rubric.

## `manuscript-reviewer2` — 稿件审稿人视角
**Panel (8):** `christopher-manning` · `julie-e-buring` · `david-hume` · `ludwig-wittgenstein` · `R4-statistics-measurement` · `R1-evidence-auditor` · `R2-red-team` · `R5-ethics-integrity`
**Settle:** Do claims follow from data? What would a hostile-but-fair reviewer demand?
**Output:** Reviewer-2 report template (`report-templates.md`): summary → major concerns → minor → required
analyses/clarifications → recommendation. Check the matching reporting guideline line by line.

## `measurement-scale` — 量表研制/汉化与验证
**Panel (9):** `ludwig-wittgenstein` · `plato` · `confucius` · `terrie-e-moffitt` · `martha-nussbaum` · `fei-fei-li` · `R4-statistics-measurement` · `R7-patient-practitioner-voice` · `R2-red-team`
**Settle:** Is the construct defined and bounded? Is content validity secured before statistics? Does the instrument
work *across* groups and in the target language/culture?
**Checks (COSMIN-style order):** construct definition and scope · content validity (relevance, comprehensiveness,
comprehensibility; expert panel + target-population cognitive interviews) · translation and cultural adaptation
(forward/back, harmonization) · structural validity (EFA→CFA on separate samples; model fit) · measurement
invariance across relevant groups · internal consistency · reliability (test–retest) and measurement error ·
hypotheses-testing for construct validity · criterion validity if a gold standard exists · interpretability
(MIC/floor-ceiling) · sample size vs item count · reporting guideline.

## `clinical-prediction-model` — 临床预测模型/风险评分
**Panel (9):** `ronald-c-kessler` · `graham-a-colditz` · `judea-pearl` · `ian-goodfellow` · `R2-red-team` · `judy-faulkner` · `R4-statistics-measurement` · `R5-ethics-integrity` · `R6-implementation-realist`
**Settle:** Is the intended use clear? Is the model valid, calibrated and useful beyond development data? Is it fair and deployable?
**Checks:** intended use & decision · predictors available at prediction time (leakage) · sample size/events per
parameter · missing-data handling · overfitting and internal validation · calibration + discrimination + clinical
utility (decision curve) · external/temporal validation · subgroup performance and fairness · do not read
predictors causally · workflow, alert fatigue, monitoring and drift · TRIPOD+AI / PROBAST.

## `real-world-database` — 真实世界/围手术期数据库研究
**Panel (9):** `eric-s-lander` · `stacey-gabriel` · `julie-e-buring` · `meir-j-stampfer` · `judea-pearl` · `judy-faulkner` · `R5-ethics-integrity` · `R4-statistics-measurement` · `R2-red-team`
**Settle:** Is the database fit for *this* question? Which biases are structural? What governance applies?
**Checks:** data provenance and coding validity · target-trial emulation framing · immortal-time and
time-varying confounding · missingness mechanism · outcome ascertainment · linkage and privacy rules ·
future-proofing (variables, biobank, versioning) · RECORD/STROBE.

## `intervention-implementation` — 护理干预/复杂干预与落地
**Panel (9):** `julie-e-buring` · `ronald-c-kessler` · `tamara-b-harris` · `R2-red-team` · `martha-nussbaum` · `lynda-resnick` · `R6-implementation-realist` · `R7-patient-practitioner-voice` · `R3-pre-mortem`
**Settle:** Does the intervention have a plausible mechanism, a defensible comparator, and a path to routine use?
**Checks:** intervention description (TIDieR) · logic model and mechanism · comparator and contamination ·
heterogeneity of effect (who benefits) · fidelity and dose · process evaluation · outcome relevance to patients ·
cost and workload · sustainability (RE-AIM / CFIR) · MRC/NIHR complex-intervention framework.

## `ai-in-research` — AI/LLM 方法选型、可靠性与规范
**Panel (9):** `demis-hassabis` · `andrew-ng` · `andrej-karpathy` · `R2-red-team` · `stuart-russell` · `ian-goodfellow` · `fei-fei-li` · `R1-evidence-auditor` · `R5-ethics-integrity`
**Settle:** Is AI the right tool? How will we know it is reliable? Who is accountable?
**Checks:** task definition and gold standard · baseline (non-AI) comparison · hallucination/robustness tests ·
distribution shift · human-in-the-loop level (autonomy slider) · reproducibility (versions, prompts, seeds) ·
privacy and data residency · disclosure of AI use · reporting guideline (TRIPOD+AI / TRIPOD-LLM, CONSORT-AI, etc.).

## `research-ethics` — 研究伦理与诚信
**Panel (10):** `immanuel-kant` · `aristotle` · `elizabeth-anscombe` · `martha-nussbaum` · `hannah-arendt` · `confucius` · `iris-murdoch` · `judith-butler` · `R5-ethics-integrity` · `R2-red-team`
**Settle:** What is owed to participants, to colleagues, and to the public? Which principle conflicts, and how is it resolved?
**Checks:** respect for persons (consent, voluntariness) · beneficence/non-maleficence (risk minimization) ·
justice (selection, access, benefit-sharing) · vulnerable groups · data governance and re-identification risk ·
conflicts of interest · authorship and AI-use transparency · institutional and legal requirements (verify locally).
**Note:** frame as reasoning aid; the ethics committee decides.

## `direction-selection` — 选题与研究方向
**Panel (8):** `demis-hassabis` · `ilya-sutskever` · `robert-langer` · `eric-s-lander` · `daphne-koller` · `fei-fei-li` · `warren-buffett` · `R2-red-team`
**Settle:** Which problem is important, tractable *for us*, and defensible against competition?
**Checks:** importance × tractability × comparative advantage · "root-node" potential · staged payoffs ·
data/resource access · timing · 3 kill criteria · what you will stop doing.

## `discrepant-results` — 矛盾证据与结果解读
**Panel (9):** `julie-e-buring` · `meir-j-stampfer` · `judea-pearl` · `david-hume` · `dorret-i-boomsma` · `terrie-e-moffitt` · `R1-evidence-auditor` · `R4-statistics-measurement` · `R2-red-team`
**Settle:** Is the conflict methodological, biological, or an artifact of populations and timing?
**Checks:** design differences (confounding, compliance, timing of exposure) · population/effect modification ·
measurement differences · Simpson/collider structure · publication bias · what new study resolves it.

## `qualitative-mixed-methods` — 质性与混合方法
**Panel (9):** `iris-murdoch` · `martin-heidegger` · `hannah-arendt` · `mary-midgley` · `ludwig-wittgenstein` · `simone-de-beauvoir` · `R4-statistics-measurement` · `R7-patient-practitioner-voice` · `R2-red-team`
**Settle:** Is the sampling logic, reflexivity and integration defensible? Are findings grounded and transferable?
**Checks:** research stance and reflexivity · sampling and saturation logic · data-to-theme audit trail ·
negative cases · integration points in mixed methods · COREQ/SRQR · member checking.

## `public-health-policy` — 人群与政策层面
**Panel (8):** `walter-c-willett` · `frank-b-hu` · `graham-a-colditz` · `albert-hofman` · `bill-gates` · `martha-nussbaum` · `R6-implementation-realist` · `R2-red-team`
**Settle:** What is the size of the preventable burden, the best-value lever, and the equity impact?
**Checks:** effect size vs feasibility · population vs high-risk strategy · unintended consequences ·
distributional equity · stakeholder alignment · monitoring metrics.

## `translation-commercial` — 转化与产业化路径
**Panel (8):** `robert-langer` · `thomas-edison` · `kiran-mazumdar-shaw` · `anne-wojcicki` · `judy-faulkner` · `warren-buffett` · `steve-jobs` · `R2-red-team`
**Settle:** Who needs it, who pays, what are the regulatory and evidence gates, and what kills it?
**Checks:** problem–solution fit · evidence required per gate · regulatory pathway · IP/skepticism evidence ·
reimbursement and adoption · unit economics · team and stage-gates. (Founders speak to feasibility only.)

## `general-8` — 通用八人组（默认）
**Panel (8):** `socrates` · `david-hume` · `judea-pearl` · `julie-e-buring` · `martha-nussbaum` · `warren-buffett` · `R2-red-team` · `R6-implementation-realist`
**Settle:** Assumptions · evidence · causal structure · design quality · who is missing · opportunity cost/inversion ·
strongest counter-case · feasibility.

---

## Quick-mode reductions (4 lenses)

| Task | Four lenses |
|---|---|
| idea / direction | `socrates` · `judea-pearl` · `R2-red-team` · `R6-implementation-realist` |
| design | `julie-e-buring` · `judea-pearl` · `R4-statistics-measurement` · `R6-implementation-realist` |
| manuscript | `julie-e-buring` · `R4-statistics-measurement` · `R1-evidence-auditor` · `R2-red-team` |
| grant | `eric-s-lander` · `julie-e-buring` · `R3-pre-mortem` · `R6-implementation-realist` |
| measurement | `ludwig-wittgenstein` · `R4-statistics-measurement` · `confucius` · `R7-patient-practitioner-voice` |
| ethics | `immanuel-kant` · `martha-nussbaum` · `elizabeth-anscombe` · `R5-ethics-integrity` |
| AI use | `demis-hassabis` · `andrej-karpathy` · `stuart-russell` · `R5-ethics-integrity` |

## Custom panels

If none fits: pick one lens per need — *what is true* (methodologist), *why* (domain), *what could be wrong*
(red team), *what is missing* (outside), *who bears the cost* (R7), *can it be done* (R6). Add at most 2 more.
