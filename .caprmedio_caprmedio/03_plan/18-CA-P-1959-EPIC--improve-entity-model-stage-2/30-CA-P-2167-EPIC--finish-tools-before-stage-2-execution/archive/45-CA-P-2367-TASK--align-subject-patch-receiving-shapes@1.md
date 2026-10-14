---
atom_id: CA-P-2367
content_role: Plan
type: Plan
label: Task
work_sequence_number: 45
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Plan]
version: 1
updated_at: "2026-10-14 05:52:57 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
---
# Summary

Align Subject patch receiving shapes

## Objective

Align only CA-D-531's Subject-only patch shapes with the already accepted CA-D-425/CA-D-623 contract. Reject public indexes, retain by-value replacement and explicit add/remove/complete-set definitions, and preserve all existing target, intent, assessment, authorization and effect fields.

## Details

Estimated own work: up to 15 minutes; split before exceeding this bound. Root owns integration, Plans and Git. Workers use disjoint assigned files and preserve unrelated edits. This is necessary Subjects-only migration tooling; Core migration, ordinary content edits, legacy C/A repair, catalogs and unrelated connector work remain outside this Task.

### Definition of Done

The exact previous D531 bytes are preserved; Version advances once. An independent review confirms only this mismatch changed and no implementation or runtime readiness is asserted.
