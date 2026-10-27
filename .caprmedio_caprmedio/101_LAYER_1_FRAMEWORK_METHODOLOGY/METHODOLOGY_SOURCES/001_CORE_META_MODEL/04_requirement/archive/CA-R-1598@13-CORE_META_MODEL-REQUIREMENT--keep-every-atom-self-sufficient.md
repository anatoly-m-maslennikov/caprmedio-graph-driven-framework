---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Property
  - Subject/Domain/Node/Continuant/Atom.Substance
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Engineering/Carrier/File Carrier
  - Subject/Graph/Relation
  - Single Source of Truth
version: 13
updated_at: 2026-10-24 10:48:25 +0400
relations:
  relates_to:
  - CA-R-117
  - CA-R-118
  - CA-R-1470
atom_id: CA-R-1598@13
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
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
