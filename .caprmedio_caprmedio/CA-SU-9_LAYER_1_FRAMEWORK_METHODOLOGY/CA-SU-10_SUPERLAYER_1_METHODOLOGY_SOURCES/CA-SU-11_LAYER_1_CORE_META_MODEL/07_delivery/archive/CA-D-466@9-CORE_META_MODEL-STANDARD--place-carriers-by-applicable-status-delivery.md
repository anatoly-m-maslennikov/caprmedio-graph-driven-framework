---
subjects:
  governs: Artifact Carrier Placement
  depends_on:
  - Artifact.Activity
  - Artifact.Status
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery'
version: 9
updated_at: 2026-10-24 00:38:25 +0400
relations:
  relates_to:
  - CA-D-461
atom_id: CA-D-466@9
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
---
# Summary

Place Carriers by Applicable Status Delivery

## Scope

Carrier placement where Artifact Activity applies or does not apply.

## Claim

**when** Activity applies **and** an Artifact has **`=1`** valid current Revision Status, its Carrier placement **must** follow the most specific applicable Delivery rule for that Artifact Type; **only when** no more specific mapping exists, Active uses the canonical current directory **and** another Status uses its lowercase Status subdirectory. **when** Activity does **not** apply, Carrier placement **must not** derive a Status directory from absent Activity.

## Details
