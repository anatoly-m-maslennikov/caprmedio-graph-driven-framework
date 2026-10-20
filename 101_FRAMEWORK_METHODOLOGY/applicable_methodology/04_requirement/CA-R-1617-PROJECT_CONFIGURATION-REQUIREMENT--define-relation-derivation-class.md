---
atom_id: CA-R-1617
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Relation Derivation Class"
  depends_on:
    - "Evidence"
    - "Realization Graph"
    - "Entity/Relation"
version: 5
updated_at: "2026-10-19 15:56:08 +0400"
relations:
  relates_to:
    - CA-R-1616
    - CA-R-1687
global_tier: 11
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1617-PROJECT_CONFIGURATION-REQUIREMENT--define-relation-derivation-class.md
  source_atom_id: CA-R-1617
  source_atom_revision: 5
  source_sha256: 4b6ea068600b9ecbd69b6946ef6393a320785da153b537814b700c809ff3fd9f
  original_relations_sha256: 5c515042d9acf4a1873660ace68c5e35e3fcb02639d6e217cf7cfe67cfec33ec
---
# Summary

Define Relation Derivation Class

## Scope

represented Realization Graph Relations and their derivation evidence.

## Claim

Relation Derivation Class **means** a classification of how a represented Realization Graph Relation is supported by source declarations, deterministic resolution, possible inference, **or** recorded observation.

## Details

it classifies the derivation evidence, **not** the Relation's validity **or** governing authority. multiple supported classes **may** apply **to** the same Relation; their evidence boundaries remain distinguishable.
