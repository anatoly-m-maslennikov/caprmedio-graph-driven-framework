---
atom_id: CA-R-2543
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Aspect
version: 4
updated_at: 2026-11-02 18:21:51 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Declare Aspect

## Claim

```CFEL
Aspect;
Aspect ((NARROWER_THAN)) @Node
```

- MODEL declares the generic Aspect.
- All concrete Aspects are instances in the applicable PROJECT STRUCTURE tree.

## Semantics

An Aspect is a topic through which an Atom addresses its Subject.
