---
subjects:
  active: Atom
  passive:
  - Term//Property
  - Entity/Aspect/Engineering/Execution Control/Decision Confidence
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Implementation Retry Limit
version: 24
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-485
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
---
## Summary

Carry defaulted Atom values without copying inherited overrides

## Claim scope

defaulted Atom values and inherited external settings.

## Claim

a writer **must** preserve the distinction between a defaulted Atom Property **and** an inherited external setting:

- a required Atom value selected by applying a default is still carried at its canonical internal location; equality **to** that default does **not** permit omitting the value.
- an unselected optional override remains absent; do **not** copy an inherited effective setting into a locally selected override.
- retain an explicit override even **when** it currently equals the inherited value, because later upstream changes **must not** change that selection.
