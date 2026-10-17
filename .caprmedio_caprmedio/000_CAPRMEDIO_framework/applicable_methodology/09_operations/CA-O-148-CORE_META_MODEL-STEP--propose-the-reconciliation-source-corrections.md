---
atom_id: CA-O-148
content_role: Operations
type: Step
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Source Reconciliation Proposal Step"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Operations/Type: Step", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Source Reconciliation", "Agentic Step Execution Context", "Entity/Occurrent/Execution/Workflow Run", "Entity/Occurrent/Execution/Step Run"]
version: 5
updated_at: "2026-10-15 18:53:44 +0000"
relations:
  relates_to:
    - CA-O-010
    - CA-O-006
    - CA-R-1509
    - CA-R-1511
    - CA-R-1527
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/09_operations/CA-O-010-CORE_META_MODEL-WORKFLOW--reconcile-sources/CA-O-148-CORE_META_MODEL-STEP--propose-the-reconciliation-source-corrections.md
  source_atom_id: CA-O-148
  source_atom_revision: 5
  source_sha256: 4d11684331248570d93d4c7fb9e7abbf4698e0d2fcfaf1b1df930b2a6744849f
  original_relations_sha256: 39a7db74790d6bc0e67bda87f7a3d5e08fdf2383b111eb958f5f8b7b0e4162c7
---
# Summary

Propose the reconciliation source corrections

## Operation

Source Reconciliation Proposal Step **means** the node **in** Workflow `CA-O-010` invoking **`=1`** Action, `CA-O-006`.

- bind the assessed frontier, identified conflicts, **and** authorized correction boundaries from CA-O-147's assessment result **and** admitted Workflow Run authorization inputs. retain the exact proposal, decision **and** source-frontier bindings supplied for this invocation, **when** applicable, rather than independently selecting **or** inferring them.
- for an invocation whose actual bound Action is Agentic, bind **`=1`** Integrated **or** Isolated context under `CA-R-1527-CORE_META_MODEL-GENERAL-REQUIREMENT--define-agentic-step-execution-context` from the admitted invocation's supplied `agentic_execution_context` runtime parameter **before** dispatch. missing, ambiguous **or** unsupported values, **or** unavailable required context/capability, return a blocked Agentic invocation; do **not** default **or** silently substitute. retain the selected context with the Step Run. this does **not** grant additional authority. a Programmatic invocation does **not** acquire an Agent context.
- retain exact Action/Step Revisions, input/source bindings, actual effects **and** returned results for the Step Run. pass the Action's unchanged result **and** payload **to** the Workflow **without** copying **or** redefining its behavior.
- remain within the Workflow's applicable approval, currentness, confidence, accepted revisit/recovery allowance **and** escalation guards. this Step does **not** authorize an extra retry, correction, publication, **or** decision.

## Details
