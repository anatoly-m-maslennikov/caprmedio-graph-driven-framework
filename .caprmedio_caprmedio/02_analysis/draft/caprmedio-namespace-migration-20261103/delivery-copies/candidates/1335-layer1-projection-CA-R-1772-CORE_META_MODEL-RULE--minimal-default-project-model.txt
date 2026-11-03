---
version: 37
updated_at: 2026-11-02 18:35:20 +0400
relations:
  child_of:
  - CA-M-005
subjects:
  active: CAPRMEDIO <+ MODEL <+ Project
  passive:
  - CAPRMEDIO <+ MODEL <+ Project
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Requirement)
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Package/Project Implementation
  - CAPRMEDIO <+ MODEL <+ Atom
  - CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Product
atom_id: CA-R-1772
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1772-CORE_META_MODEL-RULE--minimal-default-project-model.md
  source_atom_id: CA-R-1772
  source_atom_revision: 37
  source_sha256: 1d28e4235cf0d7ad41bc54c9bfc4fdc0f85a8f29b23a34066c2731a7d3391422
  original_relations_sha256: 492413f1249ab26855e5486c7d168371d1c677633fce8e2c0144e0c4df387c15
---
## Summary

Minimal default project model

## Claim scope

Project models.

## Claim

CAPRMEDIO **must** use Project-scope Requirement authority plus its real Implementation as the minimum Project model, **must not** require an Implementation Atom, **and** **may** enable other Atom roles, applicability tiers, descendant scopes, **or** automation **only** **when** necessary. Scope Unit ancestry remains parent-declaration data; no Structural Level property is required.
