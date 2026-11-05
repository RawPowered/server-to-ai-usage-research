# Definitions and accounting rules

## Measurement layers

| Layer | Question | Suitable evidence | Prohibited shortcut |
|---|---|---|---|
| Ownership/control | Who controls the accelerator stock? | Dated owner estimates, filings | Treat all delivered chips as online |
| Operation | Who runs the physical site? | Operator disclosures and site records | Assume tenant owns the campus |
| Allocation/access | Who may use the capacity? | Contract scope and delivery confirmations | Add tenant capacity to provider stock |
| Utilization | How much is actually busy over an interval? | Metering, accelerator-hours, workload telemetry | Equate nameplate capacity with activity |
| Distribution | Who sells model access? | Product availability announcements | Infer training location |

These are project accounting definitions. Epoch's distinct owner/user boundaries are documented in [S01](https://epoch.ai/data/ai-chip-owners) and [S14](https://epoch.ai/data/ai-chip-users-documentation/methodology).

## Evidence policy

Every numerical record needs a source ID, unit, observation period, status, and scope. Keep publication/update and retrieval dates separately. Prefer company filings for contract terms and technical deployments, and primary research for independent estimates. A company announcement is high-confidence evidence of the announcement, not independent verification that the promised system is operating.

Record source disagreement explicitly. Do not average incompatible dates or scopes. Keep unknowns empty, never zero. Do not infer absence of a relationship from an empty cell. Parent-company and lab figures require distinct entity IDs.

## Units and aggregation

- H100e: source-modeled accelerator capability, sensitive to chip and workload assumptions.
- GPU/chip count: physical units; generations are not interchangeable.
- IT MW/GW: computing-system power capacity; 1 GW = 1,000 MW. Facility power may also include cooling and other overhead.
- MWh/GWh: energy over time; not capacity.
- USD: investment or contract value; no automatic conversion into chips, watts, or utilization.

Only aggregate measurements with compatible units, dates, coverage, and status. For component medians, label their sum as a derived sum rather than a joint median; do not add confidence bounds as though they were a valid aggregate interval.

## Deduplication procedure for the next phase

1. Create a stable site ID, then a separate cluster/phase ID; aliases point to these IDs.
2. Store physical capacity once per site/phase/date/unit/status.
3. Link owner, operator, tenant, financier, and model distributor as separate roles.
4. Store tenant allocations as edges into the physical asset, not additional assets.
5. Link later contracts and expansions to earlier scopes; explicitly mark replacement, inclusion, or uncertainty.
6. Sum unique operating assets for physical totals. Sum each tenant's nonoverlapping allocations for usage-access totals. Do not mix the two totals.

Potential metrics, once denominators exist: customer dependence on provider = allocated provider capacity / total customer allocation; provider exposure to customer = allocated customer capacity / total provider capacity. Both require the same unit and date. Neither is currently computed in this repository.

Validation checks establish internal consistency, not independent truth of external disclosures. This is a selected-source baseline; it is not an exhaustive literature review.
