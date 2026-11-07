---
atom_id: CA-R-2784
ref_id: CA-R-2784
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Container.scope_unit
tier: 3
status: Active
version: 1
updated_at: 2026-11-05 22:47:24 +0400
carrier_destination:
  file:
    name: CA-R-2784-CORE_META_MODEL-DECLARATION--declare-atom-header-container-scope-unit.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2784-CORE_META_MODEL-DECLARATION--declare-atom-header-container-scope-unit.md
  source_atom_id: CA-R-2784
  source_atom_revision: 1
  source_sha256: a836a564c7bae0887fb17e9a8a337102f163856b281fb9242888863bc665f6e5
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare Atom.Header.Container.scope_unit

## Claim

### Prose Claim

The value is the stable ID of the containing Scope Unit.
### Formal Claim

```CFEL
# model
Atom.Header.Container.scope_unit :: [string]{::0..1};

Atom.Header.Container.scope_unit.*[]{::0}
```

