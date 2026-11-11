---
atom_id: CA-R-1990
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Enabled Relations.Contains'
  passive:
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom.Enabled Relations.Contains
relations:
  child_of:
  - CA-R-2478
version: 12
updated_at: 2026-11-02 00:18:22 +0400
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1990-CORE_META_MODEL-RULE--enable-containment-for-plan-atoms.md
  source_atom_id: CA-R-1990
  source_atom_revision: 12
  source_sha256: 73bce4ae3883eb1ae24b553205cd279a3991cd4099798e9dfa8ec4f94bc26853
  original_relations_sha256: 4fde62f0627e52833e954bbd64d451c404b9f9d66585c52603ef12fa5886adfa
---
## Summary

Enable containment for Plan Atoms

## Claim scope

Containment capability of Plan Atoms.

## Claim

`Atom/Content Role: Plan.Enabled Relations.Contains` **must** be True. a Plan Atom **may** contain other Plan Atoms.

## Details

Plan labels such as Epic, Task and Version do not create different containment Types. Containment is optional and can nest. This permission does not implement a Plan projection or replace other typed relations between Plans.
