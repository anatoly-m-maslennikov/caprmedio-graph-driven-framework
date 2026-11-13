---
identity:
  atom_id: CA-A-1346
  ref_id: CA-A-1346
context:
  role: analysis_and_advisory
  form: code_synopsis
  tier: 4
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
      <+ Architecture <+ Communication <+ Interface Contracts
  container:
    scope_unit: FRAMEWORK_ENGINE
state:
  version: 1
  status: active
  updated_at: '2026-11-12T12:48:53.126318+00:00'
destination:
  file:
    name: CA-A-1346-FRAMEWORK_ENGINE-CODE_SYNOPSIS--query-error-diagnostics-echo-submitted-sql.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis_and_advisory
---
## Summary

Query error diagnostics echo submitted SQL

## Claim

### Prose Claim

In the CAPRMEDIO working tree based on `c0b983cb27`, `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/query_store.py` forwards DuckDB exception text and `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/workbench_tools.py` returns it as a diagnostic. A live read-only request with `SELECT missing_review_field FROM atoms` returned `LINE 1: EXPLAIN SELECT missing_review_field FROM atoms` in its diagnostic. CA-D-673@18 and CA-M-462@14 require ordinary responses to omit the full submitted SQL. The binder error can expose that text.
