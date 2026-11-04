---
atom_id: CA-R-2482
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Declaration)
  passive:
  - CAPRMEDIO_MODEL <+ Atom
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2482-CORE_META_MODEL-RULE--declare-formal-scope.md
  source_atom_id: CA-R-2482
  source_atom_revision: 2
  source_sha256: 78bc2dfe9176d96df3c8dcd5f852467c241a027a5f526f8ee3efc171bf50b96e
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Formal Scope Independently of Scope Unit

## Claim

### Prose Claim


Formal Scope expressed by a Declaration.


- A formal Scope Declaration is contained outside the Scope Unit it constrains.
- It states permitted active and passive Subjects, Relations, endpoints and cardinalities.
- Its Subjects resolve in the applicable MODEL and PROJECT STRUCTURE instances.
- A Target Scope does not widen its granted permissions.
- The Declaration does not establish runtime behavior.

