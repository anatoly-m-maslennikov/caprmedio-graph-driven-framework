---
atom_id: CA-P-1985
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Requirement, Method, Evaluation, Delivery, Operations, Plan, Operator]
version: 1
updated_at: "2026-10-10 23:51:04 +0400"
relations:
  is_decomposition_of: [CA-P-1980]
---
# Summary

Repair Subject Tool Evaluations

## Objective

Specify independent checks for the two valid-file Subject operations.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. Required prerequisites: CA-P-1982, CA-P-1983.

Exclusive files: CA-E-301 and CA-E-304. Consume CA-P-1979 and the normalized metadata. Add field direction, literal exact and boundary-prefix, filters, false-positive, ordered occurrence/pin cases; exact pinned replacement, complete-file validation, stale/invalid/duplicate/path/symlink/no-op failures, byte and line-ending preservation, no-write preview and unchanged apply guard. Define fixtures independently of the producer. Do not create implementation/tests in this repair Task. Preserve Summary and increment each Version once. Output: revised Evaluation Atoms and pins.

Use the shared minimum contract in the CA-P-1979 review. A worker owns only the listed files; root owns integration, commits and Task completion. Recheck source pins after normalization. No unrelated changes, Core entity-model edits, source migration, runtime activation or release work. Ask for a concrete unresolved decision below 90% confidence. Decompose before exceeding 15 minutes.

### Definition of Done

The Plan is **not** Done if its stated output or exact before/after evidence is missing; a file outside its exclusive scope changes; preserved claims or identity are lost; the cross-role contract conflicts; checks fail; a prerequisite is incomplete; or own work exceeds 15 minutes without decomposition.
