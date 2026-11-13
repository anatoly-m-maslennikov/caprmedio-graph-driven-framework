---
identity:
  ref_id: CA-R-3054@1
  id: CA-R-3054
context:
  container:
    scope_unit: CA-SU-11
  role: Requirement
  form: Relation Declaration
  topics:
    main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_REPLACEMENT_FOR
  tier: 4
relations:
  IS_REPLACEMENT_FOR:
  - CA-R-3011
state:
  status: archived
  version: 1
  updated_at: 2026-11-08 20:06:37 +0400
destination:
  file:
    name: CA-R-3054@1-CORE_META_MODEL-RELATION_DECLARATION--declare-is-replacement-for.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
author: Anatoly Maslennikov
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
