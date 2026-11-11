---
identity:
  atom_id: CA-M-550
  ref_id: CA-M-550@1-draft
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
  - CA-R-2728@9-draft
  - CA-R-2953
  IS_REPLACEMENT_FOR:
  - CA-M-462
state:
  status: Draft
  version: 1
  updated_at: 2026-11-11 01:59:26 +0400
destination:
  file:
    name: CA-M-550@1-draft-WORKBENCH_BACKEND-DECISION--route-public-sql-through-query-and-source-adapters.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/05_method/000_draft
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---
## Summary

Route public SQL through query and source adapters.

## Claim scope

Trusted public SQL and internal result materialization for one Project.

## Claim

### Prose Claim

Admit supported SQL through MCP or Workbench under CA-R-2728@9-draft, using native parsing/query APIs including DuckPGQ SQL/PGQ. Process the whole script or explicit statement selection in order. Preserve native SQL syntax and distinguish delimiters in quoted strings and comments.

Execute each accepted SELECT once into a DuckDB-owned generated result table. Route supported UPDATE through the shared source adapter under CA-R-2728@9-draft; never mutate source-derived Projection rows directly. Reject unsupported DDL and other DML. Retain ordered native column metadata, including duplicates, and deliver bounded pages from that stable result. Preview uses native `relation.limit(N)` without rewriting submitted SQL, preserves an existing SQL LIMIT, supports CTE/GRAPH_TABLE, and changes counts to the capped execution; absent preview adds no cap.

Keep exact submitted SQL (comments, Unicode and LIMIT) internal. Ordinary Run, Check and Page responses never echo it. Save appends the Bookmark only after materialization; a save failure returns the completed result ID/metadata with `outcome: partial` and `save_error`, without retry or rollback. Failed queries create no saved entry; unsaved Run, Check and Page have no Journal effect. Page transforms use only the existing result table and never rerun, parse, append to or rewrite SQL. At materialization, use one native cache with a private quoted ordinal before public columns; apply preview before snapshot numbering. Resolve public indices to physical positions, never user names or DuckDB `rowid`. Use the ordinal as the final stable page tie-breaker, never as public metadata or a filter/group value. Bind literal filter values with native DuckDB, use `NULLS LAST`, put group order before sort, and calculate window counts before offset/limit. Do not add a second cache, ALTER, UPDATE, rescan, raw SQL grid clause, endpoint or service.

The dedicated result lifecycle owns retention, View pinning, restart disposal and runtime-setting reads. Startup loads bundled DuckPGQ before disabling external access, autoinstall/autoload and public configuration changes; database/spill writes stay in the owned runtime directory and source writes use only the shared adapter. Reject/unknown/storage/delivery errors return useful caller reasons and stderr diagnostics. Invalid requests are recoverable `query_error` WARNING failures; unavailable/unexpected owner failures are ERROR/blocked with the existing restart or generic boundary. DuckPGQ management calls may invalidate the connection; this trusted-input MVP promises no capability sandbox, retry, restoration or connection recovery.
