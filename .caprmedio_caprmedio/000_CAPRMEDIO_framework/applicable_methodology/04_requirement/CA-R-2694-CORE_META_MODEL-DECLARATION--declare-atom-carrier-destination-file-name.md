---
atom_id: CA-R-2694
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
version: 1
relations: {}
tier: 3
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom.Carrier Destination.File.Name
role: Requirement
form: Declaration
updated_at: 2026-11-03 00:20:05 +0400
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2694-CORE_META_MODEL-DECLARATION--declare-atom-carrier-destination-file-name.md
  source_atom_id: CA-R-2694
  source_atom_revision: 1
  source_sha256: 95df0f10e381c60ea21b7947beb373af8e4dd2333f01bac8a65def79562ae992
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom.Carrier Destination.File.Name

## Claim

```CFEL
Atom.Carrier Destination.File.Name{:1}: [string]{:1};
Atom.Carrier Destination.File.Name.*[]{:0}
```

Calculated full filename, including its extension.
