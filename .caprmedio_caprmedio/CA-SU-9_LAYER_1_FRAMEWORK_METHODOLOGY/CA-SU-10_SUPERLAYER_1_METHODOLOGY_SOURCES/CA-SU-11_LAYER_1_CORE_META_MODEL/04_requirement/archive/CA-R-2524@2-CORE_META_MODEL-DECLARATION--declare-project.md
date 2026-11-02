---
atom_id: CA-R-2524@2
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
subjects:
  active: Project
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---

## Summary

Declare Project

## Claim

A Project uses CAPRMEDIO's MODEL.

```CFEL
Scope Unit/Project;
Scope Unit/Project//{:1};
Project >| (Container == yes);
Project// {:0}((IS_CONTAINED_BY)) Scope Unit//;
Project ((NARROWER_THAN)) @Scope Unit
```

## Semantics

A Project is the root Scope Unit.
