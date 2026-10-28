---
atom_id: CA-M-328@13
content_role: Method
type: Implementation Method
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
status: Archived
author: Anatoly Maslennikov
version: 13
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Execution Control
  depends_on:
  - Subject/Graph Node/Engineering/Execution Control/Failure Handling
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Evaluation'
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run.Retry
  - Subject/Graph Node/Domain/Continuant/History
relations: {}
tier: 3
---
# Summary

Diagnose, admit, and repair implementation failures

## Scope

the diagnosed repair path after a selected Implementation Workflow check does not pass.

## Claim

**to** handle a failure, retain the actual failing evidence, diagnose its category, admit retry only through current permission/confidence/retry guards, repair the admitted defect, and return for renewed preparation or checking.

## Details

Changed failures, stale evidence, unavailable authority, or non-progressing work block. Repair preserves issue evidence and does not create or promote an M atom.
