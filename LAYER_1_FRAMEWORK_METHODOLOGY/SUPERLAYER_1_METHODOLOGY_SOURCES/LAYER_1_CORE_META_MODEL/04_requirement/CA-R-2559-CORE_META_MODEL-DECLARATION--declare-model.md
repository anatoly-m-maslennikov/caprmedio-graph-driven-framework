---
atom_id: CA-R-2559
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---

## Summary

Declare MODEL

## Claim

### Formal Claim

```CFEL
# model
MODEL {:0}((IS_PROPERTY_OF));

MODEL >| (Container == yes);

MODEL ((NARROWER_THAN)) Node
```

### Prose Claim



- A local MODEL inherits CAPRMEDIO's MODEL.
- MODEL inheritance is distinct from Node narrowing.
- Local overrides replace matching inherited rules in the local MODEL.
- Local overrides preserve the base MODEL's rules.
- Unmodified inherited Declarations are reused.

## Semantics

MODEL declares Node kinds, Relations, Properties, and rules.
