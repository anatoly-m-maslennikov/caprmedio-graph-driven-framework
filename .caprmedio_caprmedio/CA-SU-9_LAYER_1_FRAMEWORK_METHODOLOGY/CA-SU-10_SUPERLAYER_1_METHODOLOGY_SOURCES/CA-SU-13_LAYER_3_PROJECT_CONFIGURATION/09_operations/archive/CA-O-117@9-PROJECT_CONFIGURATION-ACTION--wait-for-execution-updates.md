---
atom_id: CA-O-117@9
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-25 17:32:27 +0400
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  depends_on:
  - Subject/Graph Node/Engineering/Programmatic Action/Execution Notification Adapter
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Engineering/Journal Event Query
relations:
  relates_to:
  - CA-R-1809
  - CA-D-517
tier: 3
---
# Summary

Wait for execution updates

## Operation

Execution notifications **means** the Programmatic Action implementing the following responsibility:

- compare snapshots of existing saved evidence; replay confirmed Journal updates after the cursor, await changes asynchronously, and distinguish unconfirmed event recording.
- accept the declared inputs **and** return the declared results under CA-D-517-WATCH_EXECUTION-ENG_DECISION--encode-watch-execution-tool-binding.
- report missing **or** ambiguous evidence as an explicit result.
- execution requires an Operator-authorized invocation; discovery **or** observation grants no mutation authority.

## Details

this Action provides the responsibility named by its Summary. a Workflow **may** invoke the Action through a Step. a direct call **may** use the same Action **without** creating a Workflow Run. observation preserves the original Run **and** evidence.
