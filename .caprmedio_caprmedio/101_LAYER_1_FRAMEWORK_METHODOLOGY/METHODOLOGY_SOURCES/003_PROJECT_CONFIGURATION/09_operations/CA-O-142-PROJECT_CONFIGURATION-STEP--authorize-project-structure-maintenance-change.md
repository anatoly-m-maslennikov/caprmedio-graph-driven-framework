---
atom_id: CA-O-142
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Active
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step//Project Structure Maintenance Authorization Step'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Domain/Occurrent/Execution/Step Run
  - Subject/Graph Node/Domain/Occurrent/Execution/Step Run.Agentic Step Execution Context
version: 13
updated_at: 2026-10-26 05:59:45 +0400
relations: {}
tier: 3
---
# Summary

Authorize project structure maintenance change

## Operation

Project Structure Maintenance Authorization Step **means** the node **in** the owning Workflow CA-O-015 that invokes **=1** existing Action, CA-O-013, with the following bindings.

| Required input or parameter | Bound source |
| --- | --- |
| Assessed proposal and exact effects | CA-O-140's exact proposal together with CA-O-141's returned assessment of that proposal. |
| Current state and applicable authorization/confidence threshold | CA-O-139's retained selected source identities/Revisions and the same Workflow Run's actual Operator authorization and effective Autonomous Confidence Threshold. |

For an invocation whose actual bound Action is Agentic, bind **=1** Integrated **or** Isolated context under CA-R-1527 from the admitted invocation's supplied `agentic_execution_context` runtime parameter **before** dispatch. Missing, ambiguous **or** unsupported values, **or** unavailable required context/capability, block that Agentic invocation; do **not** default **or** silently substitute. A Programmatic invocation does **not** acquire an Agent context. Applicable authority, permissions and remaining retry allowance come from the same Workflow Run; the binding grants no additional authority.

Return the referenced Action's exact result **to** CA-O-015 **without** copying **or** redefining the Action's behavior, changing its outcome, **or** choosing the next Step here. CA-O-015 owns every transition and terminal guard. Retain the exact Action/Step Revisions, input/result source identities, actual effects and resolved context with the Step Run under CA-R-1510/CA-R-1511; a source definition is **not** evidence of an executed Run.

## Details
