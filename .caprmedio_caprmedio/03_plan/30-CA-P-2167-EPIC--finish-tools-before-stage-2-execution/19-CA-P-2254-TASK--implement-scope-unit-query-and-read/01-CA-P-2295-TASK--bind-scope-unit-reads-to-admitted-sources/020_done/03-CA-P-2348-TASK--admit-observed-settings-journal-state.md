---
atom_id: CA-P-2348
ref_id: CA-P-2348
container:
  atom: CA-P-2295
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/Continuant/Tool
  dependencies:
  - Subject/Graph Node/Domain/Continuant/Atom
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
  - Subject/Graph Node/Domain/Continuant/Project.Settings
  - Subject/Graph Node/Domain/Continuant/History/Journal
tier: 3
relations:
  is_decomposition_of:
  - CA-P-2295
status: Done
version: 7
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 3-CA-P-2348-TASK--admit-observed-settings-journal-state.md
    path: .caprmedio_caprmedio/03_plan/30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/19-CA-P-2254-TASK--implement-scope-unit-query-and-read/1-CA-P-2295-TASK--bind-scope-unit-reads-to-admitted-sources/done
work_sequence_number: 3
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
---
# Summary

Admit observed Settings Journal state

## Objective

Allow truthful initial observation of existing Settings through the already registered recovered-state Journal form.

## Details

Update only D360, D365, E458 and E459, preserving exact predecessors and increasing each Version by one. Preserve Summary, Subjects, identity, relations and existing schema/ownership policy. Reuse recovered/governed_project_state and exact Project/path/Revision/digest evidence; no new Journal format, false past edit, Settings-byte change or lineage reset. Operator authorized this registration after clarification that it is in the Journal. Actual registration stays separate from rules and requires an available admitted route.

Estimated own work: up to 15 minutes. Split before exceeding this bound. Root owns Plans and Git. Parallel workers own disjoint files. No live Core migration.

### Definition of Done

Exact source and implementation evidence, focused positive/refusal checks and independent review establish this bounded outcome. Preparation is not completion; runtime and whole-Project admission remain separate.


### Accepted outcome — 2026-10-13

Independent four-source acceptance is recorded in observed-settings-source-acceptance.md under the Stage-2 Tools-first derived receipts. D360 v13, D365 v12 and E458/E459 v17 preserve exact predecessors. Existing Journal schema positive plus seven refusals passed. Settings bytes remain unchanged. Live registration is not completed by this Task.

