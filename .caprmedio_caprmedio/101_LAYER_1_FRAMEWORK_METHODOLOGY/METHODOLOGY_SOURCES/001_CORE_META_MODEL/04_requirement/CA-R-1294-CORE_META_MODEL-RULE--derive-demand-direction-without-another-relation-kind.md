---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement/Type: Demand.Target Scope Unit'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Local Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Target Scope Unit
version: 29
updated_at: 2026-10-27 19:59:53 +0400
relations: {}
atom_id: CA-R-1294
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Derive Demand Direction without Another Relation Kind

## Scope

Demand Atom directions.

## Claim

a Demand Atom **must not** introduce a graph Relation Kind for its direction because its Consumer Atom Scope Unit **and** Producer Claim Target Scope Unit references determine that direction.

## Details
