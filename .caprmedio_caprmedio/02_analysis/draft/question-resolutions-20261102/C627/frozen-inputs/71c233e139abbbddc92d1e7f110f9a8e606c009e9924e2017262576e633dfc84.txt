---
atom_id: CA-R-2465
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Atom/(.Role := Operations)/Step
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---

## Summary

Declare Step

## Claim

```CFEL
Atom/(.Role: Operations)/Step;
Step//{:1}((IS_CONTAINED_BY)) Workflow//;
((Step//{:1+}((CONTAINS)) Substep//)
AND (Step//{:0}((RUN)) Action//))
OR
((Step//{:0}((CONTAINS)) Substep//)
AND (Step//{:1}((RUN)) Action//))
```

## Semantics

A Step is a unit of work within a Workflow. It runs an Action or contains Substeps.
