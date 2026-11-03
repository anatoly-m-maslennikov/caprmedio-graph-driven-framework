---
atom_id: CA-O-132
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject/caprmedio/Step//Approved Change Reversal Step
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Step Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
version: 12
updated_at: 2026-10-27 19:59:46 +0400
relations: {}
tier: 3
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
