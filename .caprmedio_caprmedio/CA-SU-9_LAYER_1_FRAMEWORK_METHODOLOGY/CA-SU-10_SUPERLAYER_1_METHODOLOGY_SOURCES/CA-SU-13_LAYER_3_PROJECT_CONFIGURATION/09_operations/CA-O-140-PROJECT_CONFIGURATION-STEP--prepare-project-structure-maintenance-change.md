---
atom_id: CA-O-140
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/caprmedio/Step//Project Structure Maintenance Preparation Step
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run.Agentic Step Execution Context
version: 13
updated_at: 2026-10-27 19:59:46 +0400
relations: {}
tier: 3
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
