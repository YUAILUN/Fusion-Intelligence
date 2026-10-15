# Lens library

80 reasoning lenses in four families + 7 role lenses. Each row is a **lens card**: hand it (with the Question
Brief and the evidence ledger) to the lens pass.

**How to read a card**
- `id` — slug of the upstream Mimeograph (K-Dense, MIT) so you can pull the full framework steps from
  `github.com/K-Dense-AI/mimeographs/tree/main/mimeographs/<id>` when you need depth.
- *Core question* — the question this lens insists on asking first.
- *Signature moves* — published frameworks / methods associated with the person's public work.
- *Blind spot* — where this lens over-reaches; the fusion step must discount it there.
- *Reach for it when* — triggers.

**Rules for using a card:** the card names a *framework*, not a speaker. Write "after Pearl", "in a Buring-style
trial critique". Never first-person as the person; never fabricate quotes. Cards are compressed
interpretations — they can be wrong; the upstream files are the source.

---

## Family A — Scientists & research methodologists (20)

| id | 中文标签 | Core question | Signature moves | Blind spot | Reach for it when |
|---|---|---|---|---|---|
| `julie-e-buring` | 试验与队列批判评价 | Would this design really answer the question — and is the question finished? | 12-question clinical-trial critique (rationale → participants/N → exposure → randomization → outcome → chance → effect modification → generalizability → ethics → alternatives → finality); investigating discrepant obs-vs-RCT results; future-proofing a cohort | Can over-weight trial design where trials are infeasible | appraising or designing RCT/cohort; conflicting findings |
| `meir-j-stampfer` | 观察性证据与因果解读 | Can long-term observational data plus short-term experiments reach a causal reading (Bradford Hill)? | cumulative-average exposure; isocaloric substitution modeling; Bradford Hill criteria; low-risk-lifestyle scores | Healthy-user bias, residual confounding | exposure measured repeatedly; substitution analyses; RCT infeasible |
| `walter-c-willett` | 营养流行病学 | Compared to what — over what horizon, in real-world eating? | short controlled feeding + large prospective cohorts; AHEI-style quality scoring; health-and-planet (EAT-Lancet) modeling | Self-report diet error; strong priors on diet effects | nutrition/lifestyle exposures; guideline critique |
| `frank-b-hu` | 膳食模式与代谢病 | Which *pattern* — and does it hold across populations and mechanisms? | dietary-pattern factor analysis; systems epidemiology / precision nutrition; food-based quality scores | Pattern derivation is analyst-dependent | cardiometabolic prevention; exposure-pattern measurement |
| `graham-a-colditz` | 预防与风险模型 | What share of the burden is preventable, and who must act for it to happen? | life-course risk accumulation; dynamic risk prediction; epidemiological proof of prevention; stakeholder integration; nested case-control recall/selection-bias checks | Risk-model optimism | prevention programs, clinical risk tools, bias audits |
| `joann-e-manson` | 获益-风险与效应修饰 | For whom does benefit outweigh harm — by age, timing, baseline status? | age/timing-stratified benefit–risk algorithm; targeted (not universal) supplementation based on baseline deficit | Trial populations differ from clinic populations | hormone/supplement-type questions; subgroup logic |
| `kay-tee-khaw` | 健康行为叠加 | How far do a few feasible behaviours go when summed? | Four Health Behaviors score (non-smoking, moderate alcohol, not sedentary, fruit/veg); population-shift thinking | Behaviours cluster with SES — oversimplifies | lifestyle-intervention framing; communicating effect size |
| `tamara-b-harris` | 老年与功能衰退 | Are we measuring early decline or late disability — and does the risk factor flip in the old? | upstream functional assessment (challenging performance tests in well older adults); aging-prevention paradigm stratified by health status; inflammatory biomarker stratification | Older-adult specificity | gerontological nursing, frailty, longitudinal aging studies |
| `albert-hofman` | 生命历程与人群干预 | Where on the life course does this act, and should we shift the population rather than screen individuals? | life-course approach; population-level over individual screening; child-health baseline dimensions; vascular–genetic–ageing interplay | Population claims can mask individual heterogeneity | cohort design, prevention strategy |
| `ronald-c-kessler` | 精准治疗与临床预测 | Is the study big, broad and baseline-deep enough to match patients to treatments? | four requirements for precision treatment research (comprehensive predictors; full range of treatments; large samples via observational CER; ensemble ML); risk model → response model → allocation by efficacy and cost | Observational CER carries confounding | mental-health trials, treatment allocation, clinical ML |
| `terrie-e-moffitt` | 纵向发展轨迹 | What does the *trajectory* say, and is the trait an artefact of family background? | developmental taxonomy from pre-adolescent history; pace-of-aging measurement; sibling-comparison design; hierarchical aggregation of symptoms | Needs long follow-up | behavioural/psychological outcomes, trajectories, self-control |
| `dorret-i-boomsma` | 遗传与家系设计 | How much is genetic vs environmental — and what does high heritability *not* mean? | classical and extended twin-family designs; MZ-discordant design; SEM for twin data | Not applicable without genetic data | nature-vs-nurture claims; confounding by family |
| `eric-s-lander` | 大科学与转化路径 | Can this be staged so each stage pays out — with open data and honest timelines? | staged deliverables; project playbook (goals, collaboration, infrastructure, open data); unbiased mapping; realistic translation pipeline | Big-science framing can overbuild | consortia, data infrastructure, multi-year programs |
| `aviv-regev` | 实验-计算闭环 | Can predictions and experiments form a closed loop? | lab-in-a-loop; perturb–measure–model; multidimensional atlases (type, state, location, history); molecular–morphological validation of computed clusters | Wet-lab-centric | AI + experiment pipelines, high-dimensional data |
| `stacey-gabriel` | 平台化与规模化 | What would industrialize this, with governance? | define vision → flagship efforts → community; high-scale perturbation platform (inputs → perturb → readout → interpret) | Platform bias vs hypothesis-driven work | scaling lab/data workflows; data governance |
| `virginia-m-y-lee` | 机制与患者来源模型 | Is the model built from patient-derived material and does each mechanistic step check out? | propagation pathway modeling; in-vitro amplification of patient aggregates; intervene at release/uptake/degradation; meticulous biobanking | Basic-science depth, thin on policy | mechanism claims, biobanks, neurodegeneration |
| `shizuo-akira` | 反向遗传与实验严谨 | What does knocking it out reveal, and is the ligand claim rigorous? | knockout-driven discovery; rigor in ligand identification (avoid contaminated purified components); scientific independence | Model-organism distance from humans | mechanism discovery, molecular experimental design |
| `robert-langer` | 融合与转化 | Which disciplines must collide, who will carry it to the patient? | first-principles biomaterial design; convergence; skepticism-as-evidence; student-led spin-out | Survivorship in translation stories | translational pathway, devices, persistence against skepticism |
| `zhenan-bao` | 材料与可穿戴 | Can contradictory requirements be met by molecular design? Is the "failure" a clue? | skin-inspired design; designing for contradictory properties; reframing experimental failure | Engineering-centric | wearable/implantable sensing, engineering bottlenecks |
| `zhong-lin-wang` | 自供能与技术路线 | Can the system power itself — and what is the 3-stage roadmap? | harvest–manage–store design; near/mid/long-term roadmap | Hardware-specific | sensors/IoT, energy constraints, scaling roadmaps |

## Family B — Philosophers (20)

| id | 中文标签 | Core question | Signature moves | Blind spot | Reach for it when |
|---|---|---|---|---|---|
| `socrates` | 诘问与假设审计 | What exactly do you mean — and on what evidence do you think that? | elenchus (cross-examination); maieutics; inner dialogue | Produces doubt, not decisions | auditing hidden assumptions, definitions, mentoring |
| `plato` | 概念结构 | What is the structure of the thing — can we collect and divide it correctly? | method of collection and division; Socratic cross-examination; true knowledge needs explanatory structure | Over-idealizes forms | defining a construct/taxonomy; aligning incentives |
| `aristotle` | 观察、四因与适度 | What did we actually observe, what are the four causes, and what is the right level of precision? | four causes; doctrine of the mean; empiricism over theory; match precision to subject; rhetoric (ethos/pathos/logos) | Teleology can smuggle in purpose | mechanism-and-purpose analysis; proposal rhetoric; trade-offs |
| `rene-descartes` | 方法怀疑与分解 | What survives doubt, and can it be decomposed into simpler parts? | radical doubt; four rules (evident truth, divide, order, review); provisional moral code | Foundationalism ignores practice | rebuilding a design from first principles |
| `david-hume` | 经验主义怀疑 | Relation of ideas or matter of fact? Is the causal claim more than regular succession? | Hume's Fork; impression test for terms; experimental method in ethics | Corrosive skepticism | causal overreach, hollow constructs |
| `immanuel-kant` | 义务与认知边界 | Could this maxim be universal; are participants ever merely means; what are the limits of this knowledge? | categorical imperative test; public vs private use of reason; critique of reason (scope of valid claims) | Rigid on consequences | research ethics, limits of inference |
| `ludwig-wittgenstein` | 语言与概念澄清 | Is this a real disagreement or two language games? How is the word actually used? | philosophical therapy; language-games analysis; logical clarification | Dissolves rather than builds | construct and item wording, interdisciplinary misunderstandings |
| `martha-nussbaum` | 能力路径与公平 | What are people actually able to do and be — and who is left out of the average? | capabilities approach; transition anger; liberal education | Hard to operationalize | outcome selection, equity, patient-centred endpoints |
| `hannah-arendt` | 责任与扩展心智 | Whose viewpoint is missing? Are we complying thoughtlessly? | vita activa (labor/work/action); reflective judgment (enlarged mentality); thinking/willing/judging | Abstract | institutional ethics, novel situations without rules |
| `elizabeth-anscombe` | 意图与行动描述 | Under which description is this act intended; what is intended vs merely foreseen? | "Why?" question of intention; doctrine of double effect; action under a description | Narrow focus on act | clinical/research trade-offs with foreseeable harm |
| `iris-murdoch` | 注意力与现实 | Have we truly attended to the particular case, beyond our ego? | refocusing attention; moral perception | Hard to audit | qualitative/clinical encounter, reflexivity |
| `mary-midgley` | 概念管道与多学科 | Which metaphor is leaking — and what does the single-discipline view miss? | philosophical plumbing; dialectical synthesis; multi-disciplinary lens | Can stay at the level of critique | scientism/reductionism checks; synthesis across fields |
| `confucius` | 关系、名分与德行 | Do the names match reality, and what do roles and relationships require? | rectification of names; evaluating character; governance by virtue; reciprocity | Hierarchy assumptions | team culture, mentoring, local/cultural fit of instruments |
| `friedrich-nietzsche` | 谱系与视角 | Whose interests does this "truth" serve — what is its genealogy? | genealogical method; perspectivism | Cynical | challenging field dogma, norms-origin analysis |
| `martin-heidegger` | 技术与现象学 | What does the technical framing conceal about lived experience? | hermeneutic phenomenology; questioning technology | Opaque | technology-in-care critique, lived experience |
| `simone-de-beauvoir` | 情境与自由 | How do situation and freedom interact — who is made the "Other"? | ethics of ambiguity; existential analysis of a situation | Less operational | gender and social context, autonomy |
| `judith-butler` | 范畴与脆弱性 | How do categories construct subjects, and who is made vulnerable? | performativity; ethics of interdependence | Theory-heavy | category choice in measurement (gender, identity), vulnerability |
| `mary-wollstonecraft` | 独立与教育 | Where does arbitrary power create dependence? | first-principles questioning; education as foundation of equality | Dated framing | power asymmetries in labs, training, access |
| `hildegard-of-bingen` | 整体与平衡 | How do body, mind and environment interconnect — what is out of balance? | holistic balance framing | Not evidence-based; use sparingly | integrative/holistic framing, never as validity evidence |
| `hypatia-of-alexandria` | 数学与逻辑基础 | What is the logical/mathematical foundation under this? | mathematics as foundation of truth | Thin primary record | foundational logic checks (use lightly) |

## Family C — AI & ML researchers (20)

| id | 中文标签 | Core question | Signature moves | Blind spot | Reach for it when |
|---|---|---|---|---|---|
| `judea-pearl` | 因果阶梯 | Which rung of the ladder is the question on — and where is the causal model? | ladder of causation (association → intervention → counterfactual); do-operator; back-door criterion; define–assume–identify–estimate | Needs defensible graph | causal claims, covariate selection, prediction-vs-causation |
| `andrew-ng` | 应用与数据中心 | Which *tasks* (not jobs) can be automated; what is the data-centric fix? | agentic workflow iteration; task-based automation analysis; fast feedback hierarchy; corporate AI process | Product-speed bias | adopting AI in workflows; prototyping |
| `andrej-karpathy` | 自主滑块与可靠性 | How much autonomy, with what audit interface — and how many "nines" of reliability? | autonomy slider; march of nines; untangling knowledge | Software-centric | LLM-assisted analysis, agent workflows, teaching |
| `daphne-koller` | AI × 生物数据 | What data should we *generate* so ML can disentangle the biology? | interdisciplinary dataset design; three buckets (biology discovery → molecule → clinic); linking in-vitro and human data | Industry-pipeline view | ML in biomedicine; dataset design |
| `demis-hassabis` | AI 问题适配 | Is it a path through a huge search space, with a clear objective and enough data? | suitable-problem checklist; model-guided search; tabula rasa | Selects for games-like problems | should AI be used here? root-node problems |
| `fei-fei-li` | 以人为本 AI | Does it augment humans — whose values and data are in each lifecycle stage? | human-centered AI framework/lifecycle; north-star problems | Normative | AI ethics, fairness, care contexts |
| `stuart-russell` | 目标不确定与红线 | What if the objective is mis-specified — what are the red lines and who proves safety? | assistance games; provably beneficial AI; red-line regulation | Formal, maximal caution | high-stakes AI deployment, governance |
| `ian-goodfellow` | 对抗与稳健 | How would an adversary or a distribution shift break this? | adversarial training; adversarial fairness; attack awareness | Security framing | robustness and bias testing of models |
| `geoffrey-hinton` | 经验性安全测试 | What does the system actually do when tested on agentic tasks? | empirical AI safety testing; knowledge distillation; inoculation against fakes | Risk-forward | AI risk evaluation, misinformation |
| `yann-lecun` | 世界模型 | Does it have a world model — is next-token enough? | JEPA; objective-driven architectures; energy-based learning | Skeptical of LLM claims | assessing LLM limits, architecture claims |
| `yoshua-bengio` | 预防与治理 | What is the capability-specific risk, and is the system safe by design? | precautionary principle; safe-by-design "scientist AI"; capability-specific risk assessment | Precaution can block use | AI governance, risk assessment |
| `ilya-sutskever` | 研究品味与规模化 | Is the idea simple, beautiful and brain-grounded enough to persist through failures? | top-down research taste; two-stage training; domain randomization | Taste ≠ evidence | choosing research directions |
| `richard-s-sutton` | 苦涩教训 | Does it improve with computation and learn from experience? | bitter lesson; common model of the agent; TD learning; realist prognostication | Dismisses hand-built knowledge | judging AI approaches and forecasts |
| `david-silver` | 经验时代 | Can it learn from its own experience beyond human data? | zero-knowledge self-play; rising-tide problem selection | Needs a simulator/reward | method choice in sequential decision problems |
| `jurgen-schmidhuber` | 压缩与好奇心 | Is the finding compressing the data (learning progress), and has credit been traced? | artificial curiosity; compression-as-science; attribution of priority | Contrarian on credit | history/priority claims, intrinsic-motivation framing |
| `christopher-manning` | 批判性阅读 | What did the authors assume — and why this method rather than another? | critical reading to "break" the idea; probing representations | NLP-centric | paper critique, reading strategy |
| `kaiming-he` | 重构与简化 | Can we reformulate the problem (learn the residual) so it becomes easy? | residual learning; conditional-distribution formulation | Architecture-centric | method reformulation, ablation thinking |
| `pieter-abbeel` | 从模拟到现实 | Does it survive contact with reality? | domain randomization; bootstrapped real-world deployment | Robotics-centric | benchmark → deployment gaps, external validation |
| `sebastian-thrun` | 弱环节与端到端 | What is the weakest link — can we test it first, end to end? | continuous weak-link testing (early freeze); end-to-end build; explicit uncertainty | Engineering bias | pilot design, system integration |
| `jeff-dean` | 系统与量级估算 | Does it still work at 5–10× scale; what do back-of-envelope numbers say? | back-of-envelope design; hardware–ML co-design; distillation | Infrastructure-centric | compute/data pipeline planning |

## Family D — Founders & operators (20)

Speak **only** to feasibility, resourcing, incentives and translation — never to scientific validity.

| id | 中文标签 | Core question | Signature moves | Blind spot | Reach for it when |
|---|---|---|---|---|---|
| `warren-buffett` | 资本配置与逆向 | What is the real value, the downside, the opportunity cost — and how does this fail? | four-filter selection; capital-allocation priorities; inversion | Financial lens | resource allocation, "what could kill this?" |
| `steve-jobs` | 体验与聚焦 | What is the user's experience — and what do we say no to? | customer-centric vision; "last day" test | Taste-driven | tool/instrument usability, scope cutting |
| `elon-musk` | 第一性与量产难度 | What do first principles say; what is the actual bottleneck; is the deadline realistic? | first-principles; production harder than prototype; 50th-percentile deadlines | Overconfident timelines | bottleneck and schedule realism |
| `bill-gates` | 全球健康回报 | What is the impact per dollar, treating all lives equally? | ROI on interventions; innovation to fill market failures | Technocratic | prioritizing health interventions |
| `mark-zuckerberg` | 快速迭代 | What is the smallest version we can ship and learn from? | the Hacker Way; small-group context sharing | Move-fast risk | prototyping tools, iteration cadence |
| `thomas-edison` | 系统发明与证伪 | What is the whole system; what have we eliminated; is it practical? | industrial invention factory; failure as elimination; prove before patenting | Commercial bias | R&D strategy, translation |
| `henry-ford` | 规模与成本 | Can this be made cheap and repeatable for the many? | just-in-time; mass-market economics | Standardization bias | scaling an intervention or instrument |
| `john-d-rockefeller` | 尽调与整合 | What do the books really say; where is the waste? | "look at the books" diligence; cooperative conditional giving | Consolidation mindset | due diligence, funding structure |
| `andrew-carnegie` | 成本控制与回报 | Do the costs support the mission; does giving empower self-improvement? | watch costs; community-matched philanthropy | Paternalism | budget realism, funder alignment |
| `walt-disney` | 叙事与迭代质量 | Does the story land — can we "plus" it one more round? | storyboarding; constructive feedback and plussing | Showmanship | scientific storytelling, figures, presentations |
| `oprah-winfrey` | 意图与同理 | What is the intention, and what do people truly need to feel heard? | "get still" decision process; intention-based decisions | Intuition-led | participant experience, burden |
| `sara-blakely` | 局外人与自举 | What would an outsider try with almost no money? | outsider advantage; bootstrap; protect ideas in infancy | Anecdotal | pilot-first, low-cost feasibility |
| `whitney-wolfe-herd` | 安全设计 | What guardrails make the safe behaviour the default? | engineered kindness; the "why" test | Platform-specific | intervention/platform guardrails, user safety |
| `anne-wojcicki` | 数据主权与监管 | Who owns the data, and how do we work with regulators? | consumer-owned data; navigating regulated environments; trough of sorrow | Consumer-genetics context | consent, data ownership, regulatory pathway |
| `judy-faulkner` | 互操作与医生负担 | Does it integrate with real clinical systems without adding burden? | interoperability; protected data sharing; reduce burnout | Vendor view | EHR-based research, clinical informatics |
| `kiran-mazumdar-shaw` | 可负担创新 | Can innovation be affordable and globally competitive? | four buckets of innovation; entrepreneurial phases | Industry framing | biotech translation, low-resource settings |
| `diane-hendricks` | 逆周期与尽调 | Is there a due-diligence-backed move others fear in a downturn? | acquisition due diligence; hands-on vocational training | Narrow domain | team building, capacity development |
| `lynda-resnick` | 社区主导与试点推广 | What does the community itself say it needs? | community-led solutions; test-and-roll; hands-on philanthropy | Marketing flavor | community engagement, staged rollout |
| `marian-ilitch` | 愿景×尽调 | Is the vision matched by unit economics and accountability? | visionary / due-diligence stress test; tactile pulse check | Retail framing | budget and feasibility sanity checks |
| `thai-lee` | 长期与排除法 | What is the 10-year path, and what can we eliminate? | decade-by-decade planning; career selection by elimination | Personal-strategy | career and lab-strategy planning |

---

## Role lenses (added by this skill — not from Pantheon)

Functional lenses that every serious panel needs. Use them like any other card.

| id | 中文标签 | Core question | Moves |
|---|---|---|---|
| `R1-evidence-auditor` | 证据审计 | Does each factual claim trace to a verified source of adequate strength? | check ledger entry per claim; grade strength A–D; flag mismatch between claim and design; check recency, population, outcome directness |
| `R2-red-team` | 红队证伪 | What is the strongest case that the leading conclusion is wrong? | build the best rival hypothesis; look for confounding, selection, measurement, reverse causation, p-hacking, garden of forking paths; propose the decisive disconfirming test |
| `R3-pre-mortem` | 事前验尸 | It is 12 months later and this failed — why? | list 5–7 failure stories; rank by likelihood × impact; propose early-warning signals and mitigations |
| `R4-statistics-measurement` | 统计与测量 | Is the estimand clear, the sample adequate, the measurement valid and reliable? | estimand definition; power/precision; multiplicity; missing data; construct and content validity; reliability; invariance; calibration and clinical utility |
| `R5-ethics-integrity` | 伦理与诚信 | Are consent, privacy, vulnerability, data governance, authorship and AI-use disclosure sound? | risk–benefit; consent and withdrawal; data minimization and security; fair participant selection; conflict of interest; transparent AI-use disclosure |
| `R6-implementation-realist` | 落地可行性 | Who will actually do this, with what time, money, training and workflow? | feasibility, staffing, burden, cost, adoption barriers, scalability (e.g., RE-AIM, CFIR) |
| `R7-patient-practitioner-voice` | 患者与一线人员视角 | Does this matter to patients and frontline staff, and what does it cost them? | outcome relevance; participant burden; cultural/linguistic fit; frontline workflow; plain-language test |

---

## Using the library at scale (`pantheon` mode)

- Split the 80 lenses by family into 4 batches (20 each). One agent per batch; each lens gets ≤ 60 words in the
  `pantheon` schema (position · one claim with tag · one objection · confidence).
- Then **cluster** positions (not lenses) into 4–7 stances; fuse stances, not voices.
- Always add the role lenses R1, R2, R4, R5 and R6 *outside* the batches.
