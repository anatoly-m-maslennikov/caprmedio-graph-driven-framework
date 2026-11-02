---
atom_id: CA-O-155@12
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
version: 12
updated_at: 2026-10-24 00:51:05 +0400
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step//Applicable Methodology Compilation Decide Step'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - 'Subject/Domain/Node/Continuant/Projection/Type: Applicable Methodology'
  - Subject/Domain/Node/Continuant/Scope Unit//PROJECT_CONFIGURATION
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Domain/Node/Continuant/History/Journal.Record
  - Subject/Domain/Node/Continuant/Scope Unit.Expansion Boundary
relations:
  relates_to:
  - CA-O-011
  - CA-O-007
tier: 3
---
# Summary

Obtain the Applicable Methodology correction decision

## Operation

this Step is the decide node **of** CA-O-011, Applicable Methodology Compilation, invoking **`=1`** Action, CA-O-007, Obtain Source Correction Decision.

### Inputs and parameters

bind the exact proposal from CA-O-154, conflict and source-frontier digest from CA-O-153, and the Workflow Run's required Operator decision context with independently retained execution evidence.

enforce CA-R-1317 through CA-O-007: obtain **`=1`** unambiguous current actual Operator decision bound **to** the exact proposal, conflict, **and** source-frontier digest, and independently retain **and** verify it through admitted execution evidence. the Journal append is a business-provenance attempt; failure yields a `recording_error` diagnostic and does **not** qualify or disqualify the decision, block dispatch, **or** serve as proof, permission, completion, **or** recovery gate. stale, partial, missing, ambiguous, **or** mismatched decision does **not** qualify. do **not** create an approval Atom **in** Project Configuration; approval **must not** itself bypass Core expansion boundaries.

### Agentic invocation binding

for an invocation whose actual bound Action is Agentic, bind **`=1`** Integrated **or** Isolated context under CA-R-1527 from the admitted invocation's supplied `agentic_execution_context` runtime parameter **before** dispatch. missing, ambiguous **or** unsupported values, **or** unavailable required context/capability, block that Agentic invocation; do **not** default **or** silently substitute. retain the selected context with the Step Run. a Programmatic invocation does **not** acquire an Agent context **or** require this parameter. this binding grants no additional authority **and** does **not** change the Action's identity **or** behavior.

## Details
