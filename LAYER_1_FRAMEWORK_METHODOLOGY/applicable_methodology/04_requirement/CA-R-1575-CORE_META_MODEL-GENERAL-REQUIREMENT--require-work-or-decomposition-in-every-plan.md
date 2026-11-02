---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Plan"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Plan", "Entity/Node/Continuant/Atom.Summary", "Entity/Node/Continuant/Atom.Substance"]
version: 9
updated_at: "2026-10-19 15:53:33 +0400"
relations: {"relates_to": ["CA-R-1574", "CA-R-1579"]}
atom_id: "CA-R-1575"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1575-CORE_META_MODEL-GENERAL-REQUIREMENT--require-work-or-decomposition-in-every-plan.md
  source_atom_id: CA-R-1575
  source_atom_revision: 9
  source_sha256: 3a0b32004327146b8d1e00f91f0877e27fb24d8ca49c8a3740f5a912471528a3
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Require work or decomposition in every Plan

## Scope

Plan Atoms and their work or decomposition.

## Claim

**every** Plan Atom **must** have **`>=1`** of:

- its own work content;
- **`>0`** outgoing `DECOMPOSES_INTO` Relations **to** other Plan Atoms.

both contributions **may** be present within the same Claim; a Summary alone **without** either contribution is insufficient.

## Details
