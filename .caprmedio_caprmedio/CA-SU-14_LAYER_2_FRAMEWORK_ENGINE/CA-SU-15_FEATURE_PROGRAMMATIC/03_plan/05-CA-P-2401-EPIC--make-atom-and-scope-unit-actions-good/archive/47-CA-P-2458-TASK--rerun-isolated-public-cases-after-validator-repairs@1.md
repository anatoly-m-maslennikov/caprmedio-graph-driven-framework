---
atom_id: CA-P-2458
content_role: Plan
type: Plan
label: Task
work_sequence_number: 47
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Backlog
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: [CA-P-2457]
relations:
  is_decomposition_of: [CA-P-2401]
version: 1
updated_at: "2026-10-20T15:10:43.000Z"
---
# Summary

Rerun the isolated public cases after validator repairs

## Objective

Run the three selected isolated public cases against the exact fresh candidate from CA-P-2457 and require protected production equality before any release retry.

## Details

Start only after CA-P-2457 supplies fresh immutable source/image identity and a passing production guard. Bind the isolated harness to that exact candidate and execute all three public cases, recording actual outcomes, canonical bytes and `production_equal: true`. Do not fall back to a prior candidate, replay either historical attempt, test production or treat host-only repair checks as this gate.

At most15minutes ownwork, split before extending. Preserve project, port, state namespace, receipt and rollback identity. No deployment, public release or full-local-release action is authorized by this Task.

### Definition of Done

A fresh receipt records all three isolated public cases, exact candidate provenance, zero unexpected failures/errors/skips and protected production equality. Only that passing receipt unlocks CA-P-2459; no deployment or release completion is inferred.
