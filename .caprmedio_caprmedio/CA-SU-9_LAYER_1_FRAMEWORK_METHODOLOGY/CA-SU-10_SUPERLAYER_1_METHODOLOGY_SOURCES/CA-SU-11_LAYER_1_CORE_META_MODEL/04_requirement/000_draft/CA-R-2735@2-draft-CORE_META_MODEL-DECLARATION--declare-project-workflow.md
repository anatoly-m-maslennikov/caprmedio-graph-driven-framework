---
atom_id: CA-R-2735
ref_id: CA-R-2735@2-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/Workflow/(.Purpose := Project)
tier: 3
status: Draft
version: 2
updated_at: '2026-11-11 14:06:22 +0400'
carrier_destination:
  file:
    name: CA-R-2735@2-draft-DECLARATION--declare-project-workflow.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---

## Summary

Declare Project Workflow

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Context.Role in (Operations))/Workflow.Purpose :: Project;

Atom/(.Header.Context.Role in (Operations))/Workflow/(.Purpose in (Project))
```

## Semantics

A Project Workflow develops, validates, maintains or releases a Project’s result.
