---
subjects:
  governs: Claim Value Set Authoring
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Substance
  - Subject/Domain/Node/Continuant/Actor
  - Claim Value Set
  - Subject/Domain/Node/Continuant/Term//Property
  - Subject
  - 'Subject/Graph/Relation/Type: IS_ALLOWED_VALUE_OF'
version: 21
updated_at: 2026-10-24 11:58:20 +0400
relations:
  child_of:
  - CA-M-115
atom_id: CA-M-237@21
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 4
type: Implementation Method
---
# Summary

Author Claim Value Sets

## Scope

Claim Value Set authoring.

## Claim

**to** author one Claim Value Set, the Author **must**:

1. identify **`=1`** Property X within **`=1`** Claim;
2. write its finite allowed-value set as `X: (A, B, C)`;
3. include **`>=1`** unique canonical values **and** treat their order as non-authoritative;
4. retain the complete set as **`=1`** Claim **only** **if** **all** values **must** be accepted, replaced, **and** retired together;
5. interpret `:` as Claim Value-Set syntax inside that Claim **and** as **`=1`** IS_ALLOWED_VALUE_OF relation **only** inside a Subject Expression.

## Details
