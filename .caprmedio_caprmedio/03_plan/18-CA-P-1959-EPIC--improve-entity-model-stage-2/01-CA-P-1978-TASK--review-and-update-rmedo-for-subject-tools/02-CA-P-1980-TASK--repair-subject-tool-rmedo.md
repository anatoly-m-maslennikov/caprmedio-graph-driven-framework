---
atom_id: CA-P-1980
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Requirement, Method, Evaluation, Delivery, Operations, Plan, Operator]
version: 1
updated_at: "2026-10-10 23:34:31 +0400"
relations:
  is_decomposition_of: [CA-P-1978]
  blocks: [CA-P-1981]
---
# Summary

Repair Subject Tool RMEDO

## Objective

Repair confirmed Subject Tool RMEDO gaps in the declared Tool authority without changing the Core entity-model corpus.

## Details

Own work: none. Required prerequisite: CA-P-1979. CA-P-1982 prepares bounded repair children; preparation alone does not complete this Task.

Create and execute disjoint, at-most-15-minute child Tasks for the confirmed Requirement, Method, Evaluation, Delivery and Operations repairs. Preserve existing meanings, ownership and identity/revision rules. R specifies required outcomes; M specifies authoring/implementation method; E specifies independent checks and failures; D specifies safe inputs/outputs/source carriers; O specifies repeatable operation steps.

Reconcile matching contracts across all five roles. Define explicit Subjects fields and RMEDO role filters, byte preservation, stale-pin rejection and preview-only/authorized-apply boundaries. Keep proposed versus admitted grammar profiles distinct. No Tool contract grants a live effect outside its separate approval.

Only Tool-governing RMEDO is editable. Generic Core grammar/corpus Subjects, ordinary Core content, candidate history, runtime/MCP delivery and implementation are excluded. Unsupported MCP is not used; local work requires an admitted authorized method and preserves every write/approval guard.

Output: actual repaired authoritative Tool Atoms, before/after pins, truthful change records and a coherent packet for CA-P-1981. Resolve concrete confidence below 90% before deciding.

Inherit CA-P-1959's confidence, preservation and execution boundaries. Creating this Plan records work; it does not execute or complete it.

### Decomposing Plans

- [CA-P-1982 — Prepare bounded Tool RMEDO repair Tasks](02-CA-P-1980-TASK--repair-subject-tool-rmedo/01-CA-P-1982-TASK--prepare-bounded-tool-rmedo-repair-tasks.md)

### Definition of Done

The Plan is **not** Done if a confirmed gap remains unaddressed; bounded effect children do not exist or are incomplete; cross-role contracts conflict; actual repaired sources/pins are missing; or an excluded source/effect is changed; any direct decomposing Plan is not Done; or own work exceeds 15 minutes without decomposition.
