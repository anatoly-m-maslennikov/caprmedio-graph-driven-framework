---
subjects:
  governs: Label
  depends_on:
  - Subject/Domain/Node/Continuant/Scope Unit.Label
  - Scope Unit/Type
  - 'Entity/Node/Continuant/Atom/Content Role: Plan.Label'
  - Plan Blocking Relations
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan/Type: Plan'
  - Entity
  - Property
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
version: 10
updated_at: 2026-10-24 00:38:25 +0400
relations:
  evaluation_for:
  - CA-R-1594
  - CA-R-972
  - CA-R-1576
  - CA-R-1577
  - CA-R-982
atom_id: CA-E-505@10
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: QA Case
tier: 3
---
# Summary

Validate shared Label semantics

## Scope

a qualified use of Label under shared Label semantics.

## Claim

the Label Evaluation **must** reject a qualified use of Label that changes the shared meaning under CA-R-1594.

## Details

### cases

- change **only** a Scope Unit Label among Layer, Feature, **and** Superlayer; retain its identity, declared Type, parentage, Local Order, authority, **and** Relation semantics.
- change **only** a Plan Label among Version, Objective, Epic, Task, **and** Subtask; retain its identity, Type, authoring Subtype, completion conditions, decomposition, **and** blocking.
- resolve `Scope Unit/Label` **and** `Atom/Content Role: Plan/Type: Plan/Label` as distinct bearer-qualified Properties using **`=1`** shared Label definition, **not** incompatible meanings of the same Term.
- reject inferring an authoring Subtype, required workflow, Status, **or** execution dependency from Label spelling alone.
- accept a Label value that matches a Type **or** Subtype name **only** as a navigation value; any classification still requires its separately governed source.
- retain bearer-specific cardinality, defaults, **and** Carrier encoding under their own authority; the shared definition **must not** require a Label on **every** Entity **or** create a new field **in** existing Carriers.

report the bearer, Label value, **and** wrongly inferred fact **without** silently changing the source Entity.
