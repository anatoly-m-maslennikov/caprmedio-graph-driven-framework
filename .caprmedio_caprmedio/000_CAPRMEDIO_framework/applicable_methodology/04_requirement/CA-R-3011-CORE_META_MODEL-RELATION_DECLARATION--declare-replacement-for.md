---
atom_id: CA-R-3011
ref_id: CA-R-3011
container:
  scope_unit: CA-SU-11
role: Requirement
form: Relation Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//REPLACEMENT_FOR
tier: 3
status: Active
version: 1
updated_at: "2026-11-08 15:22:04 +0400"
carrier_destination:
  file:
    name: CA-R-3011-CORE_META_MODEL-RELATION_DECLARATION--declare-replacement-for.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-3011-CORE_META_MODEL-RELATION_DECLARATION--declare-replacement-for.md
  source_atom_id: CA-R-3011
  source_atom_revision: 1
  source_sha256: 188d3d460e4df2326193cc327e5596270f26178accac8ca07273a661597e133a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare REPLACEMENT_FOR

## Claim

### Prose Claim

The Host is a replacement Atom. The Target is a predecessor Atom identified by its base Atom ID. One replacement can target several predecessors.

A Draft Host proposes replacement. Its links remain after promotion, including when the predecessor becomes Archived. Completed replacement requires an adopted successor and an Archived predecessor.

### Formal Claim

```CFEL
# model
Relation//REPLACEMENT_FOR ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
$replacement[<Atom>] ((REPLACEMENT_FOR)) $predecessor[<Atom>]
```

## Semantics

REPLACEMENT_FOR relates a replacement Atom to the predecessor Atom whose contribution it replaces.
