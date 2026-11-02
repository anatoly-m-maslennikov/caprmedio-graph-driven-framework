---
subjects:
  governs: Entity/Aspect/Engineering/Execution Control/Decision Confidence
  depends_on:
  - Entity/Object/Continuant/Actor/Operator
  - 'Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Plan)/(.Type: Plan)'
  - Entity/Term//Property
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
version: 29
updated_at: 2026-10-30 16:33:38 +0400
relations:
  child_of:
  - CA-R-1427
atom_id: CA-R-1428@29
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
## Summary

Permit confidence-threshold defaults and overrides

## Claim scope

the source of a Confidence Threshold value.

## Claim

a Confidence Threshold **must** take its value from applicable direct Operator input, an explicit Property on the current Plan, the nearest enclosing Hub Plan with an explicit Property, **or** the Framework Instance Settings default; the Plan-containment chain follows `IS_CONTAINED_BY` toward the nearest enclosing Plan, **not** Label spelling.
