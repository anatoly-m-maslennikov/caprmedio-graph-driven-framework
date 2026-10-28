---
atom_id: CA-O-146@13
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step//Source Reconciliation Selection Step'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Continuant/Scope Unit//PROJECT_CONFIGURATION
  - Subject/Graph Node/Domain/Occurrent/Execution/Step Run.Agentic Step Execution Context
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Domain/Occurrent/Execution/Step Run
version: 13
updated_at: 2026-10-26 05:59:45 +0400
relations: {}
tier: 3
---
# Summary

Select the reconciliation source frontier

## Operation

Source Reconciliation Selection Step **means** the node **in** Workflow `CA-O-010` invoking **`=1`** Action, `CA-O-004`.

- bind the requested source selection **and** applicable source authority from the admitted Workflow Run inputs. retain the exact proposal, decision **and** source-frontier bindings supplied for this invocation, **when** applicable, rather than independently selecting **or** inferring them.
- for an invocation whose actual bound Action is Agentic, bind **`=1`** Integrated **or** Isolated context under `CA-R-1527-CORE_META_MODEL-GENERAL-REQUIREMENT--define-agentic-step-execution-context` from the admitted invocation's supplied `agentic_execution_context` runtime parameter **before** dispatch. missing, ambiguous **or** unsupported values, **or** unavailable required context/capability, return a blocked Agentic invocation; do **not** default **or** silently substitute. retain the selected context with the Step Run. this does **not** grant additional authority. a Programmatic invocation does **not** acquire an Agent context.
- retain exact Action/Step Revisions, input/source bindings, actual effects **and** returned results for the Step Run. pass the Action's unchanged result **and** payload **to** the Workflow **without** copying **or** redefining its behavior.
- remain within the Workflow's applicable approval, currentness, confidence, accepted revisit/recovery allowance **and** escalation guards. this Step does **not** authorize an extra retry, correction, publication, **or** decision.

## Details
