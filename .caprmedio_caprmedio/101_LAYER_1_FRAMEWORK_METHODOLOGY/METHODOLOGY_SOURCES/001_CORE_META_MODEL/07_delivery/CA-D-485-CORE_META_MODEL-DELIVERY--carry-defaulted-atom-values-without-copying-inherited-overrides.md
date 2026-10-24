---
subjects:
  governs: Atom Property Default
  depends_on:
  - Subject/Domain/Node/Continuant/Term//Property
  - Atom Property Default
  - Subject/Domain/Node/Continuant/Atom.Property
  - Autonomous Confidence Threshold
  - Subject/Domain/Node/Continuant/Project.Framework Settings.implementation.retry_limit
version: 10
updated_at: 2026-10-24 01:37:42 +0400
relations:
  relates_to:
  - CA-D-478
  - CA-D-472
  - CA-D-447
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
