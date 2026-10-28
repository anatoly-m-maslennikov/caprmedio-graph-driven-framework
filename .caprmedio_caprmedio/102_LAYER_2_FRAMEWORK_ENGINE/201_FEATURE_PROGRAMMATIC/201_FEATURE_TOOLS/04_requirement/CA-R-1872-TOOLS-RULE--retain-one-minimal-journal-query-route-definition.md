---
atom_id: CA-R-1872
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-27 20:00:05 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
relations: {}
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
