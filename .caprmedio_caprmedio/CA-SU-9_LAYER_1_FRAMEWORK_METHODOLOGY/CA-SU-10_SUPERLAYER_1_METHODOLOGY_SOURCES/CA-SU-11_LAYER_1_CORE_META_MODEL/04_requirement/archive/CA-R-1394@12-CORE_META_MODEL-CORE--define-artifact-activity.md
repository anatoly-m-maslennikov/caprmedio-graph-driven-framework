---
subjects:
  governs: Artifact.Activity
  depends_on:
  - Artifact
  - Artifact.Status
  - Property
  - 'Artifact.Activity: Active'
  - 'Artifact.Activity: Inactive'
version: 12
updated_at: 2026-10-24 00:38:25 +0400
relations: {}
atom_id: CA-R-1394@12
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
---
# Summary
Define Artifact Activity

## Scope
Artifact Activity derived from an Artifact's current Revision Status within the applicability defined by CA-R-1307-CORE_META_MODEL-CORE-REQUIREMENT--limit-artifact-activity-to-explicit-status-models, including absence of an applicable Status model.

## Claim

the Artifact Property Activity **means** the derived Property that classifies an Artifact as Active **or** Inactive from its current Revision Status within the applicability defined by CA-R-1307-CORE_META_MODEL-CORE-REQUIREMENT--limit-artifact-activity-to-explicit-status-models. absence of an applicable Status model **means** absence of Activity, **not** Activity Inactive.

## Details
