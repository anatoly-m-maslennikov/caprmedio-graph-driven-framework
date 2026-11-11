---
atom_id: CA-R-2734
ref_id: CA-R-2734
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/Workflow/(.Purpose := Runtime)
tier: 3
status: Active
version: 3
updated_at: '2026-11-11 14:06:22 +0400'
---

## Summary

Declare Runtime Workflow

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Context.Role in (Operations))/Workflow.Purpose :: Runtime;
```

## Semantics

A Runtime Workflow is a Workflow whose Purpose is Runtime: it provides behavior through a Project's delivered result during its operation. In CAPRMEDIO, examples include Create Draft, Promote Draft and Archive Atom.

It inherits Workflow's shared Step, Substep and Action model. Purpose describes use relative to a Project and does not change the canonical definition's owning Scope Unit.
