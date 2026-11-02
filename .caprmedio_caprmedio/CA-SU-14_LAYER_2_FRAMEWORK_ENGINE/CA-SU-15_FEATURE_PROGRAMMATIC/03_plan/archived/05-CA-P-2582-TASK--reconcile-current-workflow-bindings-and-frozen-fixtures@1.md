---
atom_id: CA-P-2582@1
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Backlog
version: 1
updated_at: "2026-10-22T09:30:58Z"
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2577]
  depends_on: [CA-P-2578, CA-P-2580, CA-P-2581]
  relates_to: [CA-O-016, CA-O-230, CA-E-652]
---
# Summary

Reconcile current Workflow bindings and frozen fixtures

## Objective

Reconcile stale R1843 and related source inventory plus the existing implementation route only after native support exists. Preserve completed/blocked terminals and the old frozen oracle; deliver a separate self-contained current-graph fixture.

## Details

One Task per file; at most 15 minutes of own work per leaf. Split before expanding. Review and update dependent Tasks after observed predecessor results, before execution. Initiative is CA-P-2577; preserve one stable action identity for each actual mutation. Use current PROGRAMMATIC M/E/D guidance and the selected locked uv environment. Preserve unrelated dirty work, exact predecessors, canonical ownership, partial results, failure visibility, retry/permission bounds and business-only Journal semantics. Create C/Problem or C/Question for actual blockers or unresolved decisions. No release, deployment, production MCP traffic, full-suite run, uncertain replay or Git publication is authorized by this Task.

### Definition of Done

Retain the bounded changed paths, current source bindings, focused commands/results and unresolved limits for this responsibility; review and update the next dependent Task before it executes.
