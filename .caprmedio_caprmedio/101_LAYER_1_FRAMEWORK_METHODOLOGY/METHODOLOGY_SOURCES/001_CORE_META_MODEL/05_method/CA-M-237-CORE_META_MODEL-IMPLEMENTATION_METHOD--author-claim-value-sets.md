---
subjects:
  active: Atom.Content
  passive:
  - Actor
  - Term//Property
  - Entity
  - CFEL<+Operator//AllowedValue
version: 33
updated_at: 2026-11-02 08:06:47 +0400
relations:
  child_of:
  - CA-M-443
atom_id: CA-M-237
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
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
5. interpret `:` as Claim Value-Set syntax inside that Claim **and** as one allowed-value qualification inside a Subject Expression; neither use creates a graph Relation or assigns an instance value.
