---
atom_id: CA-P-2535
ref_id: CA-P-2535
container:
  atom: CA-P-2533
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/Release Version
tier: 3
relations:
  is_decomposition_of:
  - CA-P-2533
status: Done
version: 5
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 2-CA-P-2535-TASK--verify-isolated-publication-scheduling-and-unchanged-suite-coverage.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan/5-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/done/88-CA-P-2533-TASK--isolate-publication-crash-checks-before-parallel-suite-work/done
work_sequence_number: 2
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Verify isolated publication scheduling and unchanged suite coverage

## Objective

Remove the full suite's own interference from its crash-publication check without weakening coverage.

## Details

Exclusive edit PROJECT_TOOLS/tests/test_full_test_suite_parallel.py only. Use actual scheduler/pools with disposable module fixtures and controlled external execution. Prove exact-once isolated critical-module execution with no other worker active; remaining pools still2ordinary+2Docker; all output/count/skip accounting and serial launcher preserved; critical failure still permits later modules and fails summary; cancellation cancels queued work. Preserve30/1800second deadlines. Do not edit source owner, sharedfixture or other files, Atoms/Git/Docker/MCP/release. At most15minutes own work, respect current compact M/E/D and source-size ratchet; run focused source-scheduler tests after owner freeze.

### Acceptance

Frozen scheduler regressions prove exclusive critical execution, FINISH before every later START, exact-once canonical execution,2+2remaining pool bounds, failure continuation/counts, launcher and cancellation behavior. Root17/17 scheduler checks pass0.807s, adjacent14/14 pass2.588s; independent review APPROVE. Test file SHAe4133300bafe6c7ddfd1a98be142b9e4826dd341e693e42f614fcdc418ce9e86,272physical lines; C564 records size debt, no whole-source waiver. No Docker daemon/full release was used by focused checks.
