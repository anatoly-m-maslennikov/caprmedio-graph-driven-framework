---
atom_id: CA-O-115@10
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
version: 10
updated_at: 2026-10-25 17:32:27 +0400
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  depends_on:
  - Subject/Graph Node/Engineering/Programmatic Action/Execution Observation Adapter
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Domain/Continuant/History/Journal
relations:
  relates_to:
  - CA-R-1807
  - CA-D-515
tier: 3
---
# Summary

Read execution status and saved results

## Operation

Execution observation **means** the Programmatic Action implementing the following responsibility:

- read the existing Run backend and saved reports; retain Action-to-Step correlation and never infer completion from an applied correction.
- accept the declared inputs **and** return the declared results under CA-D-515-GET_EXECUTION_STATUS-ENG_DECISION--encode-get-execution-status-tool-binding.
- report missing **or** ambiguous evidence as an explicit result.
- execution requires an Operator-authorized invocation; discovery **or** observation grants no mutation authority.

## Details

this Action provides the responsibility named by its Summary. a Workflow **may** invoke the Action through a Step. a direct call **may** use the same Action **without** creating a Workflow Run. observation preserves the original Run **and** evidence.
