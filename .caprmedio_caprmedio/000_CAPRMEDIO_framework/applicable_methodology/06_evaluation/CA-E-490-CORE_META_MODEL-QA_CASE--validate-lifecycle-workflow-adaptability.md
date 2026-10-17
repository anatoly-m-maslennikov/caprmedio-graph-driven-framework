---
subjects:
  governs: "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Workflow"
  depends_on:
    ["Entity", "Entity/Continuant/Object/Atom", "Atom/Content Role", "Type", "Status", "Entity/Continuant/Object/Scope Unit", "Container Atom", "Entity/Carrier"]
version: 7
updated_at: "2026-10-15 23:50:15 +0400"
relations: {"evaluation_for": ["CA-R-1521"]}
atom_id: "CA-E-490"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/06_evaluation/CA-E-490-CORE_META_MODEL-QA_CASE--validate-lifecycle-workflow-adaptability.md
  source_atom_id: CA-E-490
  source_atom_revision: 7
  source_sha256: 478e3d37ed145ec7cb638ddbadfa6eab7f7260800efff1af9b9ef0d46e5c6009
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Validate lifecycle Workflow adaptability

## Scope

a status-change Workflow **and** its target Entity's applicable model.

## Claim

the Evaluation **must** check that a status-change Workflow follows the target Entity's applicable model under CA-R-1521.

## Details

- supply **`=2`** applicable status models with different admitted values, including a newly admitted value absent from the original model; the same Workflow definition **must** support their admitted values. For Atom creation and explicit Atom Status updates, verify every value admitted by the qualified Content Role/Type model is selectable without a required intermediate Status or transition matrix.
- specialize an Atom's model by Content Role **and** Type; checking **only** a universal Atom value list fails.
- supply an applicable Scope Unit **or** Atom Collection model; admit its valid change **without** imposing an Atom lifecycle.
- request an unknown value or a change **without** a defined model: reject **without** inventing a value **or** bypassing required Carrier behavior. For a non-Atom Entity model that defines transition conditions, reject its prohibited transition; do not apply that matrix as an Atom Status gate. Preserve ordinary schema, identity/collision, expected-source/currentness, permission and Carrier safeguards.
- supply a model requiring an unsupported capability: require an explicit limitation rather than a false pass.

these cases validate the methodology definition; an executor requires separate Implementation checks.
