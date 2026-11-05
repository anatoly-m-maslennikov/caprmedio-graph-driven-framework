---
atom_id: CA-R-2704
ref_id: CA-R-2704
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Version
version: 1
updated_at: 2026-11-03 20:00:05 +0400
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2704-CORE_META_MODEL-DECLARATION--declare-atom-header-version.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
container:
  scope_unit: CA-SU-11
---
## Summary

Declare Atom.Header.Version

## Claim

### Formal Claim

```CFEL
# model
Atom.Header.Version{::1}:: [int]{::1};

Atom.Header.Version.*[]{::0};

Atom.Header.Version >= 1
```
