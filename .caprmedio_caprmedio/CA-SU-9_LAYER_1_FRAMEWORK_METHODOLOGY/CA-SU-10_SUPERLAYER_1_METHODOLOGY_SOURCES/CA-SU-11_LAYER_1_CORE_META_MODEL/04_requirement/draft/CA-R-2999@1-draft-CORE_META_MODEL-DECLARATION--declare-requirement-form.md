---
atom_id: CA-R-2999
ref_id: CA-R-2999@1-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Form := Requirement)
tier: 3
status: Draft
version: 1
updated_at: "2026-11-07 14:23:30 +0400"
carrier_destination:
  file:
    name: CA-R-2999@1-draft-CORE_META_MODEL-DECLARATION--declare-requirement-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---

## Summary

Declare Requirement Form

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Form := Requirement);

# instances
Atom/(.Header.Form := Requirement)//$requirement.Header.Role:: [in (Requirement)]{::1}
```

## Semantics

A Requirement Form states a local required outcome, behavior, property or constraint.
