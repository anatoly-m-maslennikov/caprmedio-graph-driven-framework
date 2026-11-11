---
atom_id: CA-R-2702
ref_id: CA-R-2702
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Context.Role
tier: 3
status: Active
version: 2
updated_at: '2026-11-11T18:56:17+04:00'
carrier_destination:
  file:
    name: CA-R-2702-CORE_META_MODEL-DECLARATION--declare-atom-header-role.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Atom.Header.Role

## Claim


### Prose Claim

Role Order Number classifies the Role-qualified Atom kind in the Model. Each Role Declaration assigns exactly one positive integer. Order numbers are distinct across Roles. Gaps are allowed.

### Formal Claim

```CFEL
# model
Atom.Header.Context.Role{::1}:: [string]{::1};

Atom.Header.Context.Role.*[]{::0}
```
