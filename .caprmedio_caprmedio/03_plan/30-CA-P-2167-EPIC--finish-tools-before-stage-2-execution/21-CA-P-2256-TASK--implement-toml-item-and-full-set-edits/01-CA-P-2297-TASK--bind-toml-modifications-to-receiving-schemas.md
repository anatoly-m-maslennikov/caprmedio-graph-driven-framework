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
version: 2
updated_at: "2026-10-22 22:06:00 +0400"
relations:
  is_decomposition_of: [CA-P-2256]
---
# Summary

Bind TOML modifications to receiving schemas

## Objective

Bind the prepared private TOML edits to the existing receiving schema, currentness and permission context. Prove exact item/full-set edits and no-op/refusal behavior without inventing a public typed-value encoding.

## Details

This remains the independent receiving/publication boundary for the TOML branch. Consume the bounded private materializer and writer evidence from CA-P-2256 and the completed CA-P-2307 selection packet, then establish exact current-source, schema, permission, effect and readback behavior with an independent review. Changed writes still await an admitted publication path.

Candidate #7 direct methodology edits do not wait for this Tool work, and this Plan does not authorize live configuration writes, runtime activation, Core migration or public publication. Internal helpers remain implementation details; parsing, reading, writing and CLI responsibilities stay distinct.

### Definition of Done

Keep this Plan Active until exact implementation/source pins, focused positive/refusal/no-op/error/effect checks and independent review establish the bounded receiving outcome. Preparation, a dependency selection, an invented public binding, deferred publication or live Core migration does not satisfy this Plan.
