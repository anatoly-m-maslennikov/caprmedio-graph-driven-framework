---
atom_id: CA-P-2297
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
version: 1
updated_at: "2026-10-13 04:30:00 +0400"
relations:
  is_decomposition_of: [CA-P-2256]
---
# Summary

Bind TOML modifications to receiving schemas

## Objective

Bind prepared TOML edits to the existing receiving schema, currentness and permission context. Prove exact item/full-set edits and no-op/refusal behavior. Do not invent a public encoding for typed TOML values or treat a configurable codec as implemented schema authority. Changed writes await an admitted publication path.

## Details

Estimated own work: 15 minutes. Split larger work into bounded children before execution. Inherit the parent Task's accepted contracts, current-source checks and authority boundaries. Internal helpers are not newly admitted Tools. Keep parsing, reading, writing and CLI responsibilities separate. The integration owner controls Plans and Git; parallel implementation owns disjoint files only.

### Definition of Done

The Plan is not Done until exact implementation/source pins, focused positive/refusal/no-op checks and an independent review establish this child's bounded outcome. Preparation alone, invented public bindings, source-policy changes, deferred publication or live Core migration do not satisfy it. Parent-wide and runtime completion remain separate.
