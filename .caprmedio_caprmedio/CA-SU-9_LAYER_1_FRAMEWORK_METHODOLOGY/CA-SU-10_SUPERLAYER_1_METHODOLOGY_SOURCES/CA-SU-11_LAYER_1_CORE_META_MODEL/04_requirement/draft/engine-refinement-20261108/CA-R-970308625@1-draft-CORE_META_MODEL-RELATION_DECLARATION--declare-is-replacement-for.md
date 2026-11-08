---
identity:
  id: CA-R-970308625
  ref_id: CA-R-970308625@1-draft
context:
  container:
    scope_unit: CA-SU-11
  role: Requirement
  form: Relation Declaration
  topics:
    main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_REPLACEMENT_FOR
  tier: 4
state:
  status: Draft
  version: 1
  updated_at: 2026-11-08 18:49:12 +0400
destination:
  file:
    name: CA-R-970308625@1-draft-CORE_META_MODEL-RELATION_DECLARATION--declare-is-replacement-for.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft/engine-refinement-20261108
author: Anatoly Maslennikov
relations:
  IS_REPLACEMENT_FOR:
    atom:
    - CA-R-3011
---

## Summary

Declare IS_REPLACEMENT_FOR

## Claim

### Prose Claim

The Host is a replacement Atom. The Target is a predecessor Atom identified by its base Atom ID. One replacement can target several predecessors.

A Draft Host proposes replacement. Its links remain after promotion, including when the predecessor becomes Archived. Completed replacement requires an adopted successor and an Archived predecessor.

### Formal Claim

```CFEL
# model
Relation//IS_REPLACEMENT_FOR ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
$replacement[<Atom>] ((IS_REPLACEMENT_FOR)) $predecessor[<Atom>]
```

## Semantics

IS_REPLACEMENT_FOR relates a replacement Atom to the predecessor Atom whose contribution it replaces.
