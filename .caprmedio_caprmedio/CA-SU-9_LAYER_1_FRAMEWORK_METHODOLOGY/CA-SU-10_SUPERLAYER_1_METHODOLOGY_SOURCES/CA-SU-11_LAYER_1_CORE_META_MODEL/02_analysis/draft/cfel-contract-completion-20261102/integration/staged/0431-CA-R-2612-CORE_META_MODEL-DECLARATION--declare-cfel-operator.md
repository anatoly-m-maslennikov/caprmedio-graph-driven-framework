---
atom_id: CA-R-2612
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CFEL<+Operator//RecursiveWildcard
version: 1
updated_at: 2026-11-02 07:52:54 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---

## Summary

Declare CFEL operator **

## Claim

```CFEL
@Operator//RecursiveWildcard == "**"
```

## Semantics

Select distinct dependent Property identities recursively below p in one bearer.
A `p.**` count aggregates that selection across all descendant depths; it does
not count values or another bearer's selection.
