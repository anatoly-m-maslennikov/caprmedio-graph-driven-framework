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
---
## Summary

Use the governed production logging platform

## Claim

### Prose Claim


production technical and business runtime log Journal Carriers.


production technical **and** business runtime log Journals **must** use the deployment environment's governed logging sink. governed CAPRMEDIO workflow **and** local project-control Journals **are not** substitutes for the production system's log platform.

## Details

The configured production-log sink may be a local database, remote database, or another governed logging platform. Runtime logs retain Journal classification and recorded-history authority without being forced into _journal. Workflow and project-control Journals retain their own governed records without replacing that platform or duplicating authority for the same historical fact.
