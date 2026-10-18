---
atom_id: "CA-D-504"
content_role: "Delivery"
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
global_tier: 11
status: "Active"
author: "Anatoly Maslennikov"
subjects:
  governs: "Entity/Carrier"
  depends_on:
    - "Entity/Continuant/Node/History/Journal"
version: 3
updated_at: "2026-10-18 03:35:01 +0400"
relations: {}
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/07_delivery/CA-D-504-PROJECT_CONFIGURATION--use-the-governed-production-logging-platform.md
  source_atom_id: CA-D-504
  source_atom_revision: 3
  source_sha256: 78b157ad810666fa667739c14ecb50c0f0673b13dce60b77514bf160dfaea697
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Use the governed production logging platform

## Scope

production technical and business runtime log Journal Carriers.

## Claim

production technical **and** business runtime log Journals **must** use the deployment environment's governed logging sink. governed CAPRMEDIO workflow **and** local project-control Journals **are not** substitutes for the production system's log platform.

## Details

The configured production-log sink may be a local database, remote database, or another governed logging platform. Runtime logs retain Journal classification and recorded-history authority without being forced into _journal. Workflow and project-control Journals retain their own governed records without replacing that platform or duplicating authority for the same historical fact.
