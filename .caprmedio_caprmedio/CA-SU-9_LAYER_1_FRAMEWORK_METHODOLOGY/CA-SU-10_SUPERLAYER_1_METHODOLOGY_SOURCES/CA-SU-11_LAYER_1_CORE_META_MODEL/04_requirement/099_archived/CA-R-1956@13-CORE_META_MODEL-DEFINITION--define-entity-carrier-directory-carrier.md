---
atom_id: CA-R-1956
ref_id: CA-R-1956@13
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier/Directory
tier: 3
relations:
  child_of:
  - CA-R-1174
status: archived
version: 13
updated_at: 2026-11-11 16:04:42 +0400
carrier_destination:
  file:
    name: CA-R-1956@13-CORE_META_MODEL-DEFINITION--define-entity-carrier-directory-carrier.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Entity/Carrier/Directory Carrier

## Claim

### Prose Claim

A Directory Carrier uses a directory to represent its carried Object; containing files alone does not make it a Directory Carrier.
### Formal Claim

```CFEL
# model
Carrier/Directory ((NARROWER_THAN)) Carrier;
```

