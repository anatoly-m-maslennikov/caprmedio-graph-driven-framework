---
atom_id: CA-O-132
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Approved Change Reversal Step"
  depends_on: ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Entity/Node/Occurrent/Execution/Workflow Run", "Entity/Node/Occurrent/Execution/Step Run", "Entity/Node/Continuant/History/Journal", "Entity/Node/Continuant/Actor/Type: Operator"]
version: 5
updated_at: "2026-10-19 15:57:02 +0400"
relations:
  relates_to: [CA-O-131, CA-R-1509, CA-R-1511, CA-R-1525]
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-132-PROJECT_CONFIGURATION-STEP--apply-the-approved-change-reversal.md
  source_atom_id: CA-O-132
  source_atom_revision: 5
  source_sha256: 680180ec22e73d843e6c1aeb6736b80012ed8a4b55b58ba0dd6b67f626ebeed3
  original_relations_sha256: 6f7f7cc249c91076c76d7f2d48c992dd9d3cd18f48aeaf727f6b21263d16a98b
---
# Summary

Apply the approved change reversal

## Operation

Approved Change Reversal Step **means** the Workflow node invoking **=1** Action, CA-O-131, as a Programmatic invocation.

Bind **all** inputs from the admitted Workflow request **and**, on recovery, its preserved execution evidence:

- selected accepted change/event/Revision references and original before/after evidence;
- exact target identities, admitted current Carrier/state and already-satisfied-result/no-op conditions and affected references;
- proposed ordered reversal effects, expected resulting state and applicable current identity/status/Carrier authority;
- recorded Operator decision for those exact effects and the admitted recovery/cancellation boundary;
- authorized executor permissions/capabilities, canonical Project Journal and durable evidence location;
- exact Workflow/Step/Action definition Revisions, distinct Workflow/Step/Action Run identities, parent lineage and completed/pending/uncertain effect and recording receipts.

Return the Action's actual result **and** effect/evidence account unchanged **to** CA-O-130's terminal routing. this binding neither redefines reversal behavior **nor** infers approval from dispatch.

## Details

Missing input, unsupported capability **or** unresolved exact binding blocks invocation rather than substituting guessed values. Programmatic execution requires no Agentic Integrated/Isolated context; an executor that delegates judgment **to** an AI Agent cannot silently treat that delegation as this Programmatic binding.

Retain the actual Step Run, referenced Action Run, definition Revisions, parent Workflow Run, supplied inputs, returned outcome **and** evidence references under current execution/Journal authority. a delivery attempt **or** Tool call is **not** by itself another Step Run. recording failures **and** partial effects survive the handoff; the Step does **not** rerun a completed Action **to** reconstruct missing Journal evidence.
