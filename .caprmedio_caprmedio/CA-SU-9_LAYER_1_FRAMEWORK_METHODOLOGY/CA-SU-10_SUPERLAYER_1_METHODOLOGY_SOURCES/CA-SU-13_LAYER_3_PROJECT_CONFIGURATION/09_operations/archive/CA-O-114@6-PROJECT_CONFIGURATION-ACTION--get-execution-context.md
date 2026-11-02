---
atom_id: CA-O-114@6
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
version: 6
updated_at: 2026-10-24 00:51:05 +0400
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  depends_on:
  - Subject/Engineering/Programmatic Action/Execution Context Retrieval Adapter
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Implementation
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Subject/Domain/Node/Continuant/History/Journal
relations:
  relates_to:
  - CA-R-1806
  - CA-D-514
tier: 3
---
# Summary

Load the selected execution context

## Operation

Execution context retrieval **means** the Programmatic Action implementing the following responsibility:

- resolve exact identifiers; load the selected definition and directly related Step or Action definitions, relevant bound prompts, and applicable RMED from declared Scope Unit ancestry.
- accept the declared inputs **and** return the declared results under CA-D-514-GET_EXECUTION_CONTEXT--encode-get-execution-context-bindings.
- report missing **or** ambiguous evidence as an explicit result.
- execution requires an Operator-authorized invocation; discovery **or** observation grants no mutation authority.

## Details

this Action provides the responsibility named by its Summary. a Workflow **may** invoke the Action through a Step. a direct call **may** use the same Action **without** creating a Workflow Run. observation preserves the original Run **and** evidence.
