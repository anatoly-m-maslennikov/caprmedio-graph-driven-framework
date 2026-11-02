---
subjects:
  governs: "Atom.Substance"
  depends_on:
    - "GOVERNS"
    - "Subject"
    - "Entity"
version: 16
updated_at: "2026-10-15 12:21:10 +0000"
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
