---
atom_id: CA-R-2698
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Relations.IS_CONTAINED_BY
version: 2
updated_at: 2026-11-04 07:31:50 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2698-CORE_META_MODEL-DECLARATION--declare-atom-header-relations-is-contained-by.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
container:
  scope_unit: CA-SU-11
---
## Summary

Declare Atom.Header.Relations.IS_CONTAINED_BY

## Claim

### Formal Claim

```CFEL
# model
Atom.Header.Relations.IS_CONTAINED_BY{::1}:: []{::0};

Atom.Header.Relations.IS_CONTAINED_BY.*[in(atom,scope_unit)]{::1}
```
