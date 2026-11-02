---
atom_id: CA-R-1861@11
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 11
updated_at: 2026-10-26 00:46:35 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Data Handling/Source Retrieval
  depends_on:
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - Subject/Graph Node/Domain/Occurrent/Event
  - Subject/Graph Node/Engineering/Continuant/Tool//FIND_AND_FETCH_JOURNAL_EVENTS
relations:
  relates_to:
  - CA-O-162
  - CA-D-555
tier: 3
type: Rule
---
# Summary

Read only the canonical Events Journal

## Scope

The FIND_AND_FETCH_JOURNAL_EVENTS Tool source boundary.

## Claim

FIND_AND_FETCH_JOURNAL_EVENTS **must** query only canonical Event carriers under the selected Project's `.caprmedio_<project name>/_journal/` root.

## Details

Historical sealed Event references resolve only as immutable references. The source
is raw canonical JSON Event bytes: raw duplicate object keys are rejected before
parse, and no alternate log, derived projection, filename identity, or source
rewrite may substitute for canonical Events.
