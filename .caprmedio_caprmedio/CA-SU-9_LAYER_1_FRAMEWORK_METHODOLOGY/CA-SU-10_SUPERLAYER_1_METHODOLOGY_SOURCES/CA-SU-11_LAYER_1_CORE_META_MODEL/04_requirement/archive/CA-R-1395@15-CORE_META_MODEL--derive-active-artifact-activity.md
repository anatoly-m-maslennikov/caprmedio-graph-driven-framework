---
subjects:
  governs: 'Artifact.Activity: Active'
  depends_on:
  - Artifact.Activity
  - Artifact.Status
version: 15
updated_at: 2026-10-24 12:35:51 +0400
relations: {}
atom_id: CA-R-1395@15
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Derive Active Artifact Activity

## Scope

Artifacts for which Activity applies.

## Claim

an Artifact's Activity **must** be Active **if** Activity applies under CA-R-1307-CORE_META_MODEL-RULE--limit-artifact-activity-to-explicit-status-models, its current Revision has **`=1`** valid Status from the applicable explicitly defined Status model, **and** that Status **`=`** Active.

## Details
