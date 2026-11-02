---
subjects:
  governs: "Entity/Continuant/Node/Atom/Content Role: Plan"
  depends_on:
    ["Entity/Continuant/Node/Atom/Content Role: Plan", "Entity/Continuant/Node/Atom/Content Role: Plan.Status: Done"]
version: 8
updated_at: "2026-10-18 03:33:44 +0400"
relations: {"relates_to": ["CA-R-1580", "CA-R-1583", "CA-R-1538"]}
atom_id: "CA-R-1592"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Keep Plan completion prerequisites acyclic

## Scope

Plan execution.

## Claim

Plan execution **must not** contain a cycle of completion prerequisites, including one formed jointly by `BLOCKS` **and** the requirement **to** complete decomposed work **before** its Hub can be Done.

## Details
