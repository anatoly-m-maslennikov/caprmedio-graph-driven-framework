---
subjects:
  governs: evaluation
  depends_on: []
version: 20
updated_at: 2026-10-24 00:38:25 +0400
relations:
  resolution_of:
  - CAPRMEDIO-GOV-CONC-054--how-should-proof-currentness-be-represented
atom_id: CA-R-1647@20
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
tier: 3
---
# Summary

Generate the proof currentness Catalog

## Scope

proof-currentness Catalogs generated from governed proof dependency frontiers and their additional invalidation conditions.

## Claim

CAPRMEDIO generates a non-authoritative proof-currentness Catalog from governed proof dependency frontiers encoded under GOV REQU 010 **and** their additional invalidation conditions. the Catalog reports **every** proof as `current`, `stale`, **or** `unknown`, marks **only** the smallest direct **and** transitive dependency closure affected by a change, never infers currentness from timestamps alone, **and** never mutates the historical proof record.

## Details
