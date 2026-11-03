---
atom_id: CA-R-2540
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Projection.Source.Atoms
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2540-CORE_META_MODEL-DECLARATION--declare-projection-source-atoms.md
  source_atom_id: CA-R-2540
  source_atom_revision: 2
  source_sha256: 180a36971ac4ffb0fbb048bd2461ede13a9be2038f6377940104d40fb10ae516
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Projection.Source.Atoms

## Claim

```CFEL
Projection.Source.Atoms{:0..1}: [string]{:0+};
Projection.Source.Atoms.*[]{:0}
```

Each value is an Atom ID with an explicit Version.
