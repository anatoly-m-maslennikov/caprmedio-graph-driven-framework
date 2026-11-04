---
atom_id: CA-R-2717
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
version: 3
relations: {}
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Carrier Destination.File.Name
role: Requirement
form: Declaration
updated_at: 2026-11-04 05:21:15 +0400
carrier_destination:
  file:
    name: CA-R-2717-CORE_META_MODEL-DECLARATION--declare-atom-header-carrier-destination-file-name.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2717-CORE_META_MODEL-DECLARATION--declare-atom-header-carrier-destination-file-name.md
  source_atom_id: CA-R-2717
  source_atom_revision: 3
  source_sha256: 73c5fa928f9ebe44fe23d5be8b54f41dca966846fd31ae0bd9329cfde36b8b56
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom.Header.Carrier Destination.File.Name

## Claim

### Formal Claim

```CFEL
# model
Atom.Header.Carrier Destination.File.Name: {:1};

Atom.Header.Carrier Destination.File.Name.*[]{:0}
```

### Prose Claim




Calculated full filename, including its extension.
