---
subjects:
  active: Atom/(.Role := Plan).Work Sequence Number
  passive:
  - Atom/(.Role := Plan)
  - Atom/(.Role := Plan).Work Sequence Number
version: 34
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-2520
  - CA-R-992
atom_id: CA-R-997
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
---
## Summary

Validate Work Sequence Numbers

## Claim scope

supplied Work Sequence Numbers for Plans directly contained by the same Plan or sharing the same top-level Plan container.

## Claim

**every** supplied Work Sequence Number **must** be a unique positive ordinal among Plans directly contained by the same Plan **or** sharing the same top-level Plan container.
