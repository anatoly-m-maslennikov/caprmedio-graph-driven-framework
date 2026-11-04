---
atom_id: CA-R-2734
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Workflow/(.Purpose := Runtime)
version: 1
updated_at: '2026-11-04 00:31:19 +0400'
relations: {}
tier: 3
role: Requirement
form: Declaration
---

## Summary

Declare Runtime Workflow

## Claim

### Formal Claim

```CFEL
Atom/(.Header.Role: Operations)/Workflow/(.Purpose := Runtime)
```

## Semantics

A Runtime Workflow is a Workflow whose Purpose is Runtime: it provides behavior through a Project's delivered result during its operation. In CAPRMEDIO, examples include Create Draft, Promote Draft and Archive Atom.

It inherits Workflow's shared Step, Substep and Action model. Purpose describes use relative to a Project and does not change the canonical definition's owning Scope Unit.
