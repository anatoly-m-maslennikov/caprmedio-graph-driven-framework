---
atom_id: CA-M-502
ref_id: CA-M-502
container:
  scope_unit: CA-SU-45
role: Method
form: Eng Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 4
relations:
  method_for:
  - CA-R-2903
status: Active
version: 1
updated_at: 2026-11-07 01:21:17 +0400
carrier_destination:
  file:
    name: CA-M-502-WORKBENCH_BACKEND-ENG_DECISION--write-query-history-in-the-background.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/05_method
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---

## Summary

Write query history in the background

## Claim

### Prose Claim

Use one ordered background writer in each Workbench owner for automatic query history. Submit one record after each Run and any requested synchronous Save handling, using the submission timestamp. Do not wait for its file write before returning the Run result. Serialize query-log reads and writes so readers never see a partial line. Report background failures to stderr, without retry or a response warning. Drain submitted writes on orderly owner shutdown; a process crash may lose unflushed history.

Explicit query and View saves still finish writing before returning their IDs. Keep the query log separate from watcher event delivery, watcher history, result retention and saved Journal records.
