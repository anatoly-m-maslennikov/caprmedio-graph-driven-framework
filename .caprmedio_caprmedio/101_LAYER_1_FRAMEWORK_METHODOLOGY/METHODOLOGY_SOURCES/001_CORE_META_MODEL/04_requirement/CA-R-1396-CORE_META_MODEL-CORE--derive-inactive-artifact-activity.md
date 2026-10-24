---
subjects:
  governs: 'Artifact.Activity: Inactive'
  depends_on:
  - Artifact.Activity
  - Artifact.Status
version: 13
updated_at: 2026-10-24 01:37:42 +0400
relations: {}
atom_id: CA-R-1396
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Derive Inactive Artifact Activity

## Scope

Artifacts for which Activity applies.

## Claim

an Artifact's Activity **must** be Inactive **if** Activity applies under CA-R-1307, its current Revision has **`=1`** valid Status from the applicable explicitly defined Status model, **and** that Status **`!=`** Active.

## Details
