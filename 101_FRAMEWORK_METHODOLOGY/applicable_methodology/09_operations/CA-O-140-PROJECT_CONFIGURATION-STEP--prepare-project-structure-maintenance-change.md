---
atom_id: CA-O-140
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Project Structure Maintenance Preparation Step"
  depends_on: ["Entity/Continuant/Object/Atom/Content Role: Operations/Type: Step", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Workflow", "Entity/Occurrent/Execution/Workflow Run", "Entity/Occurrent/Execution/Step Run", "Agentic Step Execution Context"]
version: 5
updated_at: "2026-10-18 16:25:48 +0400"
relations:
  relates_to: [CA-O-015, CA-O-012, CA-O-139, CA-R-1509, CA-R-1510, CA-R-1511, CA-R-1527]
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-140-PROJECT_CONFIGURATION-STEP--prepare-project-structure-maintenance-change.md
  source_atom_id: CA-O-140
  source_atom_revision: 5
  source_sha256: 47ef970994d473a79b841bad3d09fdd04274d923226dd1acdcdea1af24c5c839
  original_relations_sha256: f814cbea998ed9ed755793a97dd77377d892bc42a447d4ef31cdf1510f4cbb35
---
# Summary

Prepare project structure maintenance change

## Operation

Project Structure Maintenance Preparation Step **means** the node **in** the owning Workflow CA-O-015 that invokes **=1** existing Action, CA-O-012, with the following bindings.

| Required input or parameter | Bound source |
| --- | --- |
| Selected current state | CA-O-139's returned exact source identities and Revisions. |
| Requested structural change | The same CA-O-015 Workflow Run's admitted request, including the requested creation, rename, reparenting, reorder, path rebinding, removal, or reconciliation. |

For an invocation whose actual bound Action is Agentic, bind **=1** Integrated **or** Isolated context under CA-R-1527 from the admitted invocation's supplied `agentic_execution_context` runtime parameter **before** dispatch. Missing, ambiguous **or** unsupported values, **or** unavailable required context/capability, block that Agentic invocation; do **not** default **or** silently substitute. A Programmatic invocation does **not** acquire an Agent context. Applicable authority, permissions and remaining retry allowance come from the same Workflow Run; the binding grants no additional authority.

Return the referenced Action's exact result **to** CA-O-015 **without** copying **or** redefining the Action's behavior, changing its outcome, **or** choosing the next Step here. CA-O-015 owns every transition and terminal guard. Retain the exact Action/Step Revisions, input/result source identities, actual effects and resolved context with the Step Run under CA-R-1510/CA-R-1511; a source definition is **not** evidence of an executed Run.

## Details
