---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Method'
  depends_on: []
version: 23
updated_at: 2026-10-23 23:43:05 +0400
relations:
  child_of:
  - CA-M-001
atom_id: CA-R-1767@23
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
status: Archived
author: Anatoly Maslennikov
global_tier: 9
---
# Summary

# Distinguish Implementation Methods from Implementation Decisions

## Scope

Eng Policy and Eng Decision Method and Delivery Types.

## Claim

an Eng Policy governs reusable policy for how accepted specification is realized, while an Eng Decision selects one concrete approach for a bounded realization target. **neither** Eng Policy **nor** Eng Decision is an execution Plan **or** native Implementation.

## Details

These names replace the legacy Implementation Method and Implementation Decision labels for this distinction. Eng Policy ownership requires an actual declared child and automatic application to every child under genuine topic or environment conditions; Eng Decision does not automatically inherit to every child. A named technology alone does not select either Type. This distinction does not impose a Type-to-Tier restriction; the applicable Method and Delivery definitions are CA-R-2119 through CA-R-2122.
