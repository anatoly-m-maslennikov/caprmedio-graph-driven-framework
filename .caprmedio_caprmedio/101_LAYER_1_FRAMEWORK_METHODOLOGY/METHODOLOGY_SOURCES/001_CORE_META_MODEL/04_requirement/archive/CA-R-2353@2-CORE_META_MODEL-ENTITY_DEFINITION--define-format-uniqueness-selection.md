---
atom_id: CA-R-2353@2
current_scope_unit: CORE_META_MODEL
status: Archived
tier: 1
subjects:
  active: CFEL > Format.Uniqueness Selection
relations: {}
version: 2
updated_at: 2026-11-02 00:18:22 +0400
claim_target_scope_unit: CORE_META_MODEL
role: Requirement
form: Entity Definition
---
## Summary

Define Format Uniqueness Selection

## Claim scope

Optional comparison-population selection in a Value Format.

## Claim

A Format Uniqueness Selection identifies the comparison population for a property uniqueness check; it is optional and does not itself impose uniqueness or define a notation.

### Formal claim

```text
Format.Uniqueness Selection[string]{0..1}
```

## Details

Source meaning: CA-R-2248. Scope-specific constraints remain in their governing Rs.
