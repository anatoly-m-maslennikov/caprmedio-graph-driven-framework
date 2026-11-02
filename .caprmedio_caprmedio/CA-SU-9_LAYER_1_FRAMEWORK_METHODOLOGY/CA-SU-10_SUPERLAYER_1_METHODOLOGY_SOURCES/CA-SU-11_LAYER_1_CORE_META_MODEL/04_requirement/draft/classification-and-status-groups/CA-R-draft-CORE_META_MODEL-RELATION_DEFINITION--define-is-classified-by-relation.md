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
  governs: Entity/Graph Syntax > Relation//IS_CLASSIFIED_BY
relations: {}
---
## Summary

Define IS_CLASSIFIED_BY Relation

## Claim scope

Explicit classification in the model, including grouping allowed Status values. Classification does not assign a Status value to an Atom instance.

## Claim

IS_CLASSIFIED_BY is the direct classification relation from the classified Entity to the Entity used as its classification. Y <:: X means that Y is classified by X. Its inverse view is CLASSIFIES: X ::> Y expresses the same classification. The classified Entity inherits the applicable features, Properties and constraints defined for its classification. Classification does not itself imply structural containment or declare a narrower-kind relation. These two spellings express one relation fact; the inverse adds no separately stored reverse fact.

### Formal claim

```text
Entity/Graph Syntax > Relation//IS_CLASSIFIED_BY
```

## Notation for subject

```text
Y <:: X
```

## Details

The Operator approved CLASSIFIES for ::> and IS_CLASSIFIED_BY for <::. This adopts the Operator clarification that classification carries inheritance. It adds no globally unique classification requirement, selector engine or automatic runtime inference. Any domain-specific cardinality or classification conditions belong to their own defining requirements. The counterpart Definition references this main meaning instead of repeating it.
