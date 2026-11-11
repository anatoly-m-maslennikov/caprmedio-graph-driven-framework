---
atom_id: CA-R-2257
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Format/scalar
version: 4
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 1
role: Requirement
form: Entity Definition
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2257-CORE_META_MODEL-ENTITY_DEFINITION--define-scalar-value-format.md
  source_atom_id: CA-R-2257
  source_atom_revision: 4
  source_sha256: 232102f2d7eb8688495aab45dce825fcb4e1985ce455b57478f8a6709fa3ef1f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define scalar Value Format

## Claim

The scalar Value Format admits a direct primitive value, including string,
numeric, Boolean, date/time and null values supported by the declared Carrier.
Sequences and mappings remain Carrier structures: sequence members are counted
individually, while child mapping keys are not direct values of their parent.
Specific Formats can restrict this broad domain.


```CFEL
CFEL <+ Format/scalar
```

## Details

C612 records the general Format for unconstrained Result values. Producer
specifications govern concrete result shapes; no function or advanced
condition syntax is introduced.
