---
subjects:
  governs: "Atom/Claim"
  depends_on:
    - "GOVERNS"
    - "Subject"
    - "Entity"
version: 15
updated_at: "2026-10-14 13:43:24 +0400"
relations: {}
atom_id: "CA-R-1203"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Split at Multiple Governed Subject Boundaries

## Scope

an Atom Claim governing canonical Entities through GOVERNS Subject Relations.

## Claim

an Atom **must** be split **if** its Claim governs **`>1`** canonical Entities through GOVERNS Subject Relations.

## Details
