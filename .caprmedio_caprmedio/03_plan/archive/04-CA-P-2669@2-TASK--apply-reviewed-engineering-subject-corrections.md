---
atom_id: CA-P-2669@2
content_role: Plan
type: Plan
label: Task
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Graph Node/Engineering
version: 2
updated_at: 2026-10-27 04:47:08 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2665
tier: 4
work_sequence_number: 4
---
# Summary

Apply reviewed Engineering Subject corrections

## Objective

Review and apply Candidate #9 Drafts, preserving predecessor history and unrelated work.

## Details

Use the decisions in P2667 and actual Drafts from P2668. Review the exact batch before promotion. Verify source identity/version and stop on a changed source or unsuccessful write.

For each accepted update, archive the Current predecessor with its previous Version and promote the next-version Draft. Classification-only path changes preserve the Atom ID. A changed Summary or Content Role requires a new ID. New definitions start with their own IDs. Preserve unrelated content and historical revisions.

Update the thin table from Drafted to Applied only after the corresponding Current source exists and matches the accepted successor. Keep unresolved changes separate.

## Definition of Done

- Applied Current heads and predecessor archives match the reviewed batch.
- Missing definitions are active only after their accepted Drafts are promoted.
- Unresolved cases and actual partial progress are recorded; no unreviewed content is published.
