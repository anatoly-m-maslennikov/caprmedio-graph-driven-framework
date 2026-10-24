---
subjects:
  governs: Set-valued Property Membership Evaluation
  depends_on:
  - Subject/Graph/Rule/CCE Condition Expression Evaluation
  - Set-valued Property
version: 17
updated_at: 2026-10-24 01:18:03 +0400
relations:
  child_of:
  - CA-M-122
atom_id: CA-M-127@17
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
---
# Summary

Evaluate Set-valued Property Membership

## Scope

evaluation of **in** **or** **not in** for one set-valued governed property.

## Claim

**to** evaluate **in** **or** **not in** for one set-valued governed property, the Resolver **must** evaluate **in** as true exactly **when** **`>=1`** property member **`=`** one listed value **and** **must** evaluate **not in** as true exactly **when** no property member **`=`** **any** listed value.

## Details
