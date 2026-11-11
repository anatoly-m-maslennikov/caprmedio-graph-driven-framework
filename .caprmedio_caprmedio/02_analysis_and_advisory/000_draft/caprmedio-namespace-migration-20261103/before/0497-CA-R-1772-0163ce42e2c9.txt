---
version: 37
updated_at: 2026-11-02 18:35:20 +0400
relations:
  child_of:
  - CA-M-005
subjects:
  active: Project
  passive:
  - Project
  - Atom/(.Role := Requirement)
  - Entity/Object/Continuant/Package/Project Implementation
  - Atom
  - Aspects <+ Product
atom_id: CA-R-1772
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Minimal default project model

## Claim scope

Project models.

## Claim

CAPRMEDIO **must** use Project-scope Requirement authority plus its real Implementation as the minimum Project model, **must not** require an Implementation Atom, **and** **may** enable other Atom roles, applicability tiers, descendant scopes, **or** automation **only** **when** necessary. Scope Unit ancestry remains parent-declaration data; no Structural Level property is required.
