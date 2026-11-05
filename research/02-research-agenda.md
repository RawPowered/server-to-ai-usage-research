# Next research phase: physical servers to AI usage

Status: planned research; no findings are claimed below. Start from the baseline report and ledger.

## Priorities and acceptance criteria

| Priority | Question | Evidence needed | Completion criterion |
|---|---|---|---|
| P0 | What is actually online at each company on one date? | Latest filings, earnings disclosures, site commissioning evidence | Every included phase has a dated operating-status record; uncertain phases remain separate |
| P0 | How much of Colossus is reserved for Anthropic, Google, other tenants, and internal models? | Latest primary cloud agreements, amendments, delivery/ramp disclosures | Reconcile the 220k site scope and 325k contract scope; verify Google allocation without treating press reports as delivery |
| P0 | Why do Epoch's SpaceXAI article and CSV differ? | Source changelog or model revision documentation | Identify revision cause or retain both values with unresolved status |
| P1 | Which assets back OpenAI's provider commitments? | Microsoft, AWS, Oracle/Stargate, CoreWeave disclosures | Map commitments to identifiable phases; leave undisclosed mappings empty |
| P1 | Which assets back Anthropic's supply? | AWS, Google/Broadcom, Azure, SpaceX and other providers | Separate existing deployments, ordered hardware, and future expansion |
| P1 | Is comparable utilization information public? | GPU-hours, energy metering, occupancy or workload disclosures | Define common interval and denominator; otherwise state utilization remains unknown |
| P2 | What changes when performance is normalized? | Chip-generation mix, memory, networking, precision and workload assumptions | Publish scenario ranges; no single chip-count or MW conversion presented as universal |

## Proposed tables

- `sites`: stable ID, location, aliases, owner and operator evidence.
- `deployments`: site/phase ID, observation date, chip generation, count, IT MW, status, source ID, uncertainty.
- `allocations`: deployment ID, tenant, interval, allocation unit/value, exclusivity, contract ID, delivered status.
- `contracts`: parties, signed date, ramp period, cap/option, superseded or included agreement IDs, source IDs.
- `claims`: one assertion per row, source locator, evidence class, observation period, analyst inference, confidence rationale.

## Publication gates

Recheck accessible source documents and record revisions; reconcile aliases and contract inclusions; label unknown tenant shares; validate unit/date consistency; publish lower-bound operating totals separately from estimates and planned builds. A shared provider does not establish a shared site. An unverified allocation must not enter a utilization percentage.

The next report should answer two separate questions: unique operational capacity by provider, and nonoverlapping allocated capacity by lab. Publish a ranking only where coverage and uncertainty justify it.
