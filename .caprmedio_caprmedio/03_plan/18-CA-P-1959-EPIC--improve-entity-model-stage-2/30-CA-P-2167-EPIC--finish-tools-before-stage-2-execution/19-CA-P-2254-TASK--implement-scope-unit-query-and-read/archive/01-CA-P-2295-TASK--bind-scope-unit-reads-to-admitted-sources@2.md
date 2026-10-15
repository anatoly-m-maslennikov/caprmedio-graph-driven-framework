---
atom_id: CA-P-2295
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Scope Unit, Workflow, Configuration, Plan]
version: 2
updated_at: "2026-10-13 20:49:49 +0400"
relations:
  is_decomposition_of: [CA-P-2254]
---
# Summary

Bind Scope Unit reads to admitted sources

## Objective

Bind the pure Scope Unit parser and selectors to the accepted Structure/Settings sources and existing receiving admission. Prove full independent Read, query frontier, missing/ambiguous/stale/denied behavior and zero effects. Reuse current schema authority rather than a guessed partial schema.

## Details

Estimated own work: 15 minutes. Split larger work into bounded children before execution. Inherit the parent Task's accepted contracts, current-source checks and authority boundaries. Internal helpers are not newly admitted Tools. Keep parsing, reading, writing and CLI responsibilities separate. The integration owner controls Plans and Git; parallel implementation owns disjoint files only.

### Definition of Done

The Plan is not Done until exact implementation/source pins, focused positive/refusal/no-op checks and an independent review establish this child's bounded outcome. Preparation alone, invented public bindings, source-policy changes, deferred publication or live Core migration do not satisfy it. Parent-wide and runtime completion remain separate.

### Concrete receiving continuation — 2026-10-13

Current D625/D626/D627/D527 and O211/O212 already define the logical map and receiving responsibilities. The missing work is production wiring, not a new map-authority decision. P2340 implements the actual private O212 receiver and P2341 independently tests genuine admission and source preservation. O211 Query and Atom O047/O046 are following bounded slices; this parent remains Active until complete Read/query receiving evidence exists.
