---
subjects:
  governs: "Entity/Continuant/Object/Atom/Content Role: Plan"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Plan", "Entity/Continuant/Object/Atom.Summary", "Entity/Continuant/Object/Atom.Substance"]
version: 7
updated_at: "2026-10-16 12:08:32 +0000"
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
  source_atom_revision: 7
  source_sha256: 27a5d7bad10be94884cc3c783c84bd1f5960d1ec8b9515a5dbe08658f45a7b46
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
