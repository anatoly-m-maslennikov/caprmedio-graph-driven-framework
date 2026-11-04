---
atom_id: CA-R-2765
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Method)/(.Header.Form := Term Definition)
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Method)
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 3
role: Requirement
form: Declaration
version: 3
updated_at: 2026-11-04 18:28:33 +0400
carrier_destination:
  file:
    name: CA-R-2765-CORE_META_MODEL-DECLARATION--declare-term-definition-as-a-method-form.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Term Definition as a Method Form

## Claim

### Formal Claim

```CFEL
# model
Atom/(.Header.Role: Method).Header.Form: Term Definition;
Atom/(.Header.Role: Method)/(.Header.Form: Term Definition)
```
