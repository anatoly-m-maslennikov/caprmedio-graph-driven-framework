---
subjects:
  active: Atom.Content
  passive:
  - Actor
  - Term//Property
  - Entity
  - CFEL <+ Relation//IS_ALLOWED_VALUE_OF
version: 31
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-M-443
atom_id: CA-M-237@31
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
tier: 4
role: Method
form: Implementation Method
---
## Summary

Author Claim Value Sets

## Claim scope

Claim Value Set authoring.

## Claim

**to** author one Claim Value Set, the Author **must**:

1. identify **`=1`** Property X within **`=1`** Claim;
2. write its finite allowed-value set as `X: (A, B, C)`;
3. include **`>=1`** unique canonical values **and** treat their order as non-authoritative;
4. retain the complete set as **`=1`** Claim **only** **if** **all** values **must** be accepted, replaced, **and** retired together;
5. interpret `:` as Claim Value-Set syntax inside that Claim **and** as **`=1`** IS_ALLOWED_VALUE_OF relation **only** inside a Subject Expression.
