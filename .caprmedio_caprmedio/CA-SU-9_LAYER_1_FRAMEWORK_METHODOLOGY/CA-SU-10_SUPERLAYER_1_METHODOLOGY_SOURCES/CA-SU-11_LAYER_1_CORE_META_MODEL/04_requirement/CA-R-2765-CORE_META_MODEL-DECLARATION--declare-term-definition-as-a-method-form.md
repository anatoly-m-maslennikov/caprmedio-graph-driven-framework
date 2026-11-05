---
atom_id: CA-R-2765
ref_id: CA-R-2765
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Method)/(.Header.Form := Term Definition)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Method)
tier: 3
role: Requirement
form: Declaration
version: 5
updated_at: 2026-11-04 23:07:00 +0400
carrier_destination:
  file:
    name: CA-R-2765-DECLARATION--declare-term-definition-as-a-method-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
container:
  scope_unit: CA-SU-11
---
## Summary

Declare Term Definition as a Method Form

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Role := Method).Header.Form: Term Definition;
Atom/(.Header.Role := Method)/(.Header.Form := Term Definition)
```
