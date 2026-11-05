---
atom_id: CA-R-2253
ref_id: CA-R-2253
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Format/string
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Format
version: 6
updated_at: 2026-11-03 23:25:51 +0400
tier: 1
role: Requirement
form: Declaration
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-2253-CORE_META_MODEL-DECLARATION--define-string-value-format.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Define string Value Format

## Claim

### Formal Claim

```CFEL
# model
CFEL <+ Format/string
```

### Prose Claim


The string Value Format admits textual string values. It does not turn null
into a string or set a property's cardinality, uniqueness, or carrier
representation.



## Semantics

string is the value domain selected by a `[string]` annotation on one direct
Property value.
