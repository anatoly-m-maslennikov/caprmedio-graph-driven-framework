---
atom_id: CA-R-2478
ref_id: CA-R-2478@6-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_CONTAINED_BY
tier: 3
status: Draft
version: 6
updated_at: 2026-11-05 18:23:39 +0400
carrier_destination:
  file:
    name: CA-R-2478@6-draft-CORE_META_MODEL-DECLARATION--define-composition-and-its-inverse.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define composition and its inverse

## Claim

### Prose Claim

The Target has classification `Container = yes`.

### Formal Claim

```CFEL
# model
$part ((IS_CONTAINED_BY)) $container;

Relation//CONTAINS ((IS_INVERSE_ALIAS_FOR)) Relation//IS_CONTAINED_BY;

alias(Relation//IS_CONTAINED_BY) == "+>";

alias(Relation//CONTAINS) == "/";

Relation//IS_CONTAINED_BY ((HAS_CLASSIFICATION)) Derivation == Direct
```

## Semantics

IS_CONTAINED_BY relates a declared Entity or instance to its immediate Container. CONTAINS is its inverse alias; both writings identify the same fact. `Whole/Part` writes the inverse view and `Part +> Whole` the canonical direction. Containment does not imply narrowing or inheritance.
