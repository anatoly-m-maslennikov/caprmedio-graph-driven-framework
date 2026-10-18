---
version: 15
updated_at: "2026-10-15 18:48:50 +0000"
relations:
  child_of:
    - CA-R-815
  evaluation_for:
    - CA-R-1487
    - CA-M-297
    - CA-O-022
    - CA-O-023
subjects:
  governs: "Project Priority Model Application"
  depends_on:
    ["Entity/Continuant/Actor/Type: Operator", "Scope", "Entity/Continuant/Object/Project", "CAPRMEDIO Framework Instance", "Resolve Operator Priorities", "Select Priority-Governed Alternative", "Project Lexicographic Selection"]
atom_id: "CA-E-207"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/06_evaluation/CA-E-207-CORE_META_MODEL-EVALUATION_APPROACH--evaluate-priority-governed-alternative-selection.md
  source_atom_id: CA-E-207
  source_atom_revision: 15
  source_sha256: a2c83b2fe141595ac59cac0b4168e6e6f80ae278d42b61c2c80f204555ea3750
  original_relations_sha256: e2be46359af7cbd5714136dddbc8fa3c5ca2d5156bc6d596b2921d2bb081b0f2
---
# Summary

Evaluate priority-governed alternative selection

## Scope

this Evaluation checks priority resolution **and** alternative selection for an affected Scope **and** Project stage under CA-R-1487, CA-M-297, CA-O-022, **and** CA-O-023.

## Claim

the evaluated behavior passes **if** **all** applicable conditions hold **and** are supported by the evaluated evidence:

- the effective model **and** parameters correspond **to** applicable Operator input; unresolved input is reported **without** activating an invented model **or** preference.
- **every** selected alternative satisfies active authority **and** non-negotiable constraints.
- selection follows the Operator-selected model **without** substituting another algorithm.
- for comparison by priority order, the first deciding criterion governs relative preference; later criteria do **not** reverse it **or** bypass an unresolved earlier comparison.
- a tie **or** incomparable result is **not** converted into an automatic winner **without** authority from the selected model.
- unresolved input **or** comparison is returned **to** the Operator with its known inputs, alternatives **when** available, constraints, evidence, **and** exact unresolved point.

### Falsification

the evaluated behavior fails **if** **any** applicable acceptance condition is false. missing evidence for an applicable condition leaves that condition unevaluated, **not** passed.

## Details
