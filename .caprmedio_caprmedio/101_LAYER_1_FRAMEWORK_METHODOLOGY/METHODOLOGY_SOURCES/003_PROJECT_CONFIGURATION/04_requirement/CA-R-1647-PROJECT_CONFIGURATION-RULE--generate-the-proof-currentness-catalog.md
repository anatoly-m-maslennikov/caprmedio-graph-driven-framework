---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Projection/Type: Catalog'
  depends_on: []
version: 24
updated_at: 2026-10-25 17:32:27 +0400
relations:
  resolution_of:
  - CAPRMEDIO-GOV-CONC-054--how-should-proof-currentness-be-represented
atom_id: CA-R-1647
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
tier: 3
type: Rule
---
# Summary

Generate the proof currentness Catalog

## Scope

proof-currentness Catalogs generated from governed proof dependency frontiers and their additional invalidation conditions.

## Claim

CAPRMEDIO generates a non-authoritative proof-currentness Catalog from governed proof dependency frontiers encoded under GOV REQU 010 **and** their additional invalidation conditions. the Catalog reports **every** proof as `current`, `stale`, **or** `unknown`, marks **only** the smallest direct **and** transitive dependency closure affected by a change, never infers currentness from timestamps alone, **and** never mutates the historical proof record.

## Details
