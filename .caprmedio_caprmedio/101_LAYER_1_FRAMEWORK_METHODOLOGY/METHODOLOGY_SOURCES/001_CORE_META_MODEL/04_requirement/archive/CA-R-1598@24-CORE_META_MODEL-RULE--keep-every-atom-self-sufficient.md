---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Object/Continuant/Governing Objects/Atom.Content
  - Entity/Carrier/File
  - Entity/Graph Syntax > Relation
version: 24
updated_at: 2026-10-29 10:13:49 +0400
relations: {}
atom_id: CA-R-1598@24
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Keep every Atom self-sufficient

## Claim scope

Atom Revisions and their applicable Properties.

## Claim

**every** Atom Revision **must** carry its applicable Properties within its own Markdown Carrier so that its own declared content can be read **without** reconstructing it from a filename **or** directory placement.

- the applicable model determines which Properties are required, optional, **or** inapplicable; self-sufficiency does **not** invent missing Properties **or** permit an invalid value.
- a Relation **to** another Atom remains declared **only** on its registered owning endpoint; the other endpoint **and** inverse views are resolved from that declaration, **not** independently copied.
- self-sufficiency does **not** require copying the referenced Atom, governing model, **or** inherited Settings authority into this Atom.
