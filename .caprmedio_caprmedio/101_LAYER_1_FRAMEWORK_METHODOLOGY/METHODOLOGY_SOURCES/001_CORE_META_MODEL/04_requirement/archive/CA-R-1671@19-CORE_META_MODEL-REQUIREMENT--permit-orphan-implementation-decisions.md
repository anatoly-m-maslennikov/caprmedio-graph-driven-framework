---
subjects:
  governs: requirement-topology
  depends_on: []
version: 19
updated_at: 2026-10-24 01:37:42 +0400
relations:
  child_of:
  - CAPRMEDIO-REQU-037-REQUIREMENT--require-parent-coverage-without-claiming-topology-completeness
  - CA-R-1767
atom_id: CA-R-1671@19
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Rule
---
# Summary

Permit orphan Implementation Decisions

## Scope

orphan permission for an active Eng Decision in strict authority mode.

## Claim

`eng_decision` **must** be registered as orphan-permitted, so an active Eng Decision **may** have no parent Eng Policy even **in** strict authority mode.

## Details

This Atom-topology permission does not create a local Policy owner at a leaf or justify artificial children; local Eng Policy ownership and child applicability remain governed by CA-R-2119 and CA-R-2120.
