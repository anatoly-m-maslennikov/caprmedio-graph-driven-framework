---
subjects:
  governs: Entity
  depends_on:
  - Entity/Term//Artifact
  - Entity/Graph Syntax <+ Relation//NARROWER_THAN
version: 34
updated_at: 2026-10-30 17:07:34 +0400
relations: {}
atom_id: CA-R-1765@34
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Prohibit Artifact Type admission through NARROWER_THAN

## Claim scope

Artifact Type values.

## Claim

an Artifact Type value **must not** use NARROWER_THAN **to** establish its admission as an Artifact.
