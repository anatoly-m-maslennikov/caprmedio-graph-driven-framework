---
identity:
  atom_id: CA-M-516
  ref_id: CA-M-516@1
context:
  container:
    scope_unit: CA-SU-45
  role: Method
  form: Decision
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data
      Handling <+ Query Processing
    dependencies:
    - CAPRMEDIO_MODEL <+ Projection
  tier: 4
relations:
  method_for:
  - CA-R-2729
state:
  status: Archived
  version: 1
  updated_at: 2026-11-10 00:46:37 +0400
destination:
  file:
    name: CA-M-516@1-WORKBENCH_BACKEND-DECISION--encode-query-result-files-as-json-matrix-by-default.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/05_method/archive
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

Use JSON matrix as the default result-file format. Store column names once in `columns` and ordered positional values in `rows`. Offer CSV and TOON as alternatives. Apply the same shared value encoding to every format.

Write results under the selected Project's `.caprmedio_tmp/workbench/query_results`. Return metadata and the completed file path instead of embedding rows or full SQL in an ordinary MCP answer. Read from the existing materialized result; do not rerun SQL to export it. Keep browser grid pages available through explicit inline delivery.

Preserve column order, duplicate names, nulls, empty strings, Unicode, source newlines and Formal Claim text. Use the official TOON codec for the matrix value. For CSV use normal quoting, distinguishing unquoted null from quoted empty with matching typed readback. Do not stringify every cell or replace multiline claims with one line.

## Details

The 50-Atom comparison found CSV slightly smaller in tokens. JSON matrix is the Operator's selected default for its explicit value representation. This choice does not claim a token advantage or a model-comprehension result.
