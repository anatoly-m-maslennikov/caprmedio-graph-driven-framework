---
atom_id: CA-R-1872@4
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 4
updated_at: 2026-10-24 11:58:20 +0400
subjects:
  governs: Subject/Engineering/Journal Event Query/Source Route
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
relations:
  relates_to:
  - CA-O-161
  - CA-O-162
  - CA-O-163
  - CA-D-557
type: Rule
tier: 3
---
# Summary

Retain one minimal Journal query route definition

## Scope

The source-to-implementation route.

## Claim

FIND_AND_FETCH_JOURNAL_EVENTS **must** retain exactly one Workflow, one query Action, and one query Step as its source route.

## Details

Shared Run support remains shared infrastructure and does not become an additional Workflow or query Action.
