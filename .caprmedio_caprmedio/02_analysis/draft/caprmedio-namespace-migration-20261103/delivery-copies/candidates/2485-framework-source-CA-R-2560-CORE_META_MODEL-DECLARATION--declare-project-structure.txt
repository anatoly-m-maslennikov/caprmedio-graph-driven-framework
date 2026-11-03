---
atom_id: CA-R-2560
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ PROJECT STRUCTURE
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---

## Summary

Declare PROJECT STRUCTURE

## Claim

```CFEL
PROJECT STRUCTURE {:0}((IS_PROPERTY_OF));
PROJECT STRUCTURE >| (Container == yes);
PROJECT STRUCTURE ((NARROWER_THAN)) @Node
```

## Semantics

PROJECT STRUCTURE describes the actual structure of a Project, including its Scope Units, Aspects, and other declared components.
