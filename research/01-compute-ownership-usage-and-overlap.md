# AI compute: ownership, usage, and overlap

Evidence cutoff: November 4, 2026, America/Chicago. Scope: AI accelerators, associated capacity, and provider/customer relationships across the six named organizations. Ordinary CPU cloud computing is outside the numerical comparison.

## Findings

1. The historical ownership proxy orders the quantified fleets Google, Microsoft, Amazon, then xAI. That is not a current operating-capacity ranking. [S01](../sources/README.md#s01--ai-chip-owners)
2. OpenAI and Google DeepMind lead the selected end-2025 lab-use medians, with overlapping uncertainty. [S02](../sources/README.md#s02--ai-chip-users)
3. No complete public dataset here measures actual utilization across all six on November 4, 2026. A precise current winner or aggregate overlap percentage remains unresolved.

## 1. Historical ownership comparison

| Organization / source label | H100e, derived sum of chip-family medians | Observation date |
|---|---:|---|
| Google | 5,049,814 | 2025-12-31 |
| Microsoft | 3,416,016 | 2025-12-31 |
| Amazon | 2,448,673 | 2025-12-31 |
| xAI, now within SpaceXSI | 553,714 | 2025-12-31 |
| OpenAI | Not quantified in owner extract | — |
| Anthropic | Not quantified in owner extract | — |

Derived from the [selected components](../data/ownership_components_2025.csv), using Epoch's ownership CSV. H100e normalizes modeled chip capability, not realized workload throughput. Delivery-based estimates may precede operation. A sum of component medians is a descriptive proxy, not a joint statistical median; no aggregate interval is claimed. Ownership attribution is informal control, not audited legal title. [S01](https://epoch.ai/data/ai-chip-owners)

## 2. Compute allocated to AI developers

| Lab / source label | Median H100e | 5th–95th percentile | Observation date |
|---|---:|---:|---|
| OpenAI | 1,743,440 | 1,251,477–2,185,142 | 2025-12-31 |
| Google DeepMind | 1,583,430 | 1,008,220–2,548,756 | 2025-12-31 |
| Anthropic | 1,189,574 | 842,242–1,716,535 | 2025-12-31 |
| SpaceXAI | 634,793 | 587,268–786,633 | 2025-12-31 |

Values are rounded from the [downloaded lab rows](../data/lab_usage_2025.csv), not inferred by subtracting provider fleets. This scope covers frontier research, training, and inference; it does not cover all Alphabet activity. Comparable internal-lab estimates for Amazon and Microsoft are absent. [S02](https://epoch.ai/data/ai-chip-users), [S14](https://epoch.ai/data/ai-chip-users-documentation/methodology)

**Reconciliation:** Epoch's explanatory article lists SpaceXAI at 615,000 H100e with a 551,000–700,000 range, whereas the retrieved downloadable CSV gives the values above. The earlier chat repeated the article. This installment uses the numeric download and preserves the discrepancy rather than silently treating the versions as identical. Provider stock and lab allocation also use different models and revisions; the xAI/SpaceXAI rows must not be subtracted to estimate spare capacity. [S03](https://epoch.ai/latest/introducing-the-ai-chip-users-explorer)

## 3. A current view of selected physical sites

| Site | Estimated operational IT capacity, November 2026 |
|---|---:|
| Anthropic-Amazon New Carlisle | 1,037 MW |
| Colossus 2 | 946 MW |
| OpenAI Stargate Abilene | 824 MW |
| Microsoft Fairwater Atlanta | 636 MW |

These are selected facilities in Epoch's tracker, not complete company fleets. Capacity to draw power is not measured electricity consumption or completed computation. Modern chips also deliver different performance per watt. The source's future buildout values are excluded from this table. [S04](https://epoch.ai/graphs/largest-ai-data-centers-by-power-capacity)

## 4. Provider/customer overlap

| Provider → customer | Evidence and scale | Accounting treatment |
|---|---|---|
| Microsoft → OpenAI | Primary cloud partner under April 27 agreement. [S08](https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/) | Provider fleet and customer allocation overlap; no public percentage here. |
| Amazon → Anthropic | Over one million Trainium2 chips reported in use; expanded agreement up to 5 GW, including nearly 1 GW targeted by end-2026. [S05](https://www.anthropic.com/news/anthropic-amazon-compute) | Current reported chip use and future capacity are separate measures. |
| Google/Broadcom → Anthropic | April announcement says multiple GW from 2027; May summary specifies 5 GW. [S13](https://www.anthropic.com/news/google-broadcom-partnership-compute), [S06](https://www.anthropic.com/news/higher-limits-spacex) | Treat as descriptions of one expansion; not two additive contracts. |
| Microsoft → Anthropic | $30 billion Azure purchase commitment and additional capacity wording up to 1 GW. [S09](https://www.anthropic.com/news/microsoft-nvidia-anthropic-announce-strategic-partnerships) | Contract scale; delivery and utilization are not established. |
| Amazon → OpenAI | Approximately 2 GW Trainium commitment; ramp begins in 2027. [S10](https://openai.com/index/amazon-partnership/), [S11](https://s2.q4cdn.com/299287126/files/doc_earnings/2026/q1/earnings-result/AMZN-Q1-2026-Earnings-Release.pdf) | Future capacity, excluded from current operating totals. |
| SpaceXSI → Anthropic | All Colossus 1 access announced: over 220,000 GPUs and 300 MW within a month. [S06](https://www.anthropic.com/news/higher-limits-spacex) | Site-level contracted access; not measured workload activity. |
| SpaceXSI → Anthropic, broader scope | Prospectus describes approximately 325,000 GPUs across Colossus 1 and 2, with a May–June ramp. [S07, PDF p. 76](https://content.spacex.com/cms-assets/FINAL_Documents%20and%20Updates/SpaceX%20-%20EU%20Prospectus%20%28Approved%20by%20Bafin%29%20-%20June%205%2C%202026.pdf#page=77) | Broader contract includes the preceding row; do not add 220,000 and 325,000. |
| Google → OpenAI | Google Cloud announced model-garden distribution. [S12](https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-brings-openai-models-to-customers) | Distribution relationship; not proof of training hardware allocation. |
| SpaceXSI → Google | Epoch describes Google as a customer of SpaceX compute. [S03](https://epoch.ai/latest/introducing-the-ai-chip-users-explorer) | Relationship supported by research analysis; exact primary contract/delivery still to reconcile. |

The [structured ledger](../data/relationships.csv) gives stable relationship IDs and caveats. It is an initial evidence inventory, not an exhaustive supplier list. Oracle and CoreWeave, although outside the requested six, matter to any complete mapping of OpenAI's supply. [S03](https://epoch.ai/latest/introducing-the-ai-chip-users-explorer)

## 5. What “overlap” can mean

- **Accounting overlap:** a customer's rented allocation sits inside a provider's fleet. Adding both counts the allocation twice.
- **Common provider dependence:** two labs use the same cloud operator. This does not establish that they share the same cluster or failure domain.
- **Commercial distribution:** a cloud sells access to a model. This alone does not locate the model's training fleet.
- **Financial connection:** investment, revenue sharing, or purchase commitments create commercial links. They do not demonstrate physical capacity sharing.

For an illustrative 100-unit provider fleet, if a lab rents 30 units from it, the physical stock remains 100, not 130. Provider dependence would be 30 divided by that lab's total allocation, which is a different denominator. Actual allocations, dates, and common units are required before computing either percentage.

## 6. Limits and next decision

This evidence does not support a current global six-company utilization leaderboard, an industry-wide overlap percentage, or a training-performance ranking derived solely from MW. It supports a historical comparison plus a dated relationship map. The next installment should reconcile operating sites to owners, operators, and tenants before aggregating company totals. See the [research agenda](02-research-agenda.md).
