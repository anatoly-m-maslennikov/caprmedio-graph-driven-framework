---
atom_id: CA-R-2257@1
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: Entity/Graph Syntax > Format/scalar
relations: {}
version: 1
updated_at: 2026-10-29 09:06:21 +0400
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
