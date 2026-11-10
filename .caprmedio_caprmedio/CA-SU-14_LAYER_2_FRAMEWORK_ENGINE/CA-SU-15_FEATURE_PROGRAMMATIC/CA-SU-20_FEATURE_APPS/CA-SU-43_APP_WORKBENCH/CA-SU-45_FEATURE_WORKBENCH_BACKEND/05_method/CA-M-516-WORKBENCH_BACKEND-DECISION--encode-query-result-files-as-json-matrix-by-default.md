---
identity:
  atom_id: CA-M-516
  ref_id: CA-M-516
context:
  container:
    scope_unit: CA-SU-45
  role: Method
  form: Decision
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Data Handling <+ Query Processing
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 4
relations:
  method_for:
  - CA-R-2729
state:
  status: Active
  version: 2
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-M-516-WORKBENCH_BACKEND-DECISION--encode-query-result-files-as-json-matrix-by-default.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/05_method
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---
## Summary

Encode query result files as JSON matrix by default

## Claim scope

Shared Workbench query-result serialization.

## Claim

### Prose Claim

Use JSON matrix as the default result-file format: `columns` stores names once and `rows` stores ordered positional values. CSV and TOON are alternatives and all formats use the shared value encoder.

Write under the selected Project's `.caprmedio_tmp/workbench/query_results`. Return completed file metadata/path, not rows or full SQL, in ordinary MCP responses; export from the existing materialized result without rerunning SQL. Explicit inline delivery keeps browser grid pages available. Preserve order, duplicate names, nulls, empty strings, Unicode, source newlines and Formal Claim text. Use the official TOON codec; CSV normal quoting must distinguish unquoted null from quoted empty. Do not stringify every cell or flatten multiline claims.
