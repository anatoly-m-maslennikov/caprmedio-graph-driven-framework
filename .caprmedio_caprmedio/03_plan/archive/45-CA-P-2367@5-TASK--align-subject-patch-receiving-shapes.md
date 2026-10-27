---
atom_id: CA-P-2367@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 45
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject/Engineering/Tool
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 5
updated_at: 2026-10-24 08:10:13 +0400
relations:
  is_decomposition_of:
  - CA-P-2167
tier: 3
---
# Summary

Align Subject patch receiving shapes

## Objective

Align only CA-D-531's Subject-only patch shapes with the already accepted CA-D-425/CA-D-623 contract. Reject public indexes, retain by-value replacement and explicit add/remove/complete-set definitions, and preserve all existing target, intent, assessment, authorization and effect fields.

## Details

Estimated own work: up to 15 minutes; split before exceeding this bound. Root owns integration, Plans and Git. Workers use disjoint assigned files and preserve unrelated edits. This is necessary Subjects-only migration tooling; Core migration, ordinary content edits, legacy C/A repair, catalogs and unrelated connector work remain outside this Task.

### Definition of Done

The exact previous D531 bytes are preserved; Version advances once. An independent review confirms only this mismatch changed and no implementation or runtime readiness is asserted.

### Accepted bounded outcome

CA-D-531 v5 aligns only the closed Subject patch shapes and rejects caller indexes. It keeps target, envelope, intent, assessment, authorization and effect rules unchanged. Source SHA-256: `0e8b2d84a37765e622406a43dca937647fdcd0d5530bc1b1f4b656e2180348d8`. Its exact archived v4 SHA-256 `8f2501d4d013e6a0b844c30fe0a80e717161a45eb0da8ed535e267bc56118f16` matches the former current file in Git HEAD byte-for-byte.

Independent source review passed against R1934/D623/D425 and D269: depends_on is an unordered unique collection, explicit complete-set replacement is admitted, equal membership is a byte-preserving no-op and scalar governs stays scalar. The diff contains only this clause and required Version/time. This releases bounded local planner implementation, not installed MCP, publication or Core migration. Those remain open under CA-P-2167.

