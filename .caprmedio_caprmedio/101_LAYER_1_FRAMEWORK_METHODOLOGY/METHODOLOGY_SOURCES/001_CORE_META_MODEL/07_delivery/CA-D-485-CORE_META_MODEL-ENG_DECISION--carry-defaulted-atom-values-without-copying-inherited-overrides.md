---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Property
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Decision Confidence
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings.implementation.retry_limit
version: 18
updated_at: 2026-10-27 19:59:25 +0400
relations: {}
atom_id: CA-D-485
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary

Carry defaulted Atom values without copying inherited overrides

## Scope

defaulted Atom values and inherited external settings.

## Claim

a writer **must** preserve the distinction between a defaulted Atom Property **and** an inherited external setting:

- a required Atom value selected by applying a default is still carried at its canonical internal location; equality **to** that default does **not** permit omitting the value.
- an unselected optional override remains absent; do **not** copy an inherited effective setting into a locally selected override.
- retain an explicit override even **when** it currently equals the inherited value, because later upstream changes **must not** change that selection.

## Details
