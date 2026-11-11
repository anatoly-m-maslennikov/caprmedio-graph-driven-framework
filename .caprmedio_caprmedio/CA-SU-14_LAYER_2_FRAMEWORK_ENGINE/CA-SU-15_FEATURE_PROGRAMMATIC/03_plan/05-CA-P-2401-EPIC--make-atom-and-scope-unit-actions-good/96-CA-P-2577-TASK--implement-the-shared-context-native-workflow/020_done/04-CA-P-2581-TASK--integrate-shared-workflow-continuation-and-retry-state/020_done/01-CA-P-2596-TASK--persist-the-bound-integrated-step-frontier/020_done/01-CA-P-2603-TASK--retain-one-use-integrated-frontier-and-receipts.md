---
atom_id: CA-P-2603
ref_id: CA-P-2603
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
  - CA-P-2579
  - CA-P-2595
  relates_to:
  - CA-R-1527
  - CA-M-405
  - CA-M-422
  - CA-M-430
  - CA-O-016
status: Done
version: 4
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 1-CA-P-2603-TASK--retain-one-use-integrated-frontier-and-receipts.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan/05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/96-CA-P-2577-TASK--implement-the-shared-context-native-workflow/020_done/04-CA-P-2581-TASK--integrate-shared-workflow-continuation-and-retry-state/020_done/01-CA-P-2596-TASK--persist-the-bound-integrated-step-frontier/020_done
work_sequence_number: 1
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Retain one-use Integrated frontier and receipts

## Objective

Persist exact Project/Run/source/packet bindings and immutable consumed receipts under one Run lock.

## Details

At most 15 minutes of own work; split before expanding. One Task per file. Review/update the next dependent Task after actual acceptance. Reuse current PROGRAMMATIC M/E/D, locked uv and canonical source/state owners. Preserve unrelated edits, exact predecessors and business-only Journal semantics. No production MCP traffic, full-suite run, release/deployment, uncertain replay or commit.

Accepted: selected_integrated_frontier.py, selected_integrated_frontier_records.py and selected_integrated_frontier_state.py; 14 root-run focused checks, producer Ruff/format/strict typing and independent targeted PASS. Canonical Project-root admission, strict closed state shapes, payload/response digests, bounded no-follow reads and lock cleanup verified. Exact duplicates return retained receipts; conflicting submissions and copied cross-Project state are refused. No native MCP claim.

### Definition of Done

Retain exact bounded paths and focused functional/type/lint evidence; distinguish storage acceptance from graph/MCP execution and runtime admission.
