# Fusion Intelligence（融合智能）

[English](README.md) · **简体中文**

> 一个科研问题 → 一组相互独立的推理视角 → 以证据为底座 → **融合**成一个带校准置信度的答案：
> 哪里达成一致、哪里出现分歧、**为什么**分歧、下一步该做什么。

适用于 **Claude Code**、**Codex**、**Antigravity**（以及任何读取 `SKILL.md` / `AGENTS.md` 的智能体）的 Agent Skill。
为科研场景而设计：研究设计、课题申报预审、论文"二号审稿人"、量表研制与验证、临床预测模型、真实世界数据库、
AI 使用决策、科研伦理、选题与方向选择。

它把 [Pantheon](https://pantheon.k-dense.ai/)（80 位"声音"、引用来源、共识环节）背后的方法蒸馏成一套可复用的
严谨流程，并补上多角色面板最容易出错的一环：**模型生成的多个声音彼此一致，并不等于证据。**

---

## 为什么不是"让几位专家聊聊"？

| 常见的多角色提示 | Fusion Intelligence |
|---|---|
| 各角色一起写，互相回声 | 每个视角**独立成稿**（有条件时并行子智能体） |
| 先发表意见，事实后补（或不补） | **先建证据清单**；每条主张标注 `[E#]` 证据 / `[R]` 推理 / `[A]` 假设 |
| "共识"=多数或平均 | 主张被分类：共识 · 有争议 · 单一视角假说 · 盲点 · 回声 |
| 分歧被总结掩盖 | 每个分歧标注**分歧类型**（事实、方法、价值、定义、范围、时间）与裁决路径 |
| 语气笃定 | **校准置信度**；不会仅因多个视角一致就给"高" |
| 冒充真实人物 | 视角是**思维框架**；不代言、不编造引语 |
| 以摘要收尾 | 以**无悔行动、条件行动、决定性检验、证伪条件**收尾 |

## 工作流

```mermaid
flowchart LR
  A[问题简述] --> B[组建面板<br/>6–8 个视角 ≥3 个学科族<br/>+ 红队]
  B --> C[证据落地<br/>证据清单 E1…En<br/>缺口 G1…Gn]
  C --> D[视角独立成稿<br/>带证据标签]
  D --> E[交叉质询<br/>最尖锐的分歧]
  E --> F[融合<br/>主张×视角矩阵<br/>分歧定型 置信度校准]
  F --> G[报告<br/>结论先行 · 一致 · 分歧<br/>路径 · 证伪 · 下一步]
```

四种模式：`quick`（4 视角，≤1 页）· `standard`（6–8，默认）· `deep`（10–16 + 交叉质询，建议并行）·
`pantheon`（80 视角分四批，先聚类成立场再融合）。

## 安装

### 方式一：安装脚本（推荐）

```bash
git clone https://github.com/YUAILUN/Fusion-Intelligence.git
cd Fusion-Intelligence
bash scripts/install.sh              # 一次装到 Claude Code + Codex + Antigravity（用户级）
bash scripts/install.sh --claude     # 只装 Claude Code
bash scripts/install.sh --project .  # 装到当前项目
bash scripts/install.sh --link       # 软链接，git pull 即更新
```

### 方式二：skills CLI

```bash
npx skills add YUAILUN/Fusion-Intelligence
```

### 方式三：手动复制

| 平台 | 复制到 |
|---|---|
| Claude Code | `~/.claude/skills/fusion-intelligence/`（项目级：`<项目>/.claude/skills/…`） |
| Codex | `~/.agents/skills/fusion-intelligence/`（项目级：`<项目>/.agents/skills/…`） |
| Antigravity | `~/.gemini/antigravity/skills/fusion-intelligence/`（项目级：`<项目>/.agent/skills/…`） |
| 其他 | 把 `AGENTS.md` 放到项目根目录 |

安装后重启智能体。随时可用 `python3 scripts/validate.py` 校验包完整性。

## 怎么用

直接提问即可，技能会自动路由；也可显式调用（Claude Code：`/fusion-intelligence`，Codex：`$fusion-intelligence`）。

```text
用融合智能对这个研究想法做压力测试，标准模式：<想法>
用"研究设计"面板审查我附上的方案，给出最危险的 3 个效度威胁。
把这份课题申请书当作评审会预审：逐项打分，指出 3 个最可能被攻击的点，并给出改写优先级。
这篇稿件二号审稿人会怎么说？请对照相应的报告规范逐条检查。
深度模式：这个围手术期数据库适合做预测模型吗？
请用"量表研制"面板审查量表汉化与验证方案，按 COSMIN 顺序列出缺口。
Pantheon 模式：为什么至今没有 ALS 的治愈方法？   # 80 视角聚类后融合
```

## 内容结构

```
SKILL.md                    技能本体：流程、硬规则、路由表、质量闸门
AGENTS.md                   不加载 skill 的智能体用的精简版
references/
  lens-library.md           80 个视角（4 族）+ 7 个角色视角（视角卡）
  panel-presets.md          17 个科研面板 + 快速模式精简组合
  fusion-protocol.md        主张矩阵、分歧定型、置信度校准、反模式
  lens-pass-template.md     单个视角的提示词与输出格式（可直接交给子智能体）
  evidence-grounding.md     证据清单、强度标签、引用规则
  report-templates.md       完整版 / 一页版 / 课题评分卡 / 审稿报告 / 设计备忘（中英）
  research-checklists.md    报告规范、因果、COSMIN 式、预测模型、伦理检查表
  platform-notes.md         三个平台的差异与并行说明
examples/                   成品报告的样子
scripts/install.sh          多平台安装脚本
scripts/validate.py         包校验
agents/openai.yaml          Codex 界面元数据
```

## 内置面板（`panel-presets.md`）

`idea-stress-test` 想法压力测试 · `study-design` 研究设计 · `causal-claim-check` 因果主张审查 ·
`grant-prescreen` 课题预审 · `manuscript-reviewer2` 审稿人视角 · `measurement-scale` 量表研制与验证 ·
`clinical-prediction-model` 临床预测模型 · `real-world-database` 真实世界/围手术期数据库 ·
`intervention-implementation` 护理干预与落地 · `ai-in-research` AI/LLM 使用 · `research-ethics` 科研伦理 ·
`direction-selection` 选题与方向 · `discrepant-results` 矛盾证据 · `qualitative-mixed-methods` 质性与混合方法 ·
`public-health-policy` 公共卫生政策 · `translation-commercial` 转化与产业化 · `general-8` 通用八人组

## 设计原则

1. **结构产生多样性**：靠不同框架、被迫提出的问题与指定立场，而不是不同的"口吻"。
2. **分歧即数据**：呈现它、定型它、说明什么能裁决它。
3. **证据共享，推理独立**：一份清单，多次独立推理。
4. **校准优先于笃定**：说明什么会改变你的结论。
5. **框架而非人物**：不冒充，不编造引语。
6. **诚实的边界**：模型生成的视角面板只能组织与拓宽思考，不增加独立专业知识或数据；它是供你挑战的第二意见，不是裁判。

## 安全与局限

- 不构成医疗、法律或金融建议；临床决策属于有资质的专业人员；伦理审查由伦理委员会决定。
- 请勿粘贴可识别的受试者/患者数据。
- 视角卡是对公开成果的压缩性解读，可能有误；以上游原文件为准。
- 引用必须核实。技能被要求绝不编造参考文献，但请仍然自行检查。
- 在论文/基金中使用时，请按期刊或资助方要求披露 AI 辅助（见 `report-templates.md` 的 T6）。

## 致谢与许可

方法灵感来自 **Pantheon**，视角框架压缩自 **Mimeographs**，两者均由 [K-Dense](https://k-dense.ai/) 发布（MIT）。
本项目为独立作品，与其无隶属关系，详见 [NOTICE.md](NOTICE.md)。基于 [MIT 许可证](LICENSE) 发布。

## 参与贡献

新增或打磨视角、面板、检查表：修改 `references/…`，运行 `python3 scripts/validate.py`，提交 PR。视角卡请只写可追溯到公开成果的
框架级陈述，并保证每个面板都包含红队视角。
