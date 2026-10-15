---
atom_id: CA-P-2249
content_role: Plan
type: Plan
label: Task
work_sequence_number: 14
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Scope Unit, Action, Workflow, Configuration, Revision, Journal, Plan, Operator]
version: 2
updated_at: "2026-10-13 01:43:29 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
  blocks: [CA-P-2251]
---
# Summary

Align Scope Unit Query and Read contracts

## Objective

Operation-specific Scope Unit Query and full Read contracts are independently accepted before their implementation.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. Split concrete work larger than this bound into actual bounded children before execution. The Operator authorizes this bounded contract-authoring packet and its separate independent acceptance now. No implementation, runtime activation or migration is authorized.

Author the missing bounded R/M/E/D/O refinements of the shared Connector Core API. Define explicit logical Scope Unit identity/query, allowed filters, actual state and optional pin/history behavior, empty/multiple/not-found results, authorization, stable errors and effect-free reads. CA-O-046/047 are Atom-only; CA-D-622 alone is not an admitted Scope Unit operation binding. Deliver exact current/predecessor pins to a different independent reviewer. A packet-ready handoff permits review while this author Task is Active; neither author assertions nor Task status substitute for accepted manifest.

The author does not independently accept this packet. A precise accepted/rejected source manifest from a different reviewer is required; resolve blocking findings and re-review changed pins before Done.

Deliver the exact changed or reviewed manifest and focused check results to the independent integration/verification owner. Preserve historical receipts. No database build, new transport, Atom deletion, automatic batch retry/resume or publication-concurrency mechanism is included.

### Definition of Done

The Plan is **not** Done if any required operation-specific source is absent, inconsistent or unpinned; exact history or a different reviewer's actual acceptance is missing; generic API readiness substitutes for the missing binding; or forbidden surfaces change. Own work must not exceed 15 minutes without prior decomposition.
