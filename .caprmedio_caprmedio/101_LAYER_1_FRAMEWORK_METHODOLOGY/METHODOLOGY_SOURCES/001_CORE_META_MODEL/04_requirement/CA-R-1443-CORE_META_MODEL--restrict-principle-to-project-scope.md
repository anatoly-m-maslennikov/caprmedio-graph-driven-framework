---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Tier
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Local Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
version: 26
updated_at: 2026-10-27 19:59:55 +0400
relations: {}
atom_id: CA-R-1443
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Restrict Principle to Project Scope

## Scope

Atoms with numeric Tier 0 owned by the Project.

## Claim

an Atom **may** use numeric Tier **`0`** **only** **if** its current Scope Unit **`=`** the Project. This scope rule does not impose a Content-Role or Type-to-Tier restriction on other admitted numeric Tiers.

## Details
