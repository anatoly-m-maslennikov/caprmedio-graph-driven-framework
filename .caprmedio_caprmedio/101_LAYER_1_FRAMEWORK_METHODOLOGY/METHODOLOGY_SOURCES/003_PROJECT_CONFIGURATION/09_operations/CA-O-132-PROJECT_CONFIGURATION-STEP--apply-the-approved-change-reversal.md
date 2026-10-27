---
atom_id: CA-O-132
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step//Approved Change Reversal Step'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Domain/Occurrent/Execution/Step Run
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
version: 11
updated_at: 2026-10-26 05:59:45 +0400
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
