---
atom_id: CA-E-207
ref_id: CA-E-207
container:
  scope_unit: CA-SU-13
role: Evaluation
form: Eval Policy
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//PROJECT_PRIORITY_MODEL
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//PROJECT_PRIORITY_MODEL
  - "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Effect Authorization"
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Selection
  - CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//PROJECT_LEXICOGRAPHIC
tier: 5
relations:
  child_of:
  - CA-R-815
  evaluation_for:
  - CA-R-1487
  - CA-M-297
  - CA-O-022
  - CA-O-023
status: Active
version: 36
updated_at: 2026-11-02 18:35:20 +0400
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/06_evaluation/CA-E-207-PROJECT_CONFIGURATION-POLICY--evaluate-priority-governed-alternative-selection.md
  source_atom_id: CA-E-207
  source_atom_revision: 36
  source_sha256: 80055bb86b9b5c6497fa5bdf395529ba00f19238fab4815e2a18f6ce1c5f6d4e
  original_relations_sha256: 138571c13f61515d1b51d847f0f383e37a505e5b98594d4320901c31466eecd0
---
## Summary

Evaluate priority-governed alternative selection

## Claim

### Prose Claim


this Evaluation checks priority resolution **and** alternative selection for an affected Scope **and** Project stage under CA-R-1487, CA-M-297, CA-O-022, **and** CA-O-023.


the evaluated behavior passes **if** **all** applicable conditions hold **and** are supported by the evaluated evidence:

- the effective model **and** parameters correspond **to** applicable Operator input; unresolved input is reported **without** activating an invented model **or** preference.
- **every** selected alternative satisfies active authority **and** non-negotiable constraints.
- selection follows the Operator-selected model **without** substituting another algorithm.
- for comparison by priority order, the first deciding criterion governs relative preference; later criteria do **not** reverse it **or** bypass an unresolved earlier comparison.
- a tie **or** incomparable result is **not** converted into an automatic winner **without** authority from the selected model.
- unresolved input **or** comparison is returned **to** the Operator with its known inputs, alternatives **when** available, constraints, evidence, **and** exact unresolved point.

### Falsification

the evaluated behavior fails **if** **any** applicable acceptance condition is false. missing evidence for an applicable condition leaves that condition unevaluated, **not** passed.
