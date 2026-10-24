---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Concern.Priority'
  depends_on:
  - Subject/Domain/Node/Continuant/Atom/Content Role
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Concern.Priority'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 16
updated_at: 2026-10-24 01:37:42 +0400
relations: {}
atom_id: CA-D-386
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary

Serialize Concern Priority

## Scope

Concern Atom Carriers and non-Concern Content Role Atom Carriers.

## Claim

a Concern Atom Carrier **must** serialize **`=1`** selected Priority as `priority` with the lowercase value `high`, `medium`, **or** `low`. **every** non-Concern Content Role Atom Carrier **must** omit `priority`; virtual `highest` **must not** be stored.

## Details
