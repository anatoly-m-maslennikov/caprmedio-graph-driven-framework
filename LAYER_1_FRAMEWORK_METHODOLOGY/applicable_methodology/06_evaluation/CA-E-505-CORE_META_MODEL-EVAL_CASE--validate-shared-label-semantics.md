---
atom_id: CA-E-505
ref_id: CA-E-505
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit.Label
  - CAPRMEDIO_MODEL <+ Scope Unit.order.ordered
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role: Plan)/(.Header.Form: Plan).Header.Label'
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//BLOCKS
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role: Plan)/(.Header.Form: Plan)'
  - CAPRMEDIO_MODEL <+ Term//Property
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
tier: 3
relations:
  evaluation_for:
  - CA-R-2705
  - CA-R-2528
  - CA-R-1576@21
  - CA-R-1577
status: Active
version: 22
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-E-505-CORE_META_MODEL-EVAL_CASE--validate-shared-label-semantics.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-505-CORE_META_MODEL-EVAL_CASE--validate-shared-label-semantics.md
  source_atom_id: CA-E-505
  source_atom_revision: 22
  source_sha256: 7692c36cacba04c85da8f3bb619e30655f480c474a124b0ada6b53414cdae98c
  original_relations_sha256: d1861630b40d29dc993c79566cff3e52b0d91a98d38a089791a31ee7469a5e27
---
## Summary

Validate shared Label semantics

## Claim

### Prose Claim


a qualified use of Label under shared Label semantics.


the Label Evaluation **must** reject a qualified use of Label that changes the shared meaning under CA-R-2705.

## Details

### cases

- change **only** a Scope Unit Label among Layer, Feature, **and** Superlayer; retain its identity, declared Type, parentage, Local Order, authority, **and** Relation semantics.
- change **only** a Plan Label among Version, Objective, Epic, Task, **and** Subtask; retain its identity, Type, authoring Subtype, completion conditions, decomposition, **and** blocking.
- resolve `Entity/Object/Continuant/Structural Unit/Scope Unit.Label` **and** `Atom/(.Header.Role: Plan)/(.Header.Form: Plan).Header.Label` as distinct bearer-qualified Properties using **`=1`** shared Label definition, **not** incompatible meanings of the same Term.
- reject inferring an authoring Subtype, required workflow, Status, **or** execution dependency from Label spelling alone.
- accept a Label value that matches a Type **or** Subtype name **only** as a navigation value; any classification still requires its separately governed source.
- retain bearer-specific cardinality, defaults, **and** Carrier encoding under their own authority; the shared definition **must not** require a Label on **every** Entity **or** create a new field **in** existing Carriers.

report the bearer, Label value, **and** wrongly inferred fact **without** silently changing the source Entity.
