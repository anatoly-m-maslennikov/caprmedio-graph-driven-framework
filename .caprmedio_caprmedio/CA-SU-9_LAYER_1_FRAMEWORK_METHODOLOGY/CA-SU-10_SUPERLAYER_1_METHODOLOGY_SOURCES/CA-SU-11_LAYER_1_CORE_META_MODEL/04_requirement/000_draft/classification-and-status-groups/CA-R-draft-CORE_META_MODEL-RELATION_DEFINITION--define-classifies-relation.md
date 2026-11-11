---
atom_id: CA-R-draft
content_role: Requirement
type: Relation Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
tier: 1
version: 1
updated_at: 2026-10-29 17:56:57 +0400
subjects:
  governs: Entity/Graph Syntax > Relation//CLASSIFIES
relations: {}
---
## Summary

Define CLASSIFIES Relation

## Claim scope

The inverse presentation of the explicit classification relation.

## Claim

CLASSIFIES is the derived inverse of IS_CLASSIFIED_BY. X ::> Y means the same classification as Y <:: X and reuses the main relation meaning; it introduces no separate reverse fact.

### Formal claim

```text
Entity/Graph Syntax > Relation//CLASSIFIES
```

## Notation for subject

```text
X ::> Y
```

## Details

See the sibling Draft Define IS_CLASSIFIED_BY Relation for the complete meaning. Both spellings carry the same classification inheritance: the classified Entity inherits the applicable features of its classification. Neither spelling means structural containment.
