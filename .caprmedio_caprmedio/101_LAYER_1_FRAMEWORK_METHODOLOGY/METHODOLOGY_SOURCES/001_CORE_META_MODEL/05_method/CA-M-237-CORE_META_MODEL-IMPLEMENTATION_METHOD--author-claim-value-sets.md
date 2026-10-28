---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Actor
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Property
  - Subject
  - 'Subject/CAPRMEDIO/Graph/Relation/Type: IS_ALLOWED_VALUE_OF'
version: 25
updated_at: 2026-10-27 19:59:40 +0400
relations:
  child_of:
  - CA-M-115
atom_id: CA-M-237
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
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
