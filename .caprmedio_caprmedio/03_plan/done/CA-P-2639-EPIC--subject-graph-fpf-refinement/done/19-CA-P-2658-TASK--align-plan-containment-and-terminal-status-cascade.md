---
atom_id: CA-P-2658
content_role: Plan
type: Plan
label: Task
work_sequence_number: 19
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Done
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
version: 1
updated_at: 2026-10-26 17:56:09 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2639
tier: 4
---
# Summary

Align Plan containment and terminal-status cascade

## Objective

Replace the retired Plan-decomposition family with child-owned IS_CONTAINED_BY and derived CONTAINS, while applying the accepted Done/Canceled cascade and preserving independent Plan completion, blocking and placement rules.

## Details

- Bound the source batch to the 33 rows in .caprmedio_tmp/subject-alignment-accepted/plans.json: 27 updates and six retirements, including the legacy decomposition family and its evaluation.
- Use only child-owned IS_CONTAINED_BY with derived CONTAINS. Do not introduce special decomposition relations, authored inverse lists, transitive authored closure, or folder-derived links; keep BLOCKS independent.
- For a parent Plan requested Done or Canceled, preserve every selected latest contained child already Done or Canceled, request Canceled for every other selected latest contained child through the existing cascade, and require every selected latest child to be Done or Canceled afterward. Mixed terminal statuses are allowed; no child is forced to match the parent's requested status.
- Apply the parent's own work and Definition of Done only to the Done case. Preserve standalone Plans, status authority, carrier placement, confidence/precedence rules, blocking, and no-inference-from-folder behavior.
- Coordinate the second O127 update in the bounded plan batch. Do not add statuses, redesign lifecycle authority, migrate unrelated history, or perform code/runtime/release work.

### Completion evidence

The accepted source correction is applied. Independent final verification passed.
Evidence: `.caprmedio_tmp/subject-alignment-accepted/verify.final.json`,
`verify.final.md`, both publication receipts, and
`graph-final/graph.subject-views.manifest.json`. The four Current-RMEDO views
contain 2,223 sources (792 Core, 405 Methodology, 1,026 Engine), with zero
unmapped Subjects. This is source/projection verification, not runtime execution.

## Definition of Done

- The retired decomposition definitions and evaluation have an explicit retirement disposition and no active consumer still requires that relation family.
- Updated consumers use child-owned IS_CONTAINED_BY and derive CONTAINS without authored inverse or special decomposition behavior.
- Done/Canceled cascades preserve already-terminal children, cancel unfinished children, allow mixed terminal results, and require all selected children to be terminal afterward.
- Parent own work and DoD are required only for Done; independent BLOCKS, placement and status meanings remain intact.
- Actual source effects and bounded verification are recorded without claiming the phase is complete before Root's integration checks.
