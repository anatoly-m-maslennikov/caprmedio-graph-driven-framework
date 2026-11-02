---
atom_id: CA-O-113@7
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
version: 7
updated_at: 2026-10-24 01:18:03 +0400
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  depends_on:
  - Subject/Engineering/Programmatic Action/Workflow and Action Discovery Adapter
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Subject/Domain/Node/Continuant/History/Journal
relations:
  relates_to:
  - CA-R-1805
  - CA-D-513
tier: 3
---
# Summary

Find Workflows and Actions by outcome

## Operation

Workflow and Action discovery **means** the Programmatic Action implementing the following responsibility:

- search carried Operations Type, Summary, Operation, Scope Unit, and declared implementation bindings; report unknown execution kind explicitly.
- accept the declared inputs **and** return the declared results under CA-D-513-DISCOVER_OPERATIONS--encode-discover-operations-bindings.
- report missing **or** ambiguous evidence as an explicit result.
- execution requires an Operator-authorized invocation; discovery **or** observation grants no mutation authority.

## Details

this Action provides the responsibility named by its Summary. a Workflow **may** invoke the Action through a Step. a direct call **may** use the same Action **without** creating a Workflow Run. observation preserves the original Run **and** evidence.
