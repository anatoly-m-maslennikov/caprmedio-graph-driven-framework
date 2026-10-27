---
atom_id: CA-P-2368@2
content_role: Plan
type: Plan
label: Task
work_sequence_number: 46
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Tool
  depends_on:
  - Atom
  - Subject
  - Plan
version: 2
updated_at: 2026-10-14 06:03:26 +0400
relations:
  is_decomposition_of:
  - CA-P-2167
---
# Summary

Implement explicit Subject dependency set replacement

## Objective

Implement the existing depends_on replace_set shape in the shared pure Subject planner and affected Describe/test surfaces. Compare the exact current collection, accept only explicit unique valid new Subjects, preserve unrelated bytes and comments or refuse unsupported forms, and keep governs scalar and generic duplicate refusal. Reuse the existing rendering and intent/materialization/staging paths; no implicit merging or live application.

## Details

Estimated own work: up to 15 minutes; split before exceeding this bound. Root owns integration, Plans and Git. Workers use disjoint assigned files and preserve unrelated edits. This is necessary Subjects-only migration tooling; Core migration, ordinary content edits, legacy C/A repair, catalogs and unrelated connector work remain outside this Task.

### Definition of Done

Focused tests prove complete-set replacement, no-op, stale/duplicate/invalid-input refusal, LF/CRLF and unrelated-byte preservation, and consistent preview/intent/staging results. Independent code/tests verify the actual implementation. Existing selected apply integration is a separate gate, not waived.

### Accepted bounded outcome

Implemented explicit depends_on replace_set using the existing comment-preserving collection renderer. Exact source membership and identity/version/hash preconditions remain required; equal membership preserves all source bytes and metadata. Scalar governs, duplicate refusal, overlap refusal and sealed authorization remain unchanged; operation is retained in the deterministic intent.

Verification: 7 dedicated author tests, 49 existing preview/intent/by-value/staging regressions and 8 separately authored independent tests passed (64 checks). Independent connected-code review found no actionable issue. Code SHA-256: atom_subject_patch.py `fcb9b53d1c7062df917401ec0dc38992bbf85292f5bfd1932ce3d818256fff6a`; atom_operations.py `ab7b3eec7da62ef0ad4e470764653e19fc948fd21c5bc17da5a8cbfd947481dc`. Author test SHA-256 `c9f2fbbd945970531623097a785e0ee5b5c355ce872f41f99ac26739fce8c312`; independent test SHA-256 `b63d7101a12ac0cb34374388ec908c2851c960bbef6955ec005d3b4fef14883f`.

Only formatting within a changed collection may normalize; comments, line endings and unrelated bytes are preserved. Installed MCP, actual selected-route integration and live Core migration remain separately gated under P2371 and the parent Epic. No broader Property-edit support or migration completion is claimed.

