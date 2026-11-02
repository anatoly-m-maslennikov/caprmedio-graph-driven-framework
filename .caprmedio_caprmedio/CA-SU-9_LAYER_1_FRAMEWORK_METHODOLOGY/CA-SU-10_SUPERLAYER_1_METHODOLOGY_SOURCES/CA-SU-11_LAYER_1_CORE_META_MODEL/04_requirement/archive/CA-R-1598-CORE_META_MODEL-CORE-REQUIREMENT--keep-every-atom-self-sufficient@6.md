---
subjects:
  governs: "Entity/Continuant/Object/Atom"
  depends_on:
    ["Entity/Continuant/Object/Atom.Property", "Entity/Continuant/Object/Atom.Substance", "Entity/Continuant/Object/Atom", "Markdown Atom Carrier", "Entity/Continuant/Object/Relation", "Single Source of Truth"]
version: 6
updated_at: "2026-10-15 18:44:58 +0000"
relations: {"relates_to": ["CA-R-117", "CA-R-118", "CA-R-1470"]}
atom_id: "CA-R-1598"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Keep every Atom self-sufficient

## Scope

Atom Revisions and their applicable Properties.

## Claim

**every** Atom Revision **must** carry its applicable Properties within its own Markdown Carrier so that its own declared content can be read **without** reconstructing it from a filename **or** directory placement.

- the applicable model determines which Properties are required, optional, **or** inapplicable; self-sufficiency does **not** invent missing Properties **or** permit an invalid value.
- a Relation **to** another Atom remains declared **only** on its registered owning endpoint; the other endpoint **and** inverse views are resolved from that declaration, **not** independently copied.
- self-sufficiency does **not** require copying the referenced Atom, governing model, **or** inherited Settings authority into this Atom.

## Details
