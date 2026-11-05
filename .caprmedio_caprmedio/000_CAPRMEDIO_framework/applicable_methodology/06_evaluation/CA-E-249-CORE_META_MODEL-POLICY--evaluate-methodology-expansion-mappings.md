---
atom_id: CA-E-249
ref_id: CA-E-249
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Policy
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit
  dependencies:
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//CORE_META_MODEL
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Atom.Header.Tier
tier: 3
relations:
  child_of:
  - CA-E-001
  evaluation_for:
  - CA-M-298
  - CA-R-1375
status: Active
version: 36
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-E-249-CORE_META_MODEL-EVAL_POLICY--evaluate-methodology-expansion-mappings.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-249-CORE_META_MODEL-POLICY--evaluate-methodology-expansion-mappings.md
  source_atom_id: CA-E-249
  source_atom_revision: 36
  source_sha256: bbb5c45ac11f8ade11121d4b5e4f61eeceb6939b7a1076048f47be83ff6869bd
  original_relations_sha256: 0e408119c14301165502ac987eef3c1bdf7e75d15e76577b578cb41d35fe1e01
---
## Summary

Evaluate methodology expansion mappings

## Claim

### Prose Claim


methodology expansion mappings.


a methodology expansion mapping Evaluation **must** return `fail` **if** a source element, exact canonical target, mapping rule, intended Scope, **or** applicable Core Meta-Model distinction at **any** numeric Tier is missing, canonical ownership is ambiguous, preservation is unproven, **or** the mapping redefines, replaces, shadows, weakens, deletes, contradicts, **or** reinterprets applicable Core Meta-Model authority at **any** numeric Tier; it **must** return `pass` **only** **when** the declared mapping preserves that authority **and** stays within its permitted expansion boundary. an Operator-approved loss **must not** count as conformance; report the failed boundary **and** leave the affected application stopped.
