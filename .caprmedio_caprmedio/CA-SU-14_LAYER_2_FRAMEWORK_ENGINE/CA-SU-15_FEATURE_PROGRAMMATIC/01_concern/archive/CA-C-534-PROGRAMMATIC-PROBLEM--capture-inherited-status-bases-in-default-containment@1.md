---
atom_id: CA-C-534
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
  concern_about: [CA-P-2443, CA-R-1539, CA-D-461]
version: 1
updated_at: "2026-10-20T13:02:28.725Z"
---
# Summary

Capture inherited Status bases in default containment

## Concern

The default containment/reference binding path omits the Atom.Status base when composing inherited Role Status declarations. A supplied captured index works, but callers such as contained_atom_targets._bindings do not supply one.

## Evidences

The full frozen validator run executed530 tests and failed20 Plan prerequisite cases at _frontier_status_folders: inheritance requires one current Atom.Status declaration. The call chain is contained_atom_targets._bindings -> _frontier_status_folders(context, plans) -> declarations_from_sources(finite frontier rows), which contains inherited R1539 but no base. This is a current code-path defect exposed by frozen fixtures, not a claim that20 separate production requests failed. P2443 reuses canonical captured authority; missing/ambiguous bases must still refuse.

## Blast radius

Default contained Plan operations and prerequisite checks cannot prove their Status mapping. Keep imagefreeze blocked until this path and the complete frozen suite pass. No production endpoint call or historical replay occurred.
