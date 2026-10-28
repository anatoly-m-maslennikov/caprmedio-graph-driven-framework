---
atom_id: CA-R-004
content_role: Requirement
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
version: 32
updated_at: 2026-10-27 19:59:48 +0400
relations:
  child_of:
  - CA-R-2157
subjects:
  governs: 'Subject/caprmedio/Product: CAPRMEDIO Framework'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
tier: 4
type: Rule
---
# Summary

Keep the framework under Operator control

## Scope

**every** governed part of the CAPRMEDIO Framework Instance **in** **every** governed state, including **after** admissible instance changes.

## Claim

the CAPRMEDIO Framework Instance **must** keep **every** governed part of itself under the Operator's control **and** keep the Operator able **to** change the Project through that instance.

## Details

control remains available throughout admissible Framework Instance changes.
