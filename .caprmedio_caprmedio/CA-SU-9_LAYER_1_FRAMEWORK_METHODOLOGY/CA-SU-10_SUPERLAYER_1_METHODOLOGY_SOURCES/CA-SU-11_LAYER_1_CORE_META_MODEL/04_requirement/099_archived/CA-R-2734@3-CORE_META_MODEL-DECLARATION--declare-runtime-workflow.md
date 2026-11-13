---
atom_id: CA-R-2734
ref_id: CA-R-2734@3
role: Requirement
form: Declaration
container:
  scope_unit: CA-SU-11
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/Workflow/(.Purpose
    := Runtime)
tier: 3
status: archived
version: 3
updated_at: 2026-11-11 14:06:22 +0400
destination:
  file:
    name: CA-R-2734@3-CORE_META_MODEL-DECLARATION--declare-runtime-workflow.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
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
