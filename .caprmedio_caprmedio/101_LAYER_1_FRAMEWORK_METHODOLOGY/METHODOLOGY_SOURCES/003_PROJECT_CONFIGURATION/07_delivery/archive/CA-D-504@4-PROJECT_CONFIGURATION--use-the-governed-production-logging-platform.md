---
atom_id: CA-D-504@4
content_role: "Delivery"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
global_tier: 11
status: Archived
author: "Anatoly Maslennikov"
subjects:
  governs: "Entity/Carrier"
  depends_on:
    - "Entity/Node/Continuant/History/Journal"
version: 4
updated_at: "2026-10-19 15:56:25 +0400"
relations: {}
---
# Summary

Use the governed production logging platform

## Scope

production technical and business runtime log Journal Carriers.

## Claim

production technical **and** business runtime log Journals **must** use the deployment environment's governed logging sink. governed CAPRMEDIO workflow **and** local project-control Journals **are not** substitutes for the production system's log platform.

## Details

The configured production-log sink may be a local database, remote database, or another governed logging platform. Runtime logs retain Journal classification and recorded-history authority without being forced into _journal. Workflow and project-control Journals retain their own governed records without replacing that platform or duplicating authority for the same historical fact.
