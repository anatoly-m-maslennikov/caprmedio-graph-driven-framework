---
identity:
  id: CA-P-2818
  ref_id: CA-P-2818
context:
  container:
    atom: CA-P-2791
  role: Plan
  form: Plan
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
  label: Task
state:
  status: Active
  version: 11
  updated_at: 2026-11-11 08:25:34 +0400
destination:
  file:
    name: CA-P-2818-TASK--review-and-deliver-the-accepted-engine-changes.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification
author: Anatoly Maslennikov
relations:
  IS_BLOCKED_BY:
  - CA-P-2816
  - CA-P-2817
  - CA-P-2842
  - CA-P-2843
  - CA-P-2844
  - CA-P-2852
  - CA-P-2839
  - CA-P-2859
  - CA-P-2861
  - CA-P-2866
  - CA-P-2910
---

## Summary

Review and deliver the accepted Engine changes

## Objective

Review the combined implementation against adopted RMED, fix confirmed issues, then perform the authorized local delivery with its actual checks. Record Current spec versions, tests, deployment and remaining deferrals separately.

## Subtasks

- [x] Review and fix the next scoped input batch. (ETA: up to 15 min.)
- [ ] Complete one scoped implementation or verification batch; split before exceeding 20 min.
- [ ] Review and fix the result; record a small P / Work Report. (ETA: up to 15 min.)

## Definition of Done

The stated work has actual source/code/test evidence. Every unresolved or unrun case is explicit; no Task text replaces RMED.

## Image-build acceptance

- [ ] Verify model/schema and canonical relation generation from selected Current Declaration formal Claims on every image build, including builds used by local and public release. Check generated inputs/provenance and live query results after build. M500 is the existing schema authority; C729 records the missing declaration-input inventory.

## Release-test cleanup check

Verify the working MCP/Workbench image and query_run. Exclude Workflow-engine execution, routing, Run-state/history, recovery and C727 prompt-frontier repair from this gate; retain the direct release-runner cleanup checks below.

- [x] Recheck C567 against the retained release test runner and current Docker fixtures. The historical failing selected-Workflow fixture is no longer present.
- [ ] Reproduce any applicable interrupted-run or failed-start cleanup defect, then prepare the smallest confirmed repair and regression coverage. Split investigation, repair and verification into batches of at most 15–20 minutes.
- [ ] Record exact resource ownership and outcomes under the existing cleanup policies. Do not restore retired Workflow tests or treat historical evidence as proof of a current failure.


## Cleanup review result

P2929 records the retained runner/fixture review, four real-process tests and seventeen controlled cleanup tests. C567 exists only in Archive and was not modified. No retained-path container/network leak was reproduced; general forced-Docker-termination cleanup is not proven by the process and controlled-fixture tests. Keep actual final delivery checks separate.

## Local Release run

Run ID `engine-refinement-20261111-v2`. Use the 59 exact test modules in `.caprmedio_tmp/CA-P-2791/CA-P-2818/focused-final-modules.json` (SHA-256 `d80615e634e449492dff193f1f4826949d7f0cbc6e70d1720c013d397a189d14`). This is the Operator's Workbench and query_run verification scope. The release receipt must report focused validation.

The checkout starts from `ef8e959d1ee030955dabb880381eca2ea803eb64` with the current working changes. P2957 records the asset comparison against the tested image. P2959 records the added service evaluation, and P2960 records the Docker and soak gates. The release runs the selected modules again after its local checkpoint. Check the installed Workbench and query_run before closing C729.

## Local Release retry

The v2 run stopped at source validation after checkpoint `126d529a16`. P2961 records the reader, copy and compiler fixes. The corrected preflight selected 1,061 Methodology Atoms with no conflicts and declaration digest `194e1969e32f5dbd6d45d985e2e2627521710e6f5944d7b98d7be96c688a4ae8`.

Run ID `engine-refinement-20261111-v3`. Repeat focused validation using the 61 exact modules in `.caprmedio_tmp/CA-P-2791/CA-P-2818/focused-retry-modules.json` (SHA-256 `4efeedc517fdb860dfd1121a72e5a56057414b73aee0a17652d8e844dfe1c8b5`). The two added modules cover the corrected Scope Unit reader and retained compiler. Verify the installed Workbench and query_run before closing C729.
