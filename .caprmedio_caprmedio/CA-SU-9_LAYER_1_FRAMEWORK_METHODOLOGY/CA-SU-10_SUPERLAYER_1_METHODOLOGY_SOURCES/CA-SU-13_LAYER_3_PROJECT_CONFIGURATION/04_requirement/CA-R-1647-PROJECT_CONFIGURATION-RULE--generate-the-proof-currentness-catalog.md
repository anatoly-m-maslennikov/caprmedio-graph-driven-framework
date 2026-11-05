---
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection/(.Form:=Catalog)
version: 33
updated_at: 2026-11-02 19:44:26 +0400
atom_id: CA-R-1647
ref_id: CA-R-1647
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 3
role: Requirement
form: Rule
container:
  scope_unit: CA-SU-13
carrier_destination:
  file:
    name: CA-R-1647-PROJECT_CONFIGURATION-RULE--generate-the-proof-currentness-catalog.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement
---
## Summary

Generate the proof currentness Catalog

## Claim

### Prose Claim


proof-currentness Catalogs generated from governed proof dependency frontiers and their additional invalidation conditions.


CAPRMEDIO generates a non-authoritative proof-currentness Catalog from governed proof dependency frontiers encoded under GOV REQU 010 **and** their additional invalidation conditions. the Catalog reports **every** proof as `current`, `stale`, **or** `unknown`, marks **only** the smallest direct **and** transitive dependency closure affected by a change, never infers currentness from timestamps alone, **and** never mutates the historical proof record.
