---
atom_id: CA-R-2257
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CFEL <+ Format/scalar
version: 4
updated_at: 2026-11-02 07:52:54 +0400
relations: {}
tier: 1
role: Requirement
form: Entity Definition
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
