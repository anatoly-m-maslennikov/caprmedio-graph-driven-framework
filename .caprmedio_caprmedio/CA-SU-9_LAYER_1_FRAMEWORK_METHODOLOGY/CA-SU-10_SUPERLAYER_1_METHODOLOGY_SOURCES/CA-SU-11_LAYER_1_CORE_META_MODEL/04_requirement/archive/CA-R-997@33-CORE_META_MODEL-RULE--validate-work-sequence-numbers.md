---
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Work Sequence Number'
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Work Sequence Number'
version: 33
updated_at: 2026-10-29 10:13:50 +0400
relations:
  child_of:
  - CA-R-991
  - CA-R-992
atom_id: CA-R-997@33
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Rule
---
## Summary

Validate Work Sequence Numbers

## Claim scope

supplied Work Sequence Numbers for Plans directly contained by the same Plan or sharing the same top-level Plan container.

## Claim

**every** supplied Work Sequence Number **must** be a unique positive ordinal among Plans directly contained by the same Plan **or** sharing the same top-level Plan container.
