---
subjects:
  governs: "Atom.Substance"
  depends_on:
    ["Atom Scope", "Atom.Substance", "Claim Value Set", "Property", "IS_ALLOWED_VALUE_OF"]
version: 14
updated_at: "2026-10-15 12:11:26 +0000"
relations:
  child_of:
    - CA-R-918
    - CA-R-1596
atom_id: "CA-R-1358@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Consolidate Single-Value Claims as One Value-Set Claim

## Scope

multiple Claims with the same Atom Scope, Claim Target Scope Unit, textual Claim Scope, **and** Property X.

## Claim

multiple Claims with the same Atom Scope, Claim Target Scope Unit, textual Claim Scope, **and** Property X **must** be consolidated as **`=1`** Claim Value Set **if** they differ **only** by one allowed value of X.

## Details
