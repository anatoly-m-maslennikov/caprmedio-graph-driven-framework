---
atom_id: CA-P-2327
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: Tool
  depends_on: [Atom, Plan, Configuration]
version: 2
updated_at: "2026-10-13 22:08:51 +0400"
relations:
  is_decomposition_of: [CA-P-2325]
---
# Summary

Align fourteen Done Plan placements

## Objective

Move the fourteen approved Done Plans beneath their explicitly carried parent Plans.

## Details

Estimated own work: up to 15 minutes; split further work before exceeding this bound. Root owns Git and tracking Plans. Concurrent workers own disjoint targets.

The exact target IDs are CA-P-1562, CA-P-1563, CA-P-1567, CA-P-1568, CA-P-1569, CA-P-1570, CA-P-1571, CA-P-1572, CA-P-1574, CA-P-1575, CA-P-1630, CA-P-1631, CA-P-1632 and CA-P-1633. Preserve filenames, Status, Summary, Subjects, relations and body; update Version +1 and Updated At, with exact predecessor archives. Resolve CA-P-1574 beneath the new CA-P-1568 location.

No live Core Subject/content migration, runtime activation or configuration publication is included.

### Reviewed placement correction

Independent review found one destination navigation collision: P1631's local 06 collided with P1123. The uncommitted replacement uses unused 40 in filename and work_sequence_number, without renumbering siblings. The exact original archive, Version 2, ID and body remain unchanged. The other thirteen filenames are unchanged. All fourteen placements and predecessor archives now pass independent review.

### Definition of Done

The Plan is not Done until the bounded outcome has actual evidence and independent acceptance, or if unrelated legacy sources were changed, history was lost, validation was bypassed or complete Project readiness was inferred.

### Completed bounded outcome — 2026-10-13

All fourteen approved Done Plan relocations, actual immediate parents, Version increments and exact archives passed the independent current audit.

Evidence: [bounded cleanup Task closure](../../../../../../../../_projection/core-entity-review/stage2/tools-first/bounded-cleanup-task-closure.md). Receiving integration, full-Project/runtime admission and deferred C/A migration remain separate.
