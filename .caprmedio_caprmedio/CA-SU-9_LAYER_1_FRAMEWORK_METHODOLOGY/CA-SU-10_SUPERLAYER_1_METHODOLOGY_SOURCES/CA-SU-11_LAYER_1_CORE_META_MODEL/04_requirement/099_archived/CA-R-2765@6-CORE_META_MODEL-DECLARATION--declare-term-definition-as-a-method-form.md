---
atom_id: CA-R-2765
ref_id: CA-R-2765@6
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Method)/(.Header.Context.Form
    := Term Definition)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Method)
tier: 3
status: archived
version: 6
updated_at: 2026-11-11 14:06:22 +0400
carrier_destination:
  file:
    name: CA-R-2765@6-CORE_META_MODEL-DECLARATION--declare-term-definition-as-a-method-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
---
## Summary

Declare Term Definition as a Method Form

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Context.Role in (Method)).Header.Context.Form :: Term Definition;
```
