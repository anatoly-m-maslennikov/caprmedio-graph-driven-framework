---
atom_id: CA-R-1809@8
content_role: Requirement
current_scope_unit: WATCH_EXECUTION
status: Archived
author: Anatoly Maslennikov
version: 8
updated_at: 2026-10-26 00:46:35 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Execution Control
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Domain/Occurrent/Execution
  - Subject/Graph Node/Domain/Continuant/History/Journal
relations:
  relates_to:
  - CA-O-117
  - CA-R-1810
type: Rule
tier: 3
---
# Summary

Wait for execution updates

## Scope

the WATCH_EXECUTION capability for Tool/WATCH_EXECUTION.

## Claim

the WATCH_EXECUTION Tool **must** return correlated execution updates after a caller's cursor, including completion, failure, interruption, handoff, progress, and evidence-recording changes.

## Details

- implement the methodology Action CA-O-117-PROJECT_CONFIGURATION-ACTION--wait-for-execution-updates.
- accept a supported Run ID, opaque cursor and bounded wait timeout; return a new cursor, updates, current status, timeout state, and full report reference.
- preserve the Operator's choice of what **to** execute; discovery, context retrieval, **and** observation provide capabilities.
- bounded **or** unavailable evidence **must** remain explicit **rather than** establish a successful assessment.
