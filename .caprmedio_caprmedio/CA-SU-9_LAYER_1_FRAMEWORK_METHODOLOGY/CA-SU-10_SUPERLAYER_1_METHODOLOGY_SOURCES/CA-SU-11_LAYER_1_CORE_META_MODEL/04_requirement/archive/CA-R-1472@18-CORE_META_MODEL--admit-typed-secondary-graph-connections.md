---
subjects:
  governs: Subject/Graph/Relation
  depends_on:
  - Subject/Graph
  - Subject/Domain/Node/Continuant/Projection
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Graph/Relation
  - Subject/Graph/Relation/Type
version: 18
updated_at: 2026-10-24 23:10:46 +0400
relations: {}
atom_id: CA-R-1472@18
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Admit typed secondary graph connections

## Scope

connections represented by a secondary CAPRMEDIO Graph.

## Claim

a secondary CAPRMEDIO Graph **may** represent typed Relations between its own nodes, **to** another secondary graph **or** its nodes, **and** **to** source Atoms **or** other admitted authoritative sources.

**every** connection **must** use **`=1`** graph-qualified Relation Kind whose governing authority admits its endpoint classes, endpoint graph contexts, direction, **and** cardinality. crossing a graph boundary **must not** transfer Relation Kind ownership, import a foreign Relation Kind as native, **or** make a referenced external endpoint a native node of the receiving graph. a cross-graph reference preserves the referenced identity **without** copying its source fact into independent authority. these permissions do **not** admit concrete Relation Kinds **or** authorize inference beyond their declared rules.

## Details
