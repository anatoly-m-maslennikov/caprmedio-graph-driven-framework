---
subjects:
  governs: Entity/Graph Syntax > Relation
  depends_on:
  - Entity
  - Entity/Object/Continuant/Term//Artifact
  - Entity
version: 20
updated_at: 2026-10-29 10:13:48 +0400
relations: {}
atom_id: CA-R-1410
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Connect Every CAPRMEDIO Graph through the General Artifact Graph

## Claim scope

CAPRMEDIO Graphs and their connections to the General Artifact Graph.

## Claim

**every** CAPRMEDIO Graph **must** connect **to** the General Artifact Graph through **`>=1`** shared **or** referenced source Artifact **or** Structural Entity. the connection preserves the existing source identity **without** creating a duplicate source **or** requiring an artificial Artifact for a structural-only source.
