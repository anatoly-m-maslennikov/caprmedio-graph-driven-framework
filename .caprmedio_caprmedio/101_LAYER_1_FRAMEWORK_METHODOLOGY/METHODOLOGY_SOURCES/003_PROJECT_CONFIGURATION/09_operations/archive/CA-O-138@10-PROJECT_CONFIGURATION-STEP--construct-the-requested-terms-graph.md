---
atom_id: CA-O-138@10
content_role: Operations
type: Step
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step//Terms Graph Construction Step'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Domain/Occurrent/Execution/Step Run
  - Subject/Graph Node/Domain/Occurrent/Execution/Step Run.Agentic Step Execution Context
  - 'Subject/Graph Node/Domain/Continuant/Projection/Type: Terms Graph'
version: 10
updated_at: 2026-10-25 17:32:27 +0400
relations:
  relates_to:
  - CA-O-136
  - CA-O-137
  - CA-R-1509
  - CA-R-1525
  - CA-R-1526
  - CA-R-1527
tier: 3
---
# Summary

Construct the requested Terms Graph

## Operation

Terms Graph Construction Step **means** the node of CA-O-136 invoking **=1** Action, CA-O-137, with graph kind fixed **to** Terms Graph.

- bind the Action's admitted request, exact source selection, narrower/governed-only view selection **if** any, current authoritative source set, governing Term/Relation Kind authority, representation configuration, target Projection/output destination **and** existing Projection/evidence from the corresponding Workflow invocation inputs.
- bind permissions, admitted realization/execution kind **and** recording context from that invocation's current admitted execution context. retain actual Workflow/Step/Action definition Revisions **and** actual Run/parent references; no earlier completed Run **or** projected state supplies missing inputs.
- resolve execution kind under CA-R-1526. for an Agentic invocation, bind **=1** Integrated **or** Isolated context from the explicitly supplied Workflow runtime parameter under CA-R-1527; for Programmatic execution, no Agent context is selected. missing input, capability, permission **or** Agentic context blocks dispatch rather than silent substitution.
- return the Action's exact result/effects/evidence **to** CA-O-136 **without** copying construction behavior, changing scope, repairing sources **or** turning internal Tool calls into Steps.

## Details

this reusable binding is distinct from its Step Run. separately placed Workflow/Step Carriers retain unambiguous references under CA-D-467.
