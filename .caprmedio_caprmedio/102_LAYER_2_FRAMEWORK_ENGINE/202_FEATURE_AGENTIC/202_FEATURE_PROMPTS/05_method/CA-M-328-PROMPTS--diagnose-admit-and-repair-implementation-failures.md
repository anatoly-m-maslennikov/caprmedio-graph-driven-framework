---
atom_id: CA-M-328
content_role: Method
type: Implementation Method
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
status: Active
author: Anatoly Maslennikov
version: 6
updated_at: 2026-10-24 01:50:12 +0400
subjects:
  governs: Subject/Engineering/Implementation prompt failure handling
  depends_on:
  - Subject/Engineering/Prompt
  - Evaluation
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run.Retry
  - Evidence
relations:
  relates_to:
  - CA-R-1846
  - CA-O-234
  - CA-O-096
  - CA-O-099
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
