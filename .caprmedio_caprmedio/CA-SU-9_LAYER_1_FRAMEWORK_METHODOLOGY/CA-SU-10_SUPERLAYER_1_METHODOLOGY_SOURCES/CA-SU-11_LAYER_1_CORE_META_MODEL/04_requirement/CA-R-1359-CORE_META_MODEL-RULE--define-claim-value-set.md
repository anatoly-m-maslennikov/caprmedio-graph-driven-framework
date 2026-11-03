---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Content
  passive:
  - CAPRMEDIO_MODEL <+ Term//Property
  - CAPRMEDIO_MODEL <+ CFEL<+Operator//AllowedValue
version: 30
updated_at: 2026-11-02 08:06:47 +0400
relations:
  child_of:
  - CA-R-1270
atom_id: CA-R-1359
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
---
## Summary

Define Claim Value Set

## Claim

### Prose Claim


Claim Value Set expressions.


a Claim Value Set **means** one Claim expression **in** the form `X: (A, B, C)`, **where** X identifies **`=1`** Property **and** `(A, B, C)` identifies one finite unordered set of **`>=1`** unique canonical values allowed by X; the value order carries no authority, **and** the complete set **must** have one authority unit **and** lifecycle by accepting, replacing, **and** retiring **all** values together as one Claim.
