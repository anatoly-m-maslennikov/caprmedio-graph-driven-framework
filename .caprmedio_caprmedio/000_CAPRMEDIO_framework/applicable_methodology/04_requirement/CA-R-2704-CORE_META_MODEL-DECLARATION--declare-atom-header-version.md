---
atom_id: CA-R-2704
ref_id: CA-R-2704
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Version
tier: 3
status: Active
version: 1
updated_at: 2026-11-03 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-2704-CORE_META_MODEL-DECLARATION--declare-atom-header-version.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2704-CORE_META_MODEL-DECLARATION--declare-atom-header-version.md
  source_atom_id: CA-R-2704
  source_atom_revision: 1
  source_sha256: 078da3b4f7d8d1446d8228694cac982f4019c8faa5acdcd6fc3e01fb9d0c5279
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
