---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Plan"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Plan", "Entity/Node/Continuant/Atom/Content Role: Plan.Status: Done"]
version: 9
updated_at: "2026-10-19 15:53:39 +0400"
relations: {"relates_to": ["CA-R-1580", "CA-R-1583", "CA-R-1538"]}
atom_id: "CA-R-1592"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1592-CORE_META_MODEL-GENERAL-REQUIREMENT--keep-plan-completion-prerequisites-acyclic.md
  source_atom_id: CA-R-1592
  source_atom_revision: 9
  source_sha256: 88926d101350cb31de88c465b986ef549a7c03a06ddc6886a1bc7d305e58c97f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Keep Plan completion prerequisites acyclic

## Scope

Plan execution.

## Claim

Plan execution **must not** contain a cycle of completion prerequisites, including one formed jointly by `BLOCKS` **and** the requirement **to** complete decomposed work **before** its Hub can be Done.

## Details
