---
atom_id: CA-R-1683
ref_id: CA-R-1683
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Selection
  - CAPRMEDIO_MODEL <+ Atom.Header.Role
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/History
  - CAPRMEDIO_MODEL <+ Package/Project Package
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Action)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow)
  - CAPRMEDIO_MODEL <+ Actor
  - CAPRMEDIO_MODEL <+ Event Record
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
tier: 1
relations:
  child_of:
  - CA-M-447
status: Active
version: 46
updated_at: 2026-11-10 14:38:45 +0400
carrier_destination:
  file:
    name: CA-R-1683-CORE_META_MODEL--authority-evaluation-and-operations-remain-distinct.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1683-CORE_META_MODEL--authority-evaluation-and-operations-remain-distinct.md
  source_atom_id: CA-R-1683
  source_atom_revision: 46
  source_sha256: 2071c5d049ef992e266c5071ea466861768b02b26df595f0ac1865aca2636929
  original_relations_sha256: cda81380ab057c4da428dab72b93f65bb72092983ee69756870fff6e5dc9bea9
---
## Summary

Authority, Evaluation, and Operations remain distinct

## Claim

### Prose Claim


RMED Spec authority, CAPO Change content, concrete Implementation, actual executions, Verification judgments.


CAPRMEDIO **must** distinguish RMED Spec authority for governed Entities; CAPO Change content under CA-R-1549@21, including specific reusable Operations definitions under CA-R-2463; concrete Implementation; actual executions **and** their Journal Records carrying facts, state changes, **and** Claim-bound evidence; **and** Verification judgments about sufficiency **and** currentness. Evaluation results, evidence, dashboards, **and** Verification judgments **may** support, challenge, **or** invalidate reliance on a Claim, but **must not** themselves establish, edit, replace, **or** override semantic authority.
