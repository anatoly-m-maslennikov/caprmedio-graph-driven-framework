---
atom_id: CA-D-504
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier
  passive:
  - CAPRMEDIO_MODEL <+ Journal
version: 14
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery/CA-D-504-PROJECT_CONFIGURATION-ENG_DECISION--use-the-governed-production-logging-platform.md
  source_atom_id: CA-D-504
  source_atom_revision: 14
  source_sha256: c7337bfd3b2ed8b5c73b46efd1a36ca8fe14c98fb47d3168e67b074cabf013a2
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Use the governed production logging platform

## Claim

### Prose Claim


production technical and business runtime log Journal Carriers.


production technical **and** business runtime log Journals **must** use the deployment environment's governed logging sink. governed CAPRMEDIO workflow **and** local project-control Journals **are not** substitutes for the production system's log platform.

## Details

The configured production-log sink may be a local database, remote database, or another governed logging platform. Runtime logs retain Journal classification and recorded-history authority without being forced into _journal. Workflow and project-control Journals retain their own governed records without replacing that platform or duplicating authority for the same historical fact.
