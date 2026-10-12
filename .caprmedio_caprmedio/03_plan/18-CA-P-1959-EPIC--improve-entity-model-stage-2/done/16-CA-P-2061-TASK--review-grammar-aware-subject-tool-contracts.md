---
atom_id: CA-P-2061
content_role: Plan
type: Plan
label: Task
work_sequence_number: 16
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Term, Tool, Plan, Projection]
version: 2
updated_at: "2026-10-11 04:19:02 +0400"
relations:
  is_decomposition_of: [CA-P-1959]
  blocks: [CA-P-1965]
---
# Summary

Review grammar-aware Subject Tool contracts

## Objective

Identify the exact governing contracts and implementation changes needed for the approved Subject grammar before changing code.

## Details

Estimated own work: 15 minutes. CA-P-2059 has adopted the five approved Core grammar definitions. Recheck their current pins and the twelve accepted Engine Tool contracts. Review graph parsing, lookup, Subject-only preview and the finite complete-carrier validator in independent read-only lanes.

Produce `_projection/core-entity-review/stage2/grammar-tools.review.md` with current authority/implementation pins, minimal contract deltas, explicit legacy/approved profile selection, disjoint edit scopes and independent acceptance cases. No selectors, native slash Relation, repair engine, migration, runtime activation, MCP or FPF. Current Subjects and frozen review outputs stay unchanged. Any required Engine Tool RMEDO authoring is separate bounded work before implementation; no ordinary Core body change is authorized here.

### Definition of Done

Not Done if any required surface is omitted, source or implementation pins are stale, old Subjects can be silently reinterpreted, native graph admission is implied, unsupported authority is hidden, or own work exceeds 15 minutes without decomposition.

### Completion

Four independent audits and the consolidated boundary review completed. Twelve accepted Tool source pins and seven implementation pins match current bytes. Nine current lookup tests and ten current preview tests passed. The review identifies ten required Tool-RMEDO revisions before implementation; two delivery-location atoms remain unchanged. Both profiles reject @, preview envelope keys are closed, and syntax/direction does not claim native endpoint admission. Evidence: `_projection/core-entity-review/stage2/grammar-tools.review.md` and `task-2061.receipt.json`. No source or code was edited by this Task.
