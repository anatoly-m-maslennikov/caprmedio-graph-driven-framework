---
subjects:
  governs: 'Entity/Node/Continuant/Atom/Content Role: Plan.Status'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
  - Subject/Domain/Node/Continuant/Atom.Status
version: 11
updated_at: 2026-10-24 00:38:25 +0400
relations:
  relates_to:
  - CA-R-1412
atom_id: CA-R-1539@11
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
---
# Summary

Register Core Plan Status Values

## Scope

Core Plan Status values.

## Claim

the Core Plan Status model **must** inherit the allowed values of Atom.Status and add (Backlog, Done, Canceled). Planned **must not** be a distinct Plan Status.

## Details
