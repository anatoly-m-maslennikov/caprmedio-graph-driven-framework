---
atom_id: CA-R-2617
ref_id: CA-R-2617@3-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//CONTAINS
tier: 3
status: Draft
version: 3
updated_at: 2026-11-05 06:30:39 +0400
carrier_destination:
  file:
    name: CA-R-2617@3-draft-DECLARATION--declare-contains.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---
## Summary

Declare CONTAINS

## Claim

### Formal Claim

```CFEL
# model
$contains[<Relation>, (.Name = CONTAINS)];
$contained_by[<Relation>, (.Name = IS_CONTAINED_BY)];

$contains <((HAS_INVERSE)) $contained_by;

alias($contains) == "/"
```

## Semantics

CONTAINS relates a Container to its immediately contained part.
