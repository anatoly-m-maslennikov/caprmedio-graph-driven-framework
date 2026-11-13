---
identity:
  id: CA-R-2689
  ref_id: CA-R-2689@4
context:
  container:
    scope_unit: CA-SU-11
  role: requirement
  form: rule
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Scope Unit
    dependencies:
    - CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_CONTAINED_BY
  tier: 2
state:
  status: archived
  version: 4
  updated_at: '2026-11-11T16:37:55+04:00'
destination:
  file:
    name: CA-R-2689@4-CORE_META_MODEL-RULE--derive-scope-unit-ancestry-from-declarations.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
---


## Summary

Derive Scope Unit ancestry from Declarations

## Claim

### Prose Claim

Scope Unit ancestry follows the Scope Unit Declarations and their direct `IS_CONTAINED_BY` Relations. Resolve conflicting or missing parent declarations before deriving ancestry.
