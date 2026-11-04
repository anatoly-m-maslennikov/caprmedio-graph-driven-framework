---
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Execution Control <+ Decision Confidence
  passive:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role: Plan)/(.Header.Form: Plan)'
  - CAPRMEDIO_MODEL <+ Term//Property
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
version: 32
updated_at: 2026-11-02 18:35:20 +0400
relations:
  child_of:
  - CA-R-1427@17
atom_id: CA-R-1428
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1428-CORE_META_MODEL--permit-confidence-threshold-defaults-and-overrides.md
  source_atom_id: CA-R-1428
  source_atom_revision: 32
  source_sha256: 4fd0a513d98f08920fbcfde8aacf54f9ecbc7f92fab2d2861d54471e0d566980
  original_relations_sha256: 78c49a17234bcda360b37449773c5ac549d056fc653111f6644e9b5c453d7e0b
---
## Summary

Permit confidence-threshold defaults and overrides

## Claim

### Prose Claim


the source of a Confidence Threshold value.


a Confidence Threshold **must** take its value from applicable direct Operator input, an explicit Property on the current Plan, the nearest enclosing Hub Plan with an explicit Property, **or** the Framework Instance Settings default; the Plan-containment chain follows `IS_CONTAINED_BY` toward the nearest enclosing Plan, **not** Label spelling.
