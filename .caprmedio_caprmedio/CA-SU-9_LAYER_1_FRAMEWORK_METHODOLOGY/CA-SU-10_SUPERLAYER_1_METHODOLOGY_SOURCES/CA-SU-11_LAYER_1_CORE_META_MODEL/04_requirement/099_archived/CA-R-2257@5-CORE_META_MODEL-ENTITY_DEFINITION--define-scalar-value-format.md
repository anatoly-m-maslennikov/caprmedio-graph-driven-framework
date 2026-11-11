---
atom_id: CA-R-2257
ref_id: CA-R-2257@5
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Format/scalar
tier: 1
status: Archived
version: 5
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-R-2257@5-CORE_META_MODEL-ENTITY_DEFINITION--define-scalar-value-format.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define scalar Value Format

## Claim

### Prose Claim


The scalar Value Format admits a direct primitive value, including string,
numeric, Boolean, date/time and null values supported by the declared Carrier.
Sequences and mappings remain Carrier structures: sequence members are counted
individually, while child mapping keys are not direct values of their parent.
Specific Formats can restrict this broad domain.



### Formal Claim

```CFEL
# model
CFEL <+ Format/scalar
```

