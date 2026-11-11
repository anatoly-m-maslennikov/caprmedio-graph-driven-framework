---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom/(.Role:=Operations)/Workflow
  passive:
  - CAPRMEDIO <+ MODEL <+ Entity
  - CAPRMEDIO <+ MODEL <+ Atom
  - CAPRMEDIO <+ MODEL <+ Atom.Role
  - CAPRMEDIO <+ MODEL <+ Scope Unit.order.ordered
  - CAPRMEDIO <+ MODEL <+ Atom.Status
  - CAPRMEDIO <+ MODEL <+ Scope Unit
  - CAPRMEDIO <+ MODEL <+ Carrier
version: 24
updated_at: 2026-11-02 19:44:26 +0400
relations:
  evaluation_for:
  - CA-R-1521
atom_id: CA-E-490
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Evaluation
form: Eval Case
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-490-CORE_META_MODEL-EVAL_CASE--validate-lifecycle-workflow-adaptability.md
  source_atom_id: CA-E-490
  source_atom_revision: 24
  source_sha256: 881d62c71da31070348d3409fef370e0ef53f624e85de14ad4d8c8bd5ea925fd
  original_relations_sha256: 535748283daec9e9470aa5758cb1714fa6f3dc0bcbab21b02d0044285bbb6a5b
---
## Summary

Validate lifecycle Workflow adaptability

## Claim scope

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
