---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Method'
  depends_on: []
version: 25
updated_at: 2026-10-24 01:37:42 +0400
relations:
  child_of:
  - CA-M-001
atom_id: CA-R-1767
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

# Distinguish Implementation Methods from Implementation Decisions

## Scope

Eng Policy and Eng Decision Method and Delivery Types.

## Claim

an Eng Policy governs reusable policy for how accepted specification is realized, while an Eng Decision selects one concrete approach for a bounded realization target. **neither** Eng Policy **nor** Eng Decision is an execution Plan **or** native Implementation.

## Details

These names replace the legacy Implementation Method and Implementation Decision labels for this distinction. Eng Policy ownership requires an actual declared child and automatic application to every child under genuine topic or environment conditions; Eng Decision does not automatically inherit to every child. A named technology alone does not select either Type. This distinction does not impose a Type-to-Tier restriction; the applicable Method and Delivery definitions are CA-R-2119 through CA-R-2122.
