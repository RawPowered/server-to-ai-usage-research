# Server locations and geographic capacity shares

Evidence cutoff: **November 4, 2026, America/Chicago**. This installment adds a pin map and location inventory for the original six organizations. The snapshot is a selection from public research, not a census of all servers.

## What the percentages answer

**The percentage of each AI's global workload at each location remains unknown for all six.** Public sources establish deployments and relationships, but this evidence has no complete same-date allocation or utilization denominator. Google-owned does not mean Gemini-only, and Microsoft-owned does not mean Copilot-only.

The computable percentages below mean **a location's share of mapped, confidently attributed, positive-IT-MW sites owned by that company**. They exclude untracked capacity, speculative owners, sites with zero current capacity, and externally rented capacity. They measure a physical-capacity proxy, not requests, tokens, GPU-hours, customer allocations, or global company share. Derivation: site IT MW / sum of eligible owner-site IT MW × 100. All rows use the retrieved November 4 snapshot. [S15](https://epoch.ai/data/ai-data-centers), [S17](https://epoch.ai/data/data-centers-documentation/methodology)

## Geographic shares within the mapped owned subset

| Company | Eligible sites | Mapped IT MW denominator | State/country shares of that denominator |
|---|---:|---:|---|
| Amazon | 5 | 1,870.00 | Indiana, United States 55.5%; Mississippi, United States 27.4%; Ohio, United States 11.4%; Pennsylvania, United States 5.8% |
| Google | 16 | 2,941.00 | Ohio, United States 26.3%; Nebraska, United States 20.9%; Oklahoma, United States 12.5%; Iowa, United States 8.1%; Arizona, United States 6.2%; Texas, United States 6.1%; Nevada, United States 5.5%; Oregon, United States 5.2%; Missouri, United States 3.6%; Hertfordshire, United Kingdom 3.0%; Virginia, United States 2.6% |
| Microsoft | 6 | 1,519.00 | Georgia, United States 41.9%; Wisconsin, United States 24.3%; Arizona, United States 13.3%; Iowa, United States 12.5%; Texas, United States 8.0% |
| SpaceXSI | 3 | 1,303.33 | Tennessee, United States 98.7%; Georgia, United States 1.3% |

The [site-level calculations](../data/geography_capacity_shares.csv) preserve the denominator for every percentage. This is **not** a six-company market-share table; percentages normalize separately within each owner. Anthropic and OpenAI have no numeric workload-share rows because campus capacity cannot be assigned wholly to a tenant.

## What is known for each AI

| AI/company | Location evidence | What is still unknown |
|---|---|---|
| OpenAI / ChatGPT | Abilene, Texas is explicitly documented as running OpenAI training and inference. Microsoft's Fairwater network connects Atlanta and Wisconsin to support OpenAI and other workloads. Additional Azure/CoreWeave associations retain research confidence labels. [S19](https://openai.com/index/five-new-stargate-sites/), [S18](https://news.microsoft.com/source/features/ai/from-wisconsin-to-atlanta-microsoft-connects-datacenters-to-build-its-first-ai-superfactory/) | Percentage of OpenAI work at each campus or provider; network support does not prove an exclusive per-campus allocation. |
| Anthropic / Claude | AWS Rainier spans multiple US data centers. New Carlisle is confidently associated in the tracker; Colossus 1 and 2 are also associated. New York and Texas expansion is publicly announced. [S20](https://www.aboutamazon.com/news/aws/aws-project-rainier-ai-trainium-chips-compute-cluster), [S06](https://www.anthropic.com/news/higher-limits-spacex), [S22](https://www.anthropic.com/news/anthropic-invests-50-billion-in-american-ai-infrastructure) | Claude's site/provider workload split; speculative AWS site associations are not confirmed tenant deployments. |
| Google / Gemini | Google publishes an operating Pryor campus and other locations. Many Google owner sites have speculative DeepMind user labels in the research data; the map preserves this distinction. [S21](https://www.datacenters.google/locations/oklahoma/), [S16](https://epoch.ai/data/ai-data-centers/map) | Which share of each campus serves Gemini, other Google products, or external customers. |
| Microsoft / Copilot and Microsoft AI | Owned campuses include Fairwater Atlanta/Wisconsin, Goodyear, Cumming and San Antonio. The data also identifies rented-capacity links in New Jersey, Finland, Portugal and Norway at varying confidence levels. [S16](https://epoch.ai/data/ai-data-centers/map), [S18](https://news.microsoft.com/source/features/ai/from-wisconsin-to-atlanta-microsoft-connects-datacenters-to-build-its-first-ai-superfactory/) | Copilot/internal models vs external customer allocations; rented sites are excluded from owned-capacity percentages. |
| Amazon / AWS and Nova | The selected owned sites are in Indiana, Mississippi, Ohio and Pennsylvania. Rainier supports Claude, so AWS locations cannot be treated as Nova-only. [S15](https://epoch.ai/data/ai-data-centers), [S20](https://www.aboutamazon.com/news/aws/aws-project-rainier-ai-trainium-chips-compute-cluster) | Nova's specific training/inference distribution and AWS's full global AI footprint. |
| SpaceXSI / Grok | Colossus campuses are in the Memphis region; the tracker also includes a small Atlanta deployment. Historical company material links Colossus to Grok, while current contracts include external tenants. [S23](https://x.ai/memphis), [S07](../sources/README.md) | Current Grok-exclusive capacity and tenant-by-tenant workload shares. Colossus ownership is not exclusive Grok usage. |

## How to read the map

Open [the interactive map](../maps/index.html) after downloading the repository, or use the inline map in the research chat. GitHub displays HTML source rather than running this page. The map uses embedded published geographic geometry; it needs an internet connection for its version-pinned D3/TopoJSON libraries.

- Company selection includes owner and user relationships. A pin identifies the owner separately from the user and the user's confidence label.
- Filled pins represent sites with positive estimated operating capacity; rings represent records with zero current IT MW when the planned/unpowered option is enabled. Zero does not prove absence of all activity.
- Locations are published approximate campus points, not individual server coordinates. Closely spaced Memphis pins may overlap; use the site selector or zoom for details.
- Capacity belongs to the campus. Multi-tenant sites do not transfer their entire capacity to every named AI.
- Missing tenant labels mean unknown, not no AI activity. `Confident`, `likely`, `speculative`, and `unclassified` remain source assessments, not independent audits by this project.

## Files and limitations

The [location inventory](../data/geography_sites.csv), [GeoJSON pins](../data/server-locations.geojson), and [structured records](../data/geography_sites.json) support further research. The JSON retains the source's upstream evidence links for each site; those links are pointers, not a claim that each has been independently inspected here. The selection and capacity normalization are this project's derivations from credited Epoch AI data, adapted under its stated CC BY license.

Planned sites remain separate from operating denominators. Cloud product regions and data-storage residency were not turned into campus pins because neither establishes the location or share of model execution. The source is heavily US-focused; the plotted subset must not be interpreted as proof that most global workload is in the plotted states. Current fields reflect the source's retrieved snapshot rather than newly measured November 4 utilization.
