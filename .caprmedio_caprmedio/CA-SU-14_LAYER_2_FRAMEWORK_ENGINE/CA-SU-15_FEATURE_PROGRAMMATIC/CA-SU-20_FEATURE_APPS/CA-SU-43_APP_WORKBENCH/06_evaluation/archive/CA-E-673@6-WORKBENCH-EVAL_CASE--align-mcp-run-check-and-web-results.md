---
identity:
  atom_id: CA-E-673
  ref_id: CA-E-673@6
context:
  container:
    scope_unit: CA-SU-43
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Development <+
      Architecture <+ Communication <+ Interface Contracts
    dependencies:
    - CAPRMEDIO_MODEL <+ Projection
  tier: 5
relations:
  evaluation_for:
  - CA-R-2729
  - CA-R-2727
  - CA-D-673
state:
  status: Archived
  version: 6
  updated_at: 2026-11-10 00:46:37 +0400
destination:
  file:
    name: CA-E-673@6-WORKBENCH-EVAL_CASE--align-mcp-run-check-and-web-results.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation/archive
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Align MCP Run, Check, and simple web query results

## Claim scope

MCP and web results from the shared synchronous connector.

## Claim

### Prose Claim

MCP and web Run, Page and Check must preserve the same requested data, ordered column metadata and exact counts. Compare decoded result files with explicit inline pages; ordinary execution and fetch responses do not echo full SQL. A Run evaluates SQL once; its pages stay stable across source refresh. The frontend fetches one page at a time and uses shared components for controls and results.

## Details

| Fixture | Expected outcome |
| --- | --- |
| Result larger than the default page | Default Run returns a complete result-file descriptor and counts without rows or SQL; explicit inline Run returns a bounded page. Page reads the requested slice without rerunning SQL or losing rows. |
| Duplicate column aliases and Unicode values | Ordered metadata and positional values remain exact through MCP and web. |
| Query followed by source refresh | The existing query ID keeps its original result; a new Run sees refreshed data. |
| Check over a large result | Validation metadata and available exact counts are returned, without rows, SQL echo, export, save or query-log entry. |
| Invalid SQL, size, offset or query ID | Useful query error; no empty success or retry. |
| Production frontend build | Static Svelte assets load from the Python listener; editor, errors, counts and page controls work. |
| Source error | stderr identifies it; unrelated valid SQL data remains queryable. |
