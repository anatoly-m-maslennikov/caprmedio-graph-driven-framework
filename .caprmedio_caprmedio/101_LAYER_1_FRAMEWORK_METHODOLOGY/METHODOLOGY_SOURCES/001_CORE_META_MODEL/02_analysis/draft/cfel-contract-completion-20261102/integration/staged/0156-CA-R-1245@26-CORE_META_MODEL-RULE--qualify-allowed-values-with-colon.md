---
subjects:
  active: Entity
  passive:
  - CFEL <+ Relation//IS_ALLOWED_VALUE_OF
  - Term//Property
version: 26
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1245@26
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
tier: 3
role: Requirement
form: Rule
---
## Summary

Qualify Allowed Values with Colon

## Claim scope

allowed-value qualification in a Subject Expression.

## Claim

**in** a Subject Expression, `X:Y` **must** express only one IS_ALLOWED_VALUE_OF relation from value Y to target Entity X, irrespective of X's kind or path. This relation admits Y as a possible value in X's qualified context; it does not assign Y to an occurrence or determine direct-value cardinality.
