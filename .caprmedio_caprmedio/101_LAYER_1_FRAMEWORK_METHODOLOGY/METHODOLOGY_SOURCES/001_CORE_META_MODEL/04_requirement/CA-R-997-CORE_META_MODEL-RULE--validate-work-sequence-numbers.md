---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan.Work Sequence Number'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan.Work Sequence Number'
version: 29
updated_at: 2026-10-26 17:47:19 +0400
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
