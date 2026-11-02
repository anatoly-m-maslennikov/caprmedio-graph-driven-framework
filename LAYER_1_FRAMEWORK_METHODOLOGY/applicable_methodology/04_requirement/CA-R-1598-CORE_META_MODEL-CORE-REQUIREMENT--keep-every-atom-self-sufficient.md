---
subjects:
  governs: "Entity/Node/Continuant/Atom"
  depends_on:
    ["Entity/Node/Continuant/Atom.Property", "Entity/Node/Continuant/Atom.Substance", "Entity/Node/Continuant/Atom", "Markdown Atom Carrier", "Entity/Relation", "Single Source of Truth"]
version: 7
updated_at: "2026-10-19 15:53:41 +0400"
relations: {"relates_to": ["CA-R-117", "CA-R-118", "CA-R-1470"]}
atom_id: "CA-R-1598"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1598-CORE_META_MODEL-CORE-REQUIREMENT--keep-every-atom-self-sufficient.md
  source_atom_id: CA-R-1598
  source_atom_revision: 7
  source_sha256: 20b63d2c396436df7ea4b85f72434015643bed4f8a3de8f756115fae151ceb3b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
