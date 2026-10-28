---
atom_id: CA-D-504@10
content_role: Delivery
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Graph Node/Carrier
  depends_on:
  - Subject/Graph Node/Domain/Continuant/History/Journal
version: 10
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
tier: 3
type: Eng Decision
---
# Summary

Use the governed production logging platform

## Scope

production technical and business runtime log Journal Carriers.

## Claim

production technical **and** business runtime log Journals **must** use the deployment environment's governed logging sink. governed CAPRMEDIO workflow **and** local project-control Journals **are not** substitutes for the production system's log platform.

## Details

The configured production-log sink may be a local database, remote database, or another governed logging platform. Runtime logs retain Journal classification and recorded-history authority without being forced into _journal. Workflow and project-control Journals retain their own governed records without replacing that platform or duplicating authority for the same historical fact.
