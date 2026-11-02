---
atom_id: CA-R-2455@2
content_role: Requirement
type: Relation Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
version: 2
updated_at: 2026-10-30 14:14:36 +0400
subjects:
  governs: Entity/Graph Syntax <+ Relation//HAS_PROPERTY
  depends_on:
  - Entity/Graph Syntax <+ Relation//IS_PROPERTY_OF
  - Entity/Property
  - Entity/Term//Property
relations: {}
---
## Summary

Define HAS_PROPERTY Relation

## Claim

HAS_PROPERTY is the declared derived inverse of IS_PROPERTY_OF; its full
meaning remains in the [pending direct Relation Definition](CA-R-draft-CORE_META_MODEL-RELATION_DEFINITION--define-is-property-of.md).
No independently stored reverse fact is introduced.

### Formal claim

```text
Entity/Graph Syntax <+ Relation//HAS_PROPERTY
```

## Details

This Draft proposes HAS_PROPERTY as the replacement inverse view for the
historical BEARS source in CA-R-2416. That provenance neither admits BEARS as
an alias nor repurposes CA-R-2416. It does not define `Entity/Property` or
`Entity/Term//Property`.

The counterpart uses the short-reference template required by CA-R-2228. Its
pending dependency link does not establish Current admission.

### Historical source snapshot

Exact predecessor carrier: `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2416-CORE_META_MODEL-RELATION_DEFINITION--define-bears-relation.md`, Version 1, SHA-256 `5b12d4f4358da16b4483575869da56bacdbaa3acce55b40dd562243c8f03deba`. This is lineage evidence for a fresh Relation identity, not authority admitting the new name.
