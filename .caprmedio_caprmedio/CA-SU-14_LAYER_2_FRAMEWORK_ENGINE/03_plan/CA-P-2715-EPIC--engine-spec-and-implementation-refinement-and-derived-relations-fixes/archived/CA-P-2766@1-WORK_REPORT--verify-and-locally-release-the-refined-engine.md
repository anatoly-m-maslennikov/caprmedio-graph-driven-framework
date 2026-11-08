---
identity:
  id: CA-P-2766
  ref_id: CA-P-2766@1
context:
  container:
    atom: CA-P-2715
  role: Plan
  form: Work Report
  label: Work Report
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2731
state:
  status: Archived
  version: 1
  updated_at: 2026-11-09 01:44:42 +0400
destination:
  file:
    name: CA-P-2766@1-WORK_REPORT--verify-and-locally-release-the-refined-engine.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/archived
author: Anatoly Maslennikov
---

## Summary

Verify and locally release the refined Engine

## Details

Eight current-code Docker E2E cases passed. Watcher latency is 240.0–340.6 ms; 500-item move is 8.128 seconds; full reread is 38.562 seconds. Existing gates are unchanged. Comment-only trace pins were subsequently reconciled. The local release, installed-image comparison, deployed query_schema/derived-relation checks and real-project canary remain. Native Codex rendering and older Tools remain excluded.
