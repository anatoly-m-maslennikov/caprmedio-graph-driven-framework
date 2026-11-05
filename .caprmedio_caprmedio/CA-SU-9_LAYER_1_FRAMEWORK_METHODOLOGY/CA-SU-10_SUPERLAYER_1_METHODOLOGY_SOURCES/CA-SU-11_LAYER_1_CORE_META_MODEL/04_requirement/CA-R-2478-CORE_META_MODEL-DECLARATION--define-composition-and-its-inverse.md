---
atom_id: CA-R-2478
ref_id: CA-R-2478
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_CONTAINED_BY
version: 5
updated_at: 2026-11-03 20:00:05 +0400
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2478-CORE_META_MODEL-DECLARATION--define-composition-and-its-inverse.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
container:
  scope_unit: CA-SU-11
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
