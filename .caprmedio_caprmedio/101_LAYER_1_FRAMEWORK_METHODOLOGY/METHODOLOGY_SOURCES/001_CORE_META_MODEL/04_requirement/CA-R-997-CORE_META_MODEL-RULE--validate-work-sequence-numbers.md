---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan.Work Sequence Number'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan.Work Sequence Number'
version: 30
updated_at: 2026-10-27 20:00:13 +0400
relations:
  child_of:
  - CA-R-991
  - CA-R-992
atom_id: CA-R-997
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Rule
---
# Summary

Validate Work Sequence Numbers

## Scope

supplied Work Sequence Numbers for Plans directly contained by the same Plan or sharing the same top-level Plan container.

## Claim

**every** supplied Work Sequence Number **must** be a unique positive ordinal among Plans directly contained by the same Plan **or** sharing the same top-level Plan container.

## Details
