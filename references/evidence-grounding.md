# Evidence grounding (Step 3)

Pantheon-style answers are only as good as the facts under them. Ground first, then reason.

## 1. The evidence ledger

| ID | Claim (as the source states it) | Source (author, year, venue; DOI/PMID/URL) | Design & N | Population / setting | Effect / direction | Strength (A–D) | Verified? |
|---|---|---|---|---|---|---|---|
| E1 | … | … | RCT, n=… | … | … | B | yes/no |

Gaps: `G1 …` — facts the decision needs that were not found. Gaps are first-class output.

## 2. Strength tags (heuristic; not a formal GRADE rating)

| Tag | Meaning |
|---|---|
| **A** | systematic review/meta-analysis of good studies; or large, well-conducted, replicated RCT(s) |
| **B** | single good RCT; multiple consistent well-adjusted cohorts; guideline recommendation grounded in A/B |
| **C** | single observational study; small/underpowered trial; preprint; mechanistic or animal evidence |
| **D** | expert opinion; case reports; model-generated reasoning; unverified or secondary reporting |

Downgrade for indirectness (wrong population/outcome), inconsistency, imprecision, risk of bias, and
publication bias. Upgrade for large effect, dose-response, and plausible residual confounding that would
*reduce* the effect.

## 3. Where to look (use what the runtime offers)

1. **The user's own material first** — protocol, draft, data dictionary, reviewer comments, prior papers.
2. **Literature tools** — PubMed/PMC (e.g., a PubMed MCP connector), Consensus-type search, preprint servers;
   registries (ClinicalTrials.gov, ChiCTR); guideline repositories.
3. **Web search** for guidelines, standards, regulator pages — prefer primary sources.
4. **Chinese literature** (CNKI, Wanfang, VIP) is often not reachable by tools: say so, ask the user to supply
   key papers, and mark language/coverage limits in the report.
5. **Nothing available?** Work from the user's material and general knowledge; mark all non-user facts `[R]`
   or `D`, and list what should be looked up.

## 4. Citation rules

- Cite only sources you actually retrieved or the user supplied. Prefer DOI/PMID.
- If you recall a reference from memory, label it **"unverified — please check"** and give no fabricated
  details (page numbers, exact statistics).
- One claim → one source of record. If sources disagree, include both and type the divergence.
- Report the **design and population** next to each effect; "reduced risk by 20%" without them is not evidence.
- Quote nothing longer than a short phrase from any source; paraphrase and attribute.
- Never attribute statements to real people from lens cards; cards describe frameworks.

## 5. Recency and relevance check

For fast-moving topics (AI methods, guidelines, regulation) confirm the date and version of each source and
search for newer versions of guidelines (e.g., reporting guidelines are revised). Say "as of <date>".

## 6. Handling the user's data

- Do not paste identifiable patient or participant data into prompts, ledgers or reports. Work with
  aggregates, de-identified extracts or synthetic examples.
- Note applicable governance (ethics approval, data-use agreements, local privacy and data-security law).
  Ask the user to confirm local requirements; do not assert them.

## 7. Minimal ledger for `quick` mode

Three to five rows plus gaps is enough. Do not stall on retrieval: label what was not checked.
