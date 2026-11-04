---
version: 37
updated_at: 2026-11-02 18:35:20 +0400
relations:
  child_of:
  - CA-M-005
subjects:
  active: CAPRMEDIO_MODEL <+ Project
  passive:
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)
  - CAPRMEDIO_MODEL <+ Package/Implementation
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Product
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
  source_sha256: 42a2f6ea0450b2616c1641b6b125c45f624e57482d0b7c31ef028279f9dfd8c0
  original_relations_sha256: 492413f1249ab26855e5486c7d168371d1c677633fce8e2c0144e0c4df387c15
---
## Summary

Minimal default project model

## Claim

### Prose Claim


Project models.


CAPRMEDIO **must** use Project-scope Requirement authority plus its real Implementation as the minimum Project model, **must not** require an Implementation Atom, **and** **may** enable other Atom roles, applicability tiers, descendant scopes, **or** automation **only** **when** necessary. Scope Unit ancestry remains parent-declaration data; no Structural Level property is required.
