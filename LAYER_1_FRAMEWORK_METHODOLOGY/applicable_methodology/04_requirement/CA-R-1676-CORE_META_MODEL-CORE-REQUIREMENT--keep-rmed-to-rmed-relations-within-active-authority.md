---
subjects:
  governs: "relation-model"
  depends_on:
    - "atom-boundary"
version: 21
updated_at: "2026-10-20 17:06:57 +0400"
relations:
  child_of:
    - CA-R-1051
atom_id: "CA-R-1676"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1676-CORE_META_MODEL-CORE-REQUIREMENT--keep-rmed-to-rmed-relations-within-active-authority.md
  source_atom_id: CA-R-1676
  source_atom_revision: 21
  source_sha256: a3807e2f89f3af7b296475d52b7813706ca92b2c07866713f54c01a9d4e04d50
  original_relations_sha256: fe61d145e2f5d262fb51b9ad7918a9f53aec7113df1dcdbd7cd1717f12d807c7
---
# Summary

Keep RMED-to-RMED Relations within Active Authority

## Scope

direct relations authored by Current RMED Atoms that target RMED Atoms.

## Claim

**if** a direct relation is authored by a Current Atom with Content Role **in** (Requirement, Method, Evaluation, Delivery) **and** targets an Atom with Content Role **in** (Requirement, Method, Evaluation, Delivery), **then** the target Atom **must** be Current.

## Details
