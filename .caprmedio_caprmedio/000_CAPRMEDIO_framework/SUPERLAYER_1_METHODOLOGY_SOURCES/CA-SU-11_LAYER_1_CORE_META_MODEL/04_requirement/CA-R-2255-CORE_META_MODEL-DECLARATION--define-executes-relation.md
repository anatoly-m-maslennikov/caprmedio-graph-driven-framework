---
atom_id: CA-R-2255
ref_id: CA-R-2255
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//EXECUTES
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Runtime
  - CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Workflow Run
tier: 1
status: Active
version: 9
updated_at: 2026-11-03 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-2255-CORE_META_MODEL-DECLARATION--define-executes-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define EXECUTES Relation

## Claim

### Prose Claim

EXECUTES connects an actual Runtime to a Workflow Run it executes. The stored direction is Runtime to Workflow Run. IS_EXECUTED_BY is its declared derived inverse and is not a second stored fact.

The Host is an actual Runtime and the Target is the Workflow Run it executes.
Forward `Host ((EXECUTES)) Target` and reverse `Target <((EXECUTES)) Host` are views of the same Relation fact.
EXECUTES relates Runtime to Workflow Run.

#### Details
This named Type uses the general `((RELATION_TYPE))` form. It has no dedicated short Subject operator. This defines the reusable Type and its derived reverse view; it creates no Runtime or actual endpoint tuple.
### Formal Claim

```CFEL
# model
Relation//EXECUTES ((HAS_INVERSE)) Relation//IS_EXECUTED_BY;

Relation//EXECUTES ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
$runtime ((EXECUTES)) $workflow_run
```

