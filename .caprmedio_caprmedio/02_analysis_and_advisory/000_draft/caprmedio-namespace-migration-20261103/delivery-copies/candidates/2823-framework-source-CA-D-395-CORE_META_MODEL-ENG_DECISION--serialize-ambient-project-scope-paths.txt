---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Carrier
  passive:
  - CAPRMEDIO <+ MODEL <+ Project
  - CAPRMEDIO <+ MODEL <+ Scope Unit
version: 24
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-395
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
---
## Summary

Serialize Ambient Project Scope Paths

## Claim scope

the `scope_path` encoding of a Carrier.

## Claim

a Carrier encoding of `scope_path` **must** omit the ambient current Project **and** use an empty path for Project Scope.
