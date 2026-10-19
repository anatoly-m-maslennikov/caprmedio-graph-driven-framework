---
version: 7
updated_at: "2026-10-15 18:43:36 +0000"
relations:
  child_of:
    - CA-R-815
subjects:
  governs: "Project Priority Model Application"
  depends_on:
    ["Entity/Continuant/Actor/Type: Operator", "Entity/Continuant/Object/Project", "Scope", "CAPRMEDIO Framework Instance"]
atom_id: "CA-R-1487"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1487-CORE_META_MODEL-REQUIREMENT--follow-the-operator-selected-priority-model.md
  source_atom_id: CA-R-1487
  source_atom_revision: 7
  source_sha256: d1a65509eb9691faf5ced0251b045e0441ff94103e1910504e56bcee62cb4161
  original_relations_sha256: 60475cbfab2b85ec31fdd4b0596755416c2a92740bfc9f0249802043ebaa6619
---
# Summary

Follow the Operator-selected priority model

## Scope

priority-model selection by the CAPRMEDIO Framework Instance for an affected Scope and Project stage.

## Claim

the CAPRMEDIO Framework Instance **must** support the admissible priority model established by the Operator for the affected Scope **and** Project stage. **every** resulting alternative selection **must** satisfy **all** of the following:

- respect applicable authority **and** non-negotiable constraints.
- conform **to** that model, its effective parameters, **and** its active criteria **without** substituting another comparison algorithm.
- remain unresolved **if** the selected model **or** its application does **not** justify a selection.

## Details

the available criteria **and** comparison techniques remain extensible; no fixed criterion set **or** comparison by priority order is mandatory.
