---
atom_id: CA-R-2478
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_CONTAINED_BY
version: 5
updated_at: 2026-11-03 20:00:05 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2478-CORE_META_MODEL-DECLARATION--define-composition-and-its-inverse.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2478-CORE_META_MODEL-DECLARATION--define-composition-and-its-inverse.md
  source_atom_id: CA-R-2478
  source_atom_revision: 5
  source_sha256: 2bbe754228c33da33e6dd16599e25cf039757d43d886da01402db4e0acf0a6e8
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define composition and its inverse

## Claim

### Formal Claim

```CFEL
# model
$part ((IS_CONTAINED_BY)) $container;

Relation//IS_CONTAINED_BY ((HAS_INVERSE)) Relation//CONTAINS;

alias(Relation//IS_CONTAINED_BY) == "+>";

Relation//IS_CONTAINED_BY ((HAS_CLASSIFICATION)) Derivation == Direct
```

### Prose Claim

IS_CONTAINED_BY relates a contained declared Entity or instance to its immediate Container. The Target has classification `Container = yes`. Containment does not imply narrowing or inheritance. CONTAINS is its derived inverse: its Host and Target are the direct Target and Host, respectively. Store the direct fact once.
