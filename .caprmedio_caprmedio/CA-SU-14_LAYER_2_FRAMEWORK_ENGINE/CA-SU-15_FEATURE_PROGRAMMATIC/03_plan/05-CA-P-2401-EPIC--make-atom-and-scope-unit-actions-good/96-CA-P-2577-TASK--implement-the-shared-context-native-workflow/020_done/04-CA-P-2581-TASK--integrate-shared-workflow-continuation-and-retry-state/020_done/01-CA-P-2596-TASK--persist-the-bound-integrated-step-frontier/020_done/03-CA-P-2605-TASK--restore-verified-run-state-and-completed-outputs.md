---
atom_id: CA-P-2605
ref_id: CA-P-2605
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
  - CA-P-2604
  relates_to:
  - CA-R-1527
  - CA-M-405
  - CA-M-422
  - CA-M-430
  - CA-O-016
status: Done
version: 6
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 3-CA-P-2605-TASK--restore-verified-run-state-and-completed-outputs.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan/05-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/96-CA-P-2577-TASK--implement-the-shared-context-native-workflow/020_done/04-CA-P-2581-TASK--integrate-shared-workflow-continuation-and-retry-state/020_done/01-CA-P-2596-TASK--persist-the-bound-integrated-step-frontier/020_done
work_sequence_number: 3
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Restore verified Run state and completed outputs

## Objective

Restore the exact checkpoint and verify retained result bytes before reusing a completed Action output; never call the provider again.

## Details

At most 15 minutes of own work; split before expanding. One Task per file. Review/update the next dependent Task after actual acceptance. Reuse current PROGRAMMATIC M/E/D, locked uv and canonical source/state owners. Preserve unrelated edits, exact predecessors and business-only Journal semantics. No production MCP traffic, full-suite run, release/deployment, uncertain replay or commit.

Review accepted checkpoint API before activation. Verify altered frozen request, Project, source/progress bytes, symlink/invalid JSON and interrupted state are refused. Preserve canonical terminal/recovery checks and missing-Journal tolerance. This leaf does not authorize graph/transport deployment.

### Definition of Done

Retain exact bounded paths and focused functional/type/lint evidence; distinguish storage acceptance from graph/MCP execution and runtime admission.

### Reviewed checkpoint predecessor — 22 October 2026

Active after CA-P-2604 checkpoint acceptance. Reuse its unchanged create/restore API, validation-only canonical RunExecutionSession probe and write-once evidence hashes. Root must verify actual restart/terminal/effect retention, altered frozen/progress/nested-state refusal, no-Journal operation and completed native output decoded from the same hashed byte buffer before accepting this leaf. No provider replay or graph/transport admission follows from checkpoint-only success.

### Accepted restore/no-replay boundary — 22 October 2026

Done after independent targeted PASS and root execution of all five focused checkpoint functional checks. Canonical actual/terminal/effect state survives restart without complete Journal delivery. Nested Run identities and lineage are checked with a no-effect canonical lifecycle probe before restoration; altered frozen binding, progress bytes or evidence-key sets are refused. Retained native output is hashed and decoded from the same bounded non-following byte buffer. No provider, production MCP, full suite, release or deployment was executed.
