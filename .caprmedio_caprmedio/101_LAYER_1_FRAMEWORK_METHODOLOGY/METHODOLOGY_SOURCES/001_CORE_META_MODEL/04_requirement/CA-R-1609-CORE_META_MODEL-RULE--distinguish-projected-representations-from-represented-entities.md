---
atom_id: CA-R-1609
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Projection
  passive:
  - Term//Artifact
  - Entity
  - Scope Unit
version: 22
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
---
## Summary

Distinguish projected representations from represented Entities

## Claim scope

Representations inside a Projection and the Entities they represent.

## Claim

a representation inside a Projection **must** remain distinct from the Entity it represents.

- depicting an existing Artifact **or** Scope Unit does **not** create another authoritative Artifact **or** Scope Unit.
- a representation **may** identify a source Entity **or** a derived element admitted by the Projection specification; source identities **and** traceability remain governed by CA-R-2535.
- this boundary introduces no separate Projection Element Term, lifecycle, **or** independently maintained authority.
