---
atom_id: CA-R-2735
ref_id: CA-R-2735
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Workflow/(.Purpose := Project)
tier: 3
status: Active
version: 1
updated_at: '2026-11-04 00:31:19 +0400'
---

## Summary

Declare Project Workflow

## Claim

### Formal Claim

```CFEL
Atom/(.Header.Role: Operations)/Workflow/(.Purpose := Project)
```

## Semantics

A Project Workflow is a Workflow whose Purpose is Project: it develops, validates, maintains or releases a Project's result. Examples include Implementation, Local Release and Public Release.

It inherits Workflow's shared Step, Substep and Action model. Purpose describes use relative to a Project and does not change the canonical definition's owning Scope Unit.
