# Server-to-AI usage research

Evidence cutoff: **November 4, 2026 (America/Chicago)**. Initial research installment.

Research question: who owns, operates, and uses the most AI compute across Amazon, Google, Microsoft, OpenAI, Anthropic, and SpaceX Super Intelligence (SpaceXSI / formerly xAI), and where do their figures overlap?

Start with the [research report](research/01-compute-ownership-usage-and-overlap.md). The evidence supports dated comparisons, not a live six-company utilization ranking.

## Contents

- [Report and conclusions](research/01-compute-ownership-usage-and-overlap.md)
- [Definitions and accounting rules](research/methodology.md)
- [Next research phase](research/02-research-agenda.md)
- [Sources and evidence locations](sources/README.md) and [structured register](sources/registry.json)
- [Ownership components](data/ownership_components_2025.csv) and [derived comparison](data/ownership_comparison_2025.csv)
- [Lab usage estimates and uncertainty](data/lab_usage_2025.csv)
- [Provider/customer overlap ledger](data/relationships.csv)
- [Selected current site capacities](data/site_capacity_2026-11.csv)
- [Retrieval provenance](sources/retrieval_manifest.json)
- [Validation script](scripts/validate.py)

## Reading the evidence

Observation date, publication date, and retrieval date are separate. An announced contract is not proof of delivery. Installed capacity is not measured utilization. Model distribution is not proof of a training deployment. The ledger records relationships, not disjoint pools that can be summed.

The owner table is a derived sum of chip-family medians, not a jointly modeled median. It retains the historical source label `xAI`. The user dataset uses `SpaceXAI` retrospectively. OpenAI and Anthropic are omitted from numeric owner rankings because their owned stock is not quantified here; missing values do not mean zero.

## Reproduction

Run `python scripts/validate.py` with Python 3.10 or later. No extra packages are required. It checks the local evidence tables, source references, and derivations without network access. Upstream CSV URLs and full-download hashes are in the retrieval manifest; only the selected rows/fields are preserved here. Those hashes identify the downloaded upstream versions but cannot reconstruct them.

Epoch-derived data is attributed to Epoch AI; see the source register for licensing. This repository does not reproduce full company articles or filings.
