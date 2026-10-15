---
subjects:
  governs: "Claim Value Set"
  depends_on:
    ["Entity/Continuant/Object/Atom.Substance", "Property", "IS_ALLOWED_VALUE_OF"]
version: 11
updated_at: "2026-10-15 18:14:10 +0000"
relations:
  child_of:
    - CA-R-1270
atom_id: "CA-R-1359@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 11
---
# Summary

Define Claim Value Set

## Scope

Claim Value Set expressions.

## Claim

a Claim Value Set **means** one Claim expression **in** the form `X: (A, B, C)`, **where** X identifies **`=1`** Property **and** `(A, B, C)` identifies one finite unordered set of **`>=1`** unique canonical values allowed by X; the value order carries no authority, **and** the complete set **must** have one authority unit **and** lifecycle by accepting, replacing, **and** retiring **all** values together as one Claim.

## Details
