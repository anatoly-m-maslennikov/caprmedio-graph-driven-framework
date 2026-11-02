---
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Method'
  depends_on: []
version: 32
updated_at: 2026-10-29 10:51:18 +0400
relations:
  child_of:
  - CA-M-001
atom_id: CA-R-1767@32
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Distinguish Implementation Methods from Implementation Decisions

## Claim scope

Method Eng Policy/Eng Decision and Delivery Policy/Decision Types.

## Claim

A Method Eng Policy governs reusable engineering policy and an Eng Decision selects a bounded engineering approach. A Delivery Policy governs a reusable representation or delivery family, while a Delivery Decision selects a bounded representation or delivery choice. **neither** Eng Policy **nor** Eng Decision is an execution Plan **or** native Implementation.

## Details

These names replace the legacy Implementation Method and Implementation Decision labels for this distinction. Eng Policy ownership requires an actual declared child and automatic application to every child under genuine topic or environment conditions; Eng Decision does not automatically inherit to every child. A named technology alone does not select either Type. This distinction does not impose a Type-to-Tier restriction; the applicable Method definitions are CA-R-2119 and CA-R-2120; Delivery uses CA-R-2267 and CA-R-2268. The Method actual-child rule is not an extra prerequisite on the Core representation-policy family.
