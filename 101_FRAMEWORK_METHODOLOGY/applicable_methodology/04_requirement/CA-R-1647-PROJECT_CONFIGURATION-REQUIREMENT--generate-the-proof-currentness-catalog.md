---
subjects:
  governs: "evaluation"
  depends_on: []
version: 19
updated_at: "2026-10-19 14:46:22 +0400"
relations:
  resolution_of:
    - CAPRMEDIO-GOV-CONC-054--how-should-proof-currentness-be-represented
atom_id: "CA-R-1647"
content_role: "Requirement"
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/04_requirement/CA-R-1647-PROJECT_CONFIGURATION-REQUIREMENT--generate-the-proof-currentness-catalog.md
  source_atom_id: CA-R-1647
  source_atom_revision: 19
  source_sha256: 9196a70d555f5388d3305b05a4ead943d1211add4b4818e101be5983efdda4db
  original_relations_sha256: f92866e80ecae21a57cc95ee6a0987c0e7890e086be2a2dcc34ad89fee8fffa1
---
# Summary

Generate the proof currentness Catalog

## Scope

proof-currentness Catalogs generated from governed proof dependency frontiers and their additional invalidation conditions.

## Claim

CAPRMEDIO generates a non-authoritative proof-currentness Catalog from governed proof dependency frontiers encoded under GOV REQU 010 **and** their additional invalidation conditions. the Catalog reports **every** proof as `current`, `stale`, **or** `unknown`, marks **only** the smallest direct **and** transitive dependency closure affected by a change, never infers currentness from timestamps alone, **and** never mutates the historical proof record.

## Details
