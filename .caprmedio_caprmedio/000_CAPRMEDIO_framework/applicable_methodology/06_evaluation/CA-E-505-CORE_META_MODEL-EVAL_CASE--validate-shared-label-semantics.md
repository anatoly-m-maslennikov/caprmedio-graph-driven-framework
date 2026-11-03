---
subjects:
  active: Entity
  passive:
  - Scope Unit.Label
  - Scope Unit.order.ordered
  - 'Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Plan)/(.Type:
    Plan).Label'
  - CFEL <+ Relation//BLOCKS
  - 'Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Plan)/(.Type:
    Plan)'
  - Term//Property
  - Entity/Object/Continuant/Actor/Operator
version: 22
updated_at: 2026-11-02 19:44:26 +0400
relations:
  evaluation_for:
  - CA-R-2497
  - CA-R-2528
  - CA-R-1576@21
  - CA-R-1577
atom_id: CA-E-505
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Evaluation
form: Eval Case
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-505-CORE_META_MODEL-EVAL_CASE--validate-shared-label-semantics.md
  source_atom_id: CA-E-505
  source_atom_revision: 22
  source_sha256: 8acb00ce8268b80c11f1d843ed80067b5235c43521d227c00ada47443498c67f
  original_relations_sha256: 4b967320e874c9a08b3d13403ff320bef5c397262cf25bf006209205090e8ac2
---
## Summary

Validate shared Label semantics

## Claim scope

a qualified use of Label under shared Label semantics.

## Claim

the Label Evaluation **must** reject a qualified use of Label that changes the shared meaning under CA-R-2497.

## Details

### cases

- change **only** a Scope Unit Label among Layer, Feature, **and** Superlayer; retain its identity, declared Type, parentage, Local Order, authority, **and** Relation semantics.
- change **only** a Plan Label among Version, Objective, Epic, Task, **and** Subtask; retain its identity, Type, authoring Subtype, completion conditions, decomposition, **and** blocking.
- resolve `Entity/Object/Continuant/Structural Unit/Scope Unit.Label` **and** `Entity/Object/Continuant/Governing Objects/Atom/(.Content Role: Plan)/(.Type: Plan).Label` as distinct bearer-qualified Properties using **`=1`** shared Label definition, **not** incompatible meanings of the same Term.
- reject inferring an authoring Subtype, required workflow, Status, **or** execution dependency from Label spelling alone.
- accept a Label value that matches a Type **or** Subtype name **only** as a navigation value; any classification still requires its separately governed source.
- retain bearer-specific cardinality, defaults, **and** Carrier encoding under their own authority; the shared definition **must not** require a Label on **every** Entity **or** create a new field **in** existing Carriers.

report the bearer, Label value, **and** wrongly inferred fact **without** silently changing the source Entity.
