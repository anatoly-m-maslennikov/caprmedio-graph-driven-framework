---
subjects:
  active: Atom.Content
  passive:
  - Entity/Object/Continuant/Governing Objects/Atom.Local Scope Unit
  - Term//Property
  - CFEL <+ Relation//IS_ALLOWED_VALUE_OF
version: 33
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-2102
  - CA-R-1596
atom_id: CA-R-1358@33
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
tier: 3
role: Requirement
form: Rule
---
## Summary

Consolidate Single-Value Claims as One Value-Set Claim

## Claim scope

multiple Claims with the same Atom Scope, Claim Target Scope Unit, textual Claim Scope, **and** Property X.

## Claim

multiple Claims with the same Atom Scope, Claim Target Scope Unit, textual Claim Scope, **and** Property X **must** be consolidated as **`=1`** Claim Value Set **if** they differ **only** by one allowed value of X.
