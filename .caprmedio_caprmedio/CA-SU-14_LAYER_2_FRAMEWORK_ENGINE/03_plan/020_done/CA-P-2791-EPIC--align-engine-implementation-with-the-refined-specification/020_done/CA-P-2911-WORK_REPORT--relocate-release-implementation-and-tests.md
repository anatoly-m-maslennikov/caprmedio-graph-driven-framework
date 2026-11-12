---
identity:
  id: CA-P-2911
  ref_id: CA-P-2911
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
  updated_at: 2026-11-11 00:44:42 +0400
destination:
  file:
    name: CA-P-2911-WORK_REPORT--relocate-release-implementation-and-tests.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/020_done
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2839
author: Anatoly Maslennikov
---

## Summary

Relocate release implementation and tests

## Details

Promoted six independently reviewed exact-path corrections and moved 25 release-specific implementation/test files to LAYER_5_FRAMEWORK_DELIVERY. Package-local public tests remain under PUBLIC_RELEASE/tests. Shared Engine helpers stay in place; updated suite discovery, fixture import and README commands. Independent review caught and corrected one focused-test example path.

Passed 88 local and 12 public release tests and both CLI help checks; integration passed 13 suite-discovery, four parallel-runner and eight relation-registry release tests. Ruff passed changed shared runner/test files. No actual local/public release, deployment, commit or push was performed.
