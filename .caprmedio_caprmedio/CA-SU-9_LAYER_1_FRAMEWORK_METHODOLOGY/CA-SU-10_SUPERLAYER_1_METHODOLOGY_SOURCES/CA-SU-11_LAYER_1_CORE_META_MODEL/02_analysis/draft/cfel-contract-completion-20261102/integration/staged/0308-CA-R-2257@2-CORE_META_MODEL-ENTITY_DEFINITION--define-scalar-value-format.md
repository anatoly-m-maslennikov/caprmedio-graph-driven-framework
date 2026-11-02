---
atom_id: CA-R-2257@2
current_scope_unit: CORE_META_MODEL
status: Archived
tier: 1
subjects:
  active: CFEL > Format/scalar
relations: {}
version: 2
updated_at: 2026-11-02 00:18:22 +0400
role: Requirement
form: Entity Definition
---
## Summary

Define scalar Value Format

## Claim

The scalar Value Format admits a direct primitive value, including string, numeric, Boolean, date/time and null values supported by the declared Carrier. Sequences and mappings remain carrier structures: sequence members are counted individually, while child mapping keys are not direct values of their parent. Specific value Formats can restrict this broad domain.

### Formal claim

```text
Format/scalar
```

## Details

C612 records the chosen general Format for unconstrained Result values. Producer-specific specifications govern their concrete result shape; no function or advanced condition syntax is introduced.
