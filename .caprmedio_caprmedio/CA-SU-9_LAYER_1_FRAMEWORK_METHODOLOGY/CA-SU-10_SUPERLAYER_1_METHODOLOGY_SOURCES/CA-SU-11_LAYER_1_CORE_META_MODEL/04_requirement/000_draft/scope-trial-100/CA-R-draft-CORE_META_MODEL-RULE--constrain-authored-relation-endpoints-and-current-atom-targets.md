---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Relations
  depends_on:
  - Entity
version: 1
updated_at: 2026-10-29 20:32:25 +0400
relations: {}
atom_id: CA-R-draft
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
tier: 1
type: Rule
---
## Summary

Constrain authored relation endpoints and Current Atom targets

## Claim scope

Authored relation endpoint permissions.

## Claim

Authored relation endpoint permissions are separate from reusable Relation Type meaning:

- rationale_for is owned by a Rationale Analysis Atom and targets one RMED Atom it explains.
- method_for is owned by a Method Atom and targets one Requirement it serves.
- delivery_for is owned by a Delivery Atom and targets one Requirement or Method it realizes.
- concern_about is owned by a Concern Atom and targets the directly affected governed entity.

Each entry represents one directed source-Type-target tuple, not a restriction that an owner can store only one entry of that Type. An Atom target must resolve to its canonical Current version; Draft and Archived targets are not admitted merely because an ID-like string is present.
