# AI → server company → location

Evidence cutoff: **November 4, 2026, America/Chicago**. This table organizes documented relationships, likely campus links, contracts and distribution links. It is not a live routing trace or an exhaustive supplier census.

**The share of each AI's total compute processed by each server company or location is undisclosed in this evidence.** Empty numeric percentage fields are unknown, not zero. Unweighted connections indicate relationships, not equal allocation.

## Overview

| AI / model family | Server companies / relationships | Locations tied to each company | % of AI total compute |
|---|---|---|---|
| OpenAI / ChatGPT | Oracle / OCI; Microsoft / Azure; CoreWeave; AWS | Oracle: Abilene, TX. Azure: Atlanta, GA / Wisconsin / Arizona (likely). CoreWeave: Denton, TX (likely). AWS: campuses undisclosed. [S19](https://openai.com/index/five-new-stargate-sites/), [S18](https://news.microsoft.com/source/features/ai/from-wisconsin-to-atlanta-microsoft-connects-datacenters-to-build-its-first-ai-superfactory/), [S27](https://openai.com/index/scaling-ai-for-everyone/), [S28](https://www.aboutamazon.com/news/aws/aws-open-ai-workloads-compute-infrastructure) | Undisclosed |
| Anthropic / Claude | AWS; SpaceXSI; Google Cloud; Azure; Fluidstack; CoreWeave | AWS: New Carlisle, IN. SpaceXSI: Memphis, TN. Google / Azure / CoreWeave: campuses undisclosed. Fluidstack: NY / TX expansion. [S05](https://www.anthropic.com/news/anthropic-amazon-compute), [S06](https://www.anthropic.com/news/higher-limits-spacex), [S13](https://www.anthropic.com/news/google-broadcom-partnership-compute), [S09](https://www.anthropic.com/news/microsoft-nvidia-anthropic-announce-strategic-partnerships), [S22](https://www.anthropic.com/news/anthropic-invests-50-billion-in-american-ai-infrastructure), [S26](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Announces-Multi-Year-Agreement-With-Anthropic/) | Undisclosed |
| Google / Gemini | Google; SpaceXSI (reported) | Google-owned campus examples: Pryor, OK; Columbus / New Albany, OH; Council Bluffs, IA. Gemini-specific site assignment uncertain. SpaceXSI tenant location undisclosed. [S30](https://cloud.google.com/blog/products/infrastructure/bringing-google-tpus-to-oracle-cloud-infrastructure), [S16](https://epoch.ai/data/ai-data-centers/map), [S03](https://epoch.ai/latest/introducing-the-ai-chip-users-explorer) | Undisclosed |
| Microsoft AI / Copilot | Microsoft / Azure; Nebius; Nscale | Azure: Atlanta, GA / Wisconsin / Arizona. Nebius: New Jersey (likely), Finland (possible). Nscale: Sines, Portugal. Model-level routing unknown. [S18](https://news.microsoft.com/source/features/ai/from-wisconsin-to-atlanta-microsoft-connects-datacenters-to-build-its-first-ai-superfactory/), [S16](https://epoch.ai/data/ai-data-centers/map) | Undisclosed |
| Amazon / Nova | Amazon / AWS | Nova: exact campuses undisclosed. AWS-owned AI capacity mapped in Indiana, Mississippi, Ohio and Pennsylvania; this does not assign Nova to those sites. [S29](https://docs.aws.amazon.com/nova/latest/userguide/what-is-nova.html), [S16](https://epoch.ai/data/ai-data-centers/map) | Undisclosed |
| SpaceXSI / Grok | SpaceXSI | Organization-linked sites: Colossus 2, Memphis, TN; QTS record, Atlanta, GA. Grok-specific split undisclosed. Colossus 1 access contracted to Anthropic. [S23](https://x.ai/memphis), [S16](https://epoch.ai/data/ai-data-centers/map), [S06](https://www.anthropic.com/news/higher-limits-spacex) | Undisclosed |

## Provider-to-location evidence ledger

`Cloud provider`, `campus owner`, `own infrastructure`, `infrastructure partner` and `model distributor` are separate roles. A campus owner need not operate the cloud service. An expansion announcement does not prove delivery. Google Cloud's OpenAI distribution row is retained for context and explicitly excluded from proof of a physical compute allocation.

| AI | Server company and role | Location | Evidence status | AI total-compute share | Sources |
|---|---|---|---|---|---|
| OpenAI | Oracle / OCI (cloud provider) | Abilene, Texas, US | Operating; Confirmed | Undisclosed | [S19](https://openai.com/index/five-new-stargate-sites/), [S27](https://openai.com/index/scaling-ai-for-everyone/) |
| OpenAI | Microsoft / Azure (cloud provider) | Fayetteville (Atlanta), Georgia; Mount Pleasant, Wisconsin; Goodyear, Arizona, US | Operating provider; likely site links; Likely | Undisclosed | [S08](https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/), [S18](https://news.microsoft.com/source/features/ai/from-wisconsin-to-atlanta-microsoft-connects-datacenters-to-build-its-first-ai-superfactory/), [S16](https://epoch.ai/data/ai-data-centers/map), [S27](https://openai.com/index/scaling-ai-for-everyone/) |
| OpenAI | CoreWeave (cloud provider) | Denton, Texas, US | Operating provider; likely site link; Likely | Undisclosed | [S27](https://openai.com/index/scaling-ai-for-everyone/), [S16](https://epoch.ai/data/ai-data-centers/map) |
| OpenAI | Amazon / AWS (cloud provider) | United States; exact campuses undisclosed | Supply relationship announced; Undisclosed | Undisclosed | [S28](https://www.aboutamazon.com/news/aws/aws-open-ai-workloads-compute-infrastructure), [S10](https://openai.com/index/amazon-partnership/), [S11](https://s2.q4cdn.com/299287126/files/doc_earnings/2026/q1/earnings-result/AMZN-Q1-2026-Earnings-Release.pdf) |
| OpenAI | Google Cloud (model distributor) | Exact processing campuses undisclosed | Distribution only in this evidence; Undisclosed | Undisclosed | [S12](https://cloud.google.com/blog/products/ai-machine-learning/google-cloud-brings-openai-models-to-customers) |
| Anthropic | Amazon / AWS (cloud provider) | New Carlisle, Indiana, US | Operating; Confirmed | Undisclosed | [S05](https://www.anthropic.com/news/anthropic-amazon-compute), [S20](https://www.aboutamazon.com/news/aws/aws-project-rainier-ai-trainium-chips-compute-cluster), [S16](https://epoch.ai/data/ai-data-centers/map) |
| Anthropic | SpaceXSI (compute provider / campus owner) | Memphis, Tennessee, US — Colossus 1 and 2 | Contracted access; operating campuses; Confirmed | Undisclosed | [S06](https://www.anthropic.com/news/higher-limits-spacex), [S07](https://content.spacex.com/cms-assets/FINAL_Documents%20and%20Updates/SpaceX%20-%20EU%20Prospectus%20%28Approved%20by%20Bafin%29%20-%20June%205%2C%202026.pdf), [S16](https://epoch.ai/data/ai-data-centers/map) |
| Anthropic | Google Cloud (cloud provider) | Existing TPU campuses undisclosed | Existing partnership; Undisclosed | Undisclosed | [S13](https://www.anthropic.com/news/google-broadcom-partnership-compute) |
| Anthropic | Microsoft / Azure (cloud provider) | Exact campuses undisclosed | Contract announced; delivery split unknown; Undisclosed | Undisclosed | [S09](https://www.anthropic.com/news/microsoft-nvidia-anthropic-announce-strategic-partnerships) |
| Anthropic | Fluidstack (infrastructure partner) | New York and Texas, US — announced expansion | Expansion announced; State-level | Undisclosed | [S22](https://www.anthropic.com/news/anthropic-invests-50-billion-in-american-ai-infrastructure) |
| Anthropic | AI XPV Platform (campus owner per tracker) | Barker, New York, US — Lake Mariner | Positive campus MW; likely user link; Likely | Undisclosed | [S16](https://epoch.ai/data/ai-data-centers/map) |
| Anthropic | CoreWeave (cloud provider) | Exact campuses undisclosed | 2026 capacity agreement; delivery unverified here; Undisclosed | Undisclosed | [S26](https://investors.coreweave.com/news/news-details/2026/CoreWeave-Announces-Multi-Year-Agreement-With-Anthropic/) |
| Google | Google (own infrastructure) | Google-owned campuses, including Pryor, Oklahoma; Columbus/New Albany, Ohio; Council Bluffs, Iowa, US | Operating fleet; model site assignment uncertain; Possible for Gemini sites | Undisclosed | [S30](https://cloud.google.com/blog/products/infrastructure/bringing-google-tpus-to-oracle-cloud-infrastructure), [S21](https://www.datacenters.google/locations/oklahoma/), [S16](https://epoch.ai/data/ai-data-centers/map) |
| Google | SpaceXSI (external compute provider) | Exact tenant campus assignment undisclosed | Research-reported rental relationship; Undisclosed | Undisclosed | [S03](https://epoch.ai/latest/introducing-the-ai-chip-users-explorer) |
| Microsoft | Microsoft / Azure (own infrastructure) | Fayetteville (Atlanta), Georgia; Mount Pleasant, Wisconsin; Goodyear, Arizona, US | Operating fleet; internal workload split unknown; Likely / confirmed organization links | Undisclosed | [S18](https://news.microsoft.com/source/features/ai/from-wisconsin-to-atlanta-microsoft-connects-datacenters-to-build-its-first-ai-superfactory/), [S16](https://epoch.ai/data/ai-data-centers/map) |
| Microsoft | Nebius (external compute provider) | Vineland, New Jersey, US; Mantsala, Uusimaa, Finland | Research-attributed user links; Likely / possible | Undisclosed | [S16](https://epoch.ai/data/ai-data-centers/map) |
| Microsoft | Nscale (external compute provider) | Sines, Portugal | Research-attributed user link; Confirmed organization link | Undisclosed | [S16](https://epoch.ai/data/ai-data-centers/map) |
| Amazon | Amazon / AWS (own infrastructure / model service) | Nova exact campuses undisclosed; mapped AWS owner footprint spans Indiana, Mississippi, Ohio and Pennsylvania, US | Nova on Bedrock; campus assignment unknown; Undisclosed for Nova | Undisclosed | [S29](https://docs.aws.amazon.com/nova/latest/userguide/what-is-nova.html), [S16](https://epoch.ai/data/ai-data-centers/map) |
| SpaceXSI | SpaceXSI (own infrastructure) | Memphis, Tennessee, US — Colossus 2; Atlanta, Georgia, US — QTS record | Operating organization links; Confirmed organization links | Undisclosed | [S23](https://x.ai/memphis), [S16](https://epoch.ai/data/ai-data-centers/map) |

## Percentages that are supportable

1. **Dated site-contract scope:** Anthropic's May 6 announcement covers all of Colossus 1 capacity (100% of that site's contracted access in the announcement). This is not 100% of Claude's compute, not a measurement of actual usage, and not evidence that the contract stayed unchanged. The broader Colossus 1/2 contract must not be added to this figure. [S06](https://www.anthropic.com/news/higher-limits-spacex)
2. **Mapped owner footprint:** the companion chart shows state-level shares of each server company's mapped, confidently owned, positive-IT-MW capacity. These are the same denominators as the preceding geography installment; they exclude external rented capacity and untracked campuses. They do not assign that owner's capacity to any particular AI tenant. [Calculation data](../data/geography_capacity_shares.csv), [geography methodology](03-server-locations-and-geographic-shares.md)

The share chart groups all states below the two largest into “Other mapped locations” to remain legible. The underlying CSV retains every site. Rounding may cause displayed labels to sum to 99.9% or 100.1%.

## Important route limits

- OpenAI's existing AWS NVIDIA supply is distinct from its future 2027 Trainium ramp. No AWS campus is assigned solely from a cloud contract.
- Anthropic's Google TPU relationship does not identify which Google campuses process Claude. Likewise, the Azure and CoreWeave agreements do not locate delivery by campus in the reviewed announcements.
- Google's own campus footprint does not prove Gemini-specific execution at each listed campus. Its SpaceX compute relationship does not identify a particular Colossus campus here.
- Microsoft AI, Copilot, Azure external customers and third-party model access have different workloads. A Microsoft tenant link does not by itself identify Copilot execution.
- Nova access through Amazon Bedrock supports the service-provider relationship; AWS campus ownership does not establish Nova training or inference at each site.
- SpaceXAI organization-level use and Grok submodel routing are different. Colossus 1 is not assigned to Grok by ownership alone.
- The Lake Mariner campus-owner record and the Fluidstack expansion relationship may describe overlapping infrastructure. They are not additive compute allocations.

## Deliverables

- [Interactive relationship table and owner-footprint chart](../charts/ai-provider-location.html) — download and open; GitHub displays HTML source.
- [Summary CSV](../data/ai-provider-location-summary.csv)
- [Detailed route CSV](../data/ai-provider-location-routes.csv) and [JSON](../data/ai-provider-location-routes.json)
- [Source register](../sources/README.md)

The route table combines existing repository evidence with newly checked official announcements. Site confidence labels and MW are inherited estimates, not independent audits. Model names identify families rather than proving a specific version ran at a particular campus.
