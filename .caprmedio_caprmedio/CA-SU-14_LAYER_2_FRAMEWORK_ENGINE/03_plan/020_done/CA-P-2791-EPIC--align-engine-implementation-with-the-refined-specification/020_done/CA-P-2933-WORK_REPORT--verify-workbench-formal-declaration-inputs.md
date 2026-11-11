---
identity:
  id: CA-P-2933
  ref_id: CA-P-2933
context:
  container:
    atom: CA-P-2791
  role: Plan
  form: Work Report
  label: Work Report
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Atom
  tier: 4
state:
  status: Done
  version: 1
  updated_at: 2026-11-11 05:37:29 +0400
destination:
  file:
    name: CA-P-2933-WORK_REPORT--verify-workbench-formal-declaration-inputs.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2866
  - CA-P-2813
author: Anatoly Maslennikov
---

## Summary

Verify Workbench formal declaration inputs

## Details

The compiler reads CFEL from Formal Claim. It ignores comments. Bracketed formats and conditions, wildcard constraints and observed headings do not create property names. The 18-test Content schema check passed, including the finite-list and observed-heading regression.

The isolated candidate image exposed 77 columns, including six declared Content columns, and returned three Core Formal Claims. Check returned ordered column metadata without SQL or rows. The Docker suite still had stale delivery and audit-table assertions. The serving image remains unchanged: live query_run returned 4,002 Atoms and zero Core model rows. Generic inheritance and deployed acceptance remain open under P2866.

Evidence: `.caprmedio_tmp/CA-P-2791/CA-P-2866/formal-input-20261111/image-build-final/candidate-result.json` and `docker-e2e.log` in the same folder.
