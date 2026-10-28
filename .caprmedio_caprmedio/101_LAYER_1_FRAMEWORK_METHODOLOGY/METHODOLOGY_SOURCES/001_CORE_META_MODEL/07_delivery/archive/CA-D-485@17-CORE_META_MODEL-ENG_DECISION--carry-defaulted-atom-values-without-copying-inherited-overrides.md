---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Term//Property
  - Subject/Graph Node/Engineering/Execution Control/Decision Confidence
  - Subject/Graph Node/Domain/Continuant/Project.Framework Settings.implementation.retry_limit
version: 17
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
atom_id: CA-D-485@17
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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
