---
atom_id: CA-P-1978
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Requirement, Method, Evaluation, Delivery, Operations, Plan, Operator]
version: 4
updated_at: "2026-10-11 00:08:45 +0400"
relations:
  is_decomposition_of: [CA-P-1959]
  blocks: [CA-P-1960]
---
# Summary

Review and update RMEDO for Subject Tools

## Objective

The Subject lookup and patch-preview Tools have reviewed, updated and independently verified RMEDO before contract compilation or implementation.

## Details

Own work: none. This composite Task completes through its bounded children.

Review the existing ATOM_SEARCH, ATOM_UPDATE, Subject migration planner and affected graph/parser/validator Tool contracts. Update their Requirements, Methods, Evaluations, Delivery and Operations in their declared Engine Tool Scope Units. Reuse existing definitions; do not create duplicate authority or a second Atom engine.

Cover field-aware governs/depends_on lookup, exact role/owner/lifecycle/source selection, source pins and diagnostics; explicit Subject-only patches, unrelated-byte preservation, stale-source checks, Version/time/history boundaries and sealed previews; independent checks, output/request carriers and repeatable operation steps.

This Task's write boundary is Tool-governing RMEDO only. Select declared Engine Tool Scope Units and their corresponding owning scope, not `current_scope_unit: CORE_META_MODEL`. Core entity-model Subjects, generic Subject grammar, the frozen candidate/review, Project Configuration, historical bodies and migration source effects are excluded. Any required generic grammar change stays under CA-P-1964's separate decision. Updating a Tool contract does not admit a new Core grammar, native relation or live writer.

Use MCP only for an actually supported advertised/admitted capability. Do not use it for unsupported operations. Use an already admitted local method within current authorization if available; otherwise stop and report the missing capability. Do not bypass sealed envelopes, approvals, pins or existing write guards.

Ask about a concrete unresolved decision below 90% confidence. Preserve Summary identities; classify repairs and use required revision/replacement rules. Keep meaningful constraints and require independent verification of the actual revised source packet before marking this Task Done.

Inherit CA-P-1959's confidence, preservation and execution boundaries. Creating this Plan records work; it does not execute or complete it.

### Decomposing Plans

- [CA-P-1979 — Review current Subject Tool RMEDO](01-CA-P-1978-TASK--review-and-update-rmedo-for-subject-tools/done/01-CA-P-1979-TASK--review-current-subject-tool-rmedo.md)
- [CA-P-1980 — Repair Subject Tool RMEDO](01-CA-P-1978-TASK--review-and-update-rmedo-for-subject-tools/done/02-CA-P-1980-TASK--repair-subject-tool-rmedo.md)
- [CA-P-1981 — Verify repaired Subject Tool RMEDO](01-CA-P-1978-TASK--review-and-update-rmedo-for-subject-tools/done/03-CA-P-1981-TASK--verify-repaired-subject-tool-rmedo.md)

### Definition of Done

The Plan is **not** Done if any applicable R/M/E/D/O contract is unreviewed or inconsistent; a confirmed gap is unaddressed; actual repaired sources lack independent current verification; a scope or unsupported-MCP boundary is violated; or Tool implementation starts before this gate passes; any direct decomposing Plan is not Done; or own work exceeds 15 minutes without decomposition.
