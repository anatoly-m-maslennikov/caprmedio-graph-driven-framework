---
atom_id: CA-R-2695
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
version: 1
relations: {}
tier: 3
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom.Carrier Destination.File.Path
role: Requirement
form: Declaration
updated_at: 2026-11-03 00:20:05 +0400
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2695-CORE_META_MODEL-DECLARATION--declare-atom-carrier-destination-file-path.md
  source_atom_id: CA-R-2695
  source_atom_revision: 1
  source_sha256: 7d10802d86a78efe12e9aecb3de28bece2950c3fc5bf674929a29a19eb4ce8cc
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom.Carrier Destination.File.Path

## Claim

```CFEL
Atom.Carrier Destination.File.Path{:1}: [string]{:1};
Atom.Carrier Destination.File.Path.*[]{:0}
```

Calculated path of the containing directory, relative to the repository root.
