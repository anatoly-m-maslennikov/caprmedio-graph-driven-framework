---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Role:=Operations)/Workflow
  passive:
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Role
  - CAPRMEDIO_MODEL <+ Scope Unit.order.ordered
  - CAPRMEDIO_MODEL <+ Atom.Status
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Carrier
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
