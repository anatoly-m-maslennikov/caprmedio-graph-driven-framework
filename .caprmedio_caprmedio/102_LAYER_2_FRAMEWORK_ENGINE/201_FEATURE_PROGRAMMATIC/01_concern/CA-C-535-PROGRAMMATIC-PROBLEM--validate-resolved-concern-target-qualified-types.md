---
atom_id: CA-C-535
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
priority: high
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  concern_about: [CA-P-2442, CA-R-1022]
version: 1
updated_at: "2026-10-20T13:02:28.725Z"
---
# Summary

Validate resolved Concern target qualified Types

## Concern

Concern target admission checks carried identity, Role, Version and admitted Status, but a generic Role Status fallback alone does not prove the target qualified Type is admitted.

## Evidences

Independent review found check_graph_extended target admission did not call the existing shared source-bound schema Role/Type validator. A role-bearing target with an unknown Type can therefore pass that mechanical slice. The literal Type label Revision is not itself a standalone entity; no arbitrary string ban is warranted. P2442 reuses the existing qualified Type schema and preserves extension uncertainty and ordinary RMED Type omission.

## Blast radius

Only valid Current Atom targets are eligible under R1022v17. Invalid/unresolved Type declarations must remain failures/gaps rather than being admitted by generic Status membership. Do not invent missing Type contributions or semantic validation; retain explicit unsupported schema cases.
