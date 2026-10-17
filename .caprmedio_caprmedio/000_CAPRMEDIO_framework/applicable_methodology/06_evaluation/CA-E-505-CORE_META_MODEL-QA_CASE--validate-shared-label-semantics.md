---
subjects:
  governs: "Label"
  depends_on:
    ["Entity/Continuant/Object/Scope Unit.Label", "Scope Unit/Type", "Entity/Continuant/Object/Atom/Content Role: Plan.Label", "Plan Blocking Relations", "Atom/Content Role: Plan/Type: Plan", "Entity", "Property", "Entity/Continuant/Actor/Type: Operator"]
version: 6
updated_at: "2026-10-15 18:50:14 +0000"
relations: {"evaluation_for": ["CA-R-1594", "CA-R-972", "CA-R-1576", "CA-R-1577", "CA-R-982"]}
atom_id: "CA-E-505"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/06_evaluation/CA-E-505-CORE_META_MODEL-QA_CASE--validate-shared-label-semantics.md
  source_atom_id: CA-E-505
  source_atom_revision: 6
  source_sha256: a94af847b6be57acc0a56fdb0f6e3a18cae8c4d4285e57c6ccc47c86e3628a71
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
