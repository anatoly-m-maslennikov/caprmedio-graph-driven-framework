---
atom_id: CA-R-1861@5
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 5
updated_at: 2026-10-24 00:51:05 +0400
subjects:
  governs: FIND_AND_FETCH_JOURNAL_EVENTS/source
  depends_on:
  - Subject/Domain/Node/Continuant/History/Journal
  - Event
  - Subject/Engineering/Tool//FIND_AND_FETCH_JOURNAL_EVENTS
relations:
  relates_to:
  - CA-O-162
  - CA-D-555
tier: 3
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
