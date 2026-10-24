---
atom_id: CA-R-1617@7
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Relation Derivation Class
  depends_on:
  - Evidence
  - Realization Graph
  - Subject/Graph/Relation
version: 7
updated_at: 2026-10-24 00:38:25 +0400
relations:
  relates_to:
  - CA-R-1616
  - CA-R-1687
tier: 3
---
# Summary

Define Relation Derivation Class

## Scope

represented Realization Graph Relations and their derivation evidence.

## Claim

Relation Derivation Class **means** a classification of how a represented Realization Graph Relation is supported by source declarations, deterministic resolution, possible inference, **or** recorded observation.

## Details

it classifies the derivation evidence, **not** the Relation's validity **or** governing authority. multiple supported classes **may** apply **to** the same Relation; their evidence boundaries remain distinguishable.
