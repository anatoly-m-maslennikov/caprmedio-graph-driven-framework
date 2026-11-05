---
subjects:
  active: CAPRMEDIO_MODEL <+ Entity
  passive:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Selection
  - CAPRMEDIO_MODEL <+ Atom.Header.Role
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/History
  - CAPRMEDIO_MODEL <+ Package/Implementation
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Action)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow)'
  - CAPRMEDIO_MODEL <+ Actor
  - CAPRMEDIO_MODEL <+ Event Record
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
version: 45
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-M-447
atom_id: CA-R-1683
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1683-CORE_META_MODEL--authority-evaluation-and-operations-remain-distinct.md
  source_atom_id: CA-R-1683
  source_atom_revision: 45
  source_sha256: cfa24e7a5a41ff45b3f525cd0635e4577f940c1a611d36a939881c6ed05a4739
  original_relations_sha256: cda81380ab057c4da428dab72b93f65bb72092983ee69756870fff6e5dc9bea9
---
## Summary

Authority, Evaluation, and Operations remain distinct

## Claim

### Prose Claim


RMED Spec authority, CAPO Change content, concrete Implementation, actual executions, Verification judgments.


CAPRMEDIO **must** distinguish RMED Spec authority for governed Entities; CAPO Change content under CA-R-1549@21, including specific reusable Operations definitions under CA-R-2463; concrete Implementation; actual executions **and** their Journal Records carrying facts, state changes, **and** Claim-bound evidence; **and** Verification judgments about sufficiency **and** currentness. Evaluation results, evidence, dashboards, **and** Verification judgments **may** support, challenge, **or** invalidate reliance on a Claim, but **must not** themselves establish, edit, replace, **or** override semantic authority.
