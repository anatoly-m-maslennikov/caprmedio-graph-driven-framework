---
atom_id: CA-R-1259
ref_id: CA-R-1259
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Property
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//HAS_PROPERTY
tier: 2
status: Active
version: 24
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1259-CORE_META_MODEL-RULE--permit-zero-or-more-properties-on-every-entity.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Permit Zero or More Properties on Every Entity

## Claim

### Prose Claim


Property occurrences borne by every Entity.


**every** Entity **may** bear **`>=0`** Property occurrences.


```text
Entity {:0+}((HAS_PROPERTY)){:1} Property
```
