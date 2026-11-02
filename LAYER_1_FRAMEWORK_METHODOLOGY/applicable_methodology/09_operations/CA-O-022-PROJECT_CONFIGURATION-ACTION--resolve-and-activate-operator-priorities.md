---
version: 11
updated_at: "2026-10-19 15:56:43 +0400"
relations:
  child_of:
    - CA-R-1487
subjects:
  governs: "Resolve Operator Priorities"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Entity/Node/Continuant/Actor/Type: Operator", "Entity/Node/Continuant/Project", "Scope", "CAPRMEDIO Framework Instance", "Project Priority Model Application"]
atom_id: "CA-O-022"
content_role: "Operations"
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Action"
global_tier: 11
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-022-PROJECT_CONFIGURATION-ACTION--resolve-and-activate-operator-priorities.md
  source_atom_id: CA-O-022
  source_atom_revision: 11
  source_sha256: e53a9dda7de8286cc94fbfef74922f4fdfbf638ae0a54cbc3d86d81b175e9a49
  original_relations_sha256: 6bed8d41cbd7d52168cdd7e51dd4f6908abe8e316b7f83b5bc478ba64412d785
---
# Summary

Resolve and activate Operator priorities

## Operation

Resolve Operator Priorities **means** the Action that turns applicable Operator input into the effective priority model for an identified Scope **and** Project stage.

### execution

1. identify the affected Scope **and** Project stage from the Operator input **and** its applicable context.
2. resolve the Operator-selected model, effective parameters, active criteria, applicable authority, **and** non-negotiable constraints. retain **every** applicable criterion **without** imposing a fixed catalog **or** comparison by priority order on another model.
3. check whether the input determines an admissible model **and** the parameters needed **to** apply it.
4. **if** that resolution succeeds, activate the resolved priorities **in** the CAPRMEDIO Framework Instance for the identified context **and** return them as the Action result.

### unresolved input

**if** the selected model, required parameters, authority, **or** context remains unresolved:

- present the known input **and** the exact unresolved point **to** the Operator.
- do **not** invent a model, infer a missing preference, **or** activate an unresolved change.
- report the Action as unresolved, **not** successfully completed.

## Details
