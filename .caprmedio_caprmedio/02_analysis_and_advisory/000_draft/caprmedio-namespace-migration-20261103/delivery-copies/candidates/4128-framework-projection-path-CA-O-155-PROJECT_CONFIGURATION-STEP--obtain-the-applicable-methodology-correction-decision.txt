---
atom_id: CA-O-155
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
version: 15
updated_at: 2026-10-27 19:59:47 +0400
subjects:
  governs: Subject/caprmedio/Step//Applicable Methodology Compilation Decide Step
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Applicable Methodology'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit//PROJECT_CONFIGURATION
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit.Expansion Boundary
relations: {}
tier: 3
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-011-PROJECT_CONFIGURATION-WORKFLOW--bind-source-reconciliation-to-applicable-methodology/CA-O-155-PROJECT_CONFIGURATION-STEP--obtain-the-applicable-methodology-correction-decision.md
  source_atom_id: CA-O-155
  source_atom_revision: 15
  source_sha256: 3ecdb627d5619c49977517b66d155e4235b97a740b74784df019d21e06cf2d29
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
