---
atom_id: CA-R-2716
ref_id: CA-R-2716
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Destination.File
tier: 3
status: Active
version: 2
updated_at: 2026-11-04 05:21:15 +0400
carrier_destination:
  file:
    name: CA-R-2716-CORE_META_MODEL-DECLARATION--declare-atom-header-carrier-destination-file.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Atom.Header.Carrier Destination.File

## Claim

### Formal Claim

```CFEL
# model
Atom.Header.Destination.File{::1}:: []{::0};

Atom.Header.Destination.File.*[in (Name, Path)]{::2};

Atom.Header.Destination.File.*:: [string]
```
