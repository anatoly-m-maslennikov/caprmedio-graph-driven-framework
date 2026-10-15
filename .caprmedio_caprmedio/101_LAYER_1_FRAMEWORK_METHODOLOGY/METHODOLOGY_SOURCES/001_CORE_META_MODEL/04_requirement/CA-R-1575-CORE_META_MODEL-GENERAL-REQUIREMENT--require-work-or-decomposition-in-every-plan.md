---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan"
  depends_on:
    ["Atom/Content Role: Plan/Type: Plan", "Entity/Continuant/Object/Atom.Summary", "Entity/Continuant/Object/Atom.Substance"]
version: 6
updated_at: "2026-10-15 18:44:35 +0000"
relations: {"relates_to": ["CA-R-1574", "CA-R-1579"]}
atom_id: "CA-R-1575"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
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
