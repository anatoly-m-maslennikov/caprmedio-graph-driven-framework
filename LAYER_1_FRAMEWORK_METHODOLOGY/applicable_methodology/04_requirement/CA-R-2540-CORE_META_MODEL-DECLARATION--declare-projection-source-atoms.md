---
atom_id: CA-R-2540
ref_id: CA-R-2540
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection.Source.Atoms
tier: 3
status: Active
version: 2
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-2540-CORE_META_MODEL-DECLARATION--declare-projection-source-atoms.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2540-CORE_META_MODEL-DECLARATION--declare-projection-source-atoms.md
  source_atom_id: CA-R-2540
  source_atom_revision: 2
  source_sha256: 0f9ec5fc8328285d1961f1d96de33d4c588b018599db36914319c467fbfc2383
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Projection.Source.Atoms

## Claim

### Prose Claim



Each value is an Atom ID with an explicit Version.
### Formal Claim

```CFEL
# model
Projection.Source.Atoms{::0..1}:: [string]{::0+};

Projection.Source.Atoms.*[]{::0}
```

