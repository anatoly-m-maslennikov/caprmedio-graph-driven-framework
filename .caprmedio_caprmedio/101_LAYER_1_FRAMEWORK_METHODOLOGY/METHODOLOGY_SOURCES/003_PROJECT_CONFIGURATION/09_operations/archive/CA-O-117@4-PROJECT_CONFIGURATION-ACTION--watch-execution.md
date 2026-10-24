---
atom_id: CA-O-117@4
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 4
updated_at: 2026-10-23 03:14:50 +0400
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  depends_on:
  - Subject/Engineering/Programmatic Action/Execution Notification Adapter
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Implementation
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Subject/Engineering/Journal Event Query
relations:
  relates_to:
  - CA-R-1809
  - CA-D-517
---
# Summary

Wait for execution updates

## Operation

Execution notifications **means** the Programmatic Action implementing the following responsibility:

- compare snapshots of existing saved evidence; replay confirmed Journal updates after the cursor, await changes asynchronously, and distinguish unconfirmed event recording.
- accept the declared inputs **and** return the declared results under CA-D-517-WATCH_EXECUTION--encode-watch-execution-bindings.
- report missing **or** ambiguous evidence as an explicit result.
- execution requires an Operator-authorized invocation; discovery **or** observation grants no mutation authority.

## Details

this Action provides the responsibility named by its Summary. a Workflow **may** invoke the Action through a Step. a direct call **may** use the same Action **without** creating a Workflow Run. observation preserves the original Run **and** evidence.
