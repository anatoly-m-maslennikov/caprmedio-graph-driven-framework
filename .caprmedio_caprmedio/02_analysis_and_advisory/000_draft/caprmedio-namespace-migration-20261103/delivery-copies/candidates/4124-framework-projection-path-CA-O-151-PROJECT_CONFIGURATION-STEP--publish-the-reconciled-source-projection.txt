---
atom_id: CA-O-151
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/caprmedio/Step//Source Reconciliation Publication Step
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit//PROJECT_CONFIGURATION
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run.Agentic Step Execution Context
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run
version: 14
updated_at: 2026-10-27 19:59:47 +0400
relations: {}
tier: 3
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-010-PROJECT_CONFIGURATION-WORKFLOW--reconcile-sources/CA-O-151-PROJECT_CONFIGURATION-STEP--publish-the-reconciled-source-projection.md
  source_atom_id: CA-O-151
  source_atom_revision: 14
  source_sha256: c534e65b0e13c79e8bbed8641a5222fe58b9e9295cee91fb4eee308683e77c92
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Publish the reconciled source projection

## Operation

Source Reconciliation Publication Step **means** the node **in** Workflow `CA-O-010` invoking **`=1`** Action, `CA-O-009`.

- bind the final assessed frontier, valid decisions, **and** selected Projection Delivery authority from CA-O-147's current assessment result, applicable retained CA-O-149 decisions, **and** admitted Workflow Run Delivery inputs. retain the exact proposal, decision **and** source-frontier bindings supplied for this invocation, **when** applicable, rather than independently selecting **or** inferring them.
- for an invocation whose actual bound Action is Agentic, bind **`=1`** Integrated **or** Isolated context under `CA-R-1527-CORE_META_MODEL-GENERAL-REQUIREMENT--define-agentic-step-execution-context` from the admitted invocation's supplied `agentic_execution_context` runtime parameter **before** dispatch. missing, ambiguous **or** unsupported values, **or** unavailable required context/capability, return a blocked Agentic invocation; do **not** default **or** silently substitute. retain the selected context with the Step Run. this does **not** grant additional authority. a Programmatic invocation does **not** acquire an Agent context.
- retain exact Action/Step Revisions, input/source bindings, actual effects **and** returned results for the Step Run. pass the Action's unchanged result **and** payload **to** the Workflow **without** copying **or** redefining its behavior.
- remain within the Workflow's applicable approval, currentness, confidence, accepted revisit/recovery allowance **and** escalation guards. this Step does **not** authorize an extra retry, correction, publication, **or** decision.

## Details
