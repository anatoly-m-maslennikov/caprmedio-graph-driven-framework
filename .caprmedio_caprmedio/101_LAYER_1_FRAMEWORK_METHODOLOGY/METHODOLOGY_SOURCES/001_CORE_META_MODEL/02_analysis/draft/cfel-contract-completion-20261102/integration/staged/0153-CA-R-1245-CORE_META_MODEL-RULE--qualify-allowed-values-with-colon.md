---
subjects:
  active: Entity
  passive:
  - CFEL<+Operator//AllowedValue
  - Term//Property
version: 28
updated_at: 2026-11-02 07:49:21 +0400
relations: {}
atom_id: CA-R-1245
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
---
## Summary

Qualify Allowed Values with Colon

## Claim scope

allowed-value qualification in a Subject Expression.

## Claim

**in** a Subject Expression, `X:Y` **must** admit Y as one possible value of X in X's qualified context, irrespective of X's kind or path. This qualification is a CFEL operator, not a graph Relation. It does not assign Y to an occurrence or determine direct-value cardinality.
