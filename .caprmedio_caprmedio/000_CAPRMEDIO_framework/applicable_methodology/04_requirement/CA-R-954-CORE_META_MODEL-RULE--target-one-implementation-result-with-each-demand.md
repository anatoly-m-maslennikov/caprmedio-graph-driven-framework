---
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Demand)'
  passive:
  - CAPRMEDIO_MODEL <+ Package/Implementation
version: 33
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-933
atom_id: CA-R-954
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 6
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-954-CORE_META_MODEL-RULE--target-one-implementation-result-with-each-demand.md
  source_atom_id: CA-R-954
  source_atom_revision: 33
  source_sha256: 52eb4fac30d8602fb3e4ffd940f192e868b9f2a96fa5334ba279df0ea367ee11
  original_relations_sha256: c28d84bac21e6f7cc7bfde47da5b055ffadede71bf17c4da3c8b2456c1f525ea
---
## Summary
Target one Implementation result with each Demand

## Claim

### Prose Claim


Demand Atoms.


**every** Demand Atom **must** constrain **`=1`** Implementation result produced by its Claim Scope.
