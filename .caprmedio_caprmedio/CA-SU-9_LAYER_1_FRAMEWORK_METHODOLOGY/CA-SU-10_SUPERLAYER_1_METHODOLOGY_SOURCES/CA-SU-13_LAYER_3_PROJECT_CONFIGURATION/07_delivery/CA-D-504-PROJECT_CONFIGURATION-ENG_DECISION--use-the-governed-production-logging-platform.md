---
atom_id: CA-D-504
ref_id: CA-D-504
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier
  dependencies:
  - CAPRMEDIO_MODEL <+ Journal
version: 14
updated_at: 2026-11-02 00:18:22 +0400
tier: 3
role: Delivery
form: Decision
container:
  scope_unit: CA-SU-13
carrier_destination:
  file:
    name: CA-D-504-PROJECT_CONFIGURATION-DECISION--use-the-governed-production-logging-platform.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery
---
## Summary

Use the governed production logging platform

## Claim

### Prose Claim


production technical and business runtime log Journal Carriers.


production technical **and** business runtime log Journals **must** use the deployment environment's governed logging sink. governed CAPRMEDIO workflow **and** local project-control Journals **are not** substitutes for the production system's log platform.

## Details

The configured production-log sink may be a local database, remote database, or another governed logging platform. Runtime logs retain Journal classification and recorded-history authority without being forced into _journal. Workflow and project-control Journals retain their own governed records without replacing that platform or duplicating authority for the same historical fact.
