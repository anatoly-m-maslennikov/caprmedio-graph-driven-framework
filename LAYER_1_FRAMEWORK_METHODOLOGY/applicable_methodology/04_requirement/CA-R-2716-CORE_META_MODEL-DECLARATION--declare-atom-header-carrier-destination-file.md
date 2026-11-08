---
atom_id: CA-R-2716
ref_id: CA-R-2716
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Carrier Destination.File
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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2716-CORE_META_MODEL-DECLARATION--declare-atom-header-carrier-destination-file.md
  source_atom_id: CA-R-2716
  source_atom_revision: 2
  source_sha256: 0cb4945cbb0f7efe4cf1a394322c1251aa3831827d343d010298eb6ac32f9a9c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom.Header.Carrier Destination.File

## Claim

### Formal Claim

```CFEL
# model
Atom.Header.Carrier Destination.File{::1}:: []{::0};

Atom.Header.Carrier Destination.File.*[in (Name, Path)]{::2};

Atom.Header.Carrier Destination.File.*:: [string]
```
