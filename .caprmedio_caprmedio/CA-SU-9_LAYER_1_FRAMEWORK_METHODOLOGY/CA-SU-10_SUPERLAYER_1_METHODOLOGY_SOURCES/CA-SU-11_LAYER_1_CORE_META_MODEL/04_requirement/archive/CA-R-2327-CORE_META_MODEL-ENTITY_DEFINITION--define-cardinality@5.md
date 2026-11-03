---
atom_id: CA-R-2327
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Cardinality
version: 5
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 1
role: Requirement
form: Entity Definition
---
## Summary

Define Cardinality

## Claim

### Formal Claim

```CFEL
CFEL <+ Cardinality
```

### Prose Claim


Cardinality is CFEL syntax for expressing the allowed number of direct values,
dependent Properties, Relation instances or contained parts.



The forms are `{:n}`, `{:n+}` and `{:n..m}` with non-negative integer bounds.

## Details

Source meaning: CA-R-1248@23 and CA-R-2244@1. Scope-specific constraints
remain in their governing Declarations.
