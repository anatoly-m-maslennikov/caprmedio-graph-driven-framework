---
atom_id: CA-P-2604
ref_id: CA-P-2604
container:
  atom: CA-P-2596
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/Workflow Orchestration/Run Execution Dispatch
tier: 3
relations:
  is_decomposition_of:
  - CA-P-2596
  depends_on:
  - CA-P-2603
  relates_to:
  - CA-R-1527
  - CA-M-405
  - CA-M-422
  - CA-M-430
  - CA-O-016
status: Done
version: 5
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 2-CA-P-2604-TASK--checkpoint-canonical-run-session-mutations.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan/5-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/96-CA-P-2577-TASK--implement-the-shared-context-native-workflow/done/4-CA-P-2581-TASK--integrate-shared-workflow-continuation-and-retry-state/done/1-CA-P-2596-TASK--persist-the-bound-integrated-step-frontier/done
work_sequence_number: 2
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Checkpoint canonical Run-session mutations

## Objective

Retain canonical actual Run identities, effects, terminal receipts and recording diagnostics after each session mutation without a Journal completeness requirement.

## Details

At most 15 minutes of own work; split before expanding. One Task per file. Review/update the next dependent Task after actual acceptance. Reuse current PROGRAMMATIC M/E/D, locked uv and canonical source/state owners. Preserve unrelated edits, exact predecessors and business-only Journal semantics. No production MCP traffic, full-suite run, release/deployment, uncertain replay or commit.

Own new selected_integrated_session checkpoint/save modules and focused disposable tests only. Constructor is effect-free; explicit save and lifecycle-compatible hooks persist strict frozen-request/Project/Run-bound state atomically. Keep restore/no-replay acceptance in the next leaf.

### Definition of Done

Retain exact bounded paths and focused functional/type/lint evidence; distinguish storage acceptance from graph/MCP execution and runtime admission.

### Accepted checkpoint/save boundary — 22 October 2026

Independent targeted readback PASS closes all four checkpoint holds. The wrapper preserves canonical actual Run identities/lifecycle mutations and write-once terminal evidence hashes, uses the shared bounded reader and canonical Project-root resolver, and does not require complete Journal delivery. Producer five focused checks, Ruff/format and strict typing pass; root checkpoint verification is running separately. Restore/no-replay is admitted for its distinct next bounded leaf after this acceptance; no graph/MCP execution or deployment is claimed.
