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
  - CAPRMEDIO_MODEL <+ Atom.Header.Context.Tier
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
---
## Summary

Evaluate methodology expansion mappings

## Claim

### Prose Claim


methodology expansion mappings.


a methodology expansion mapping Evaluation **must** return `fail` **if** a source element, exact canonical target, mapping rule, intended Scope, **or** applicable Core Meta-Model distinction at **any** numeric Tier is missing, canonical ownership is ambiguous, preservation is unproven, **or** the mapping redefines, replaces, shadows, weakens, deletes, contradicts, **or** reinterprets applicable Core Meta-Model authority at **any** numeric Tier; it **must** return `pass` **only** **when** the declared mapping preserves that authority **and** stays within its permitted expansion boundary. an Operator-approved loss **must not** count as conformance; report the failed boundary **and** leave the affected application stopped.
