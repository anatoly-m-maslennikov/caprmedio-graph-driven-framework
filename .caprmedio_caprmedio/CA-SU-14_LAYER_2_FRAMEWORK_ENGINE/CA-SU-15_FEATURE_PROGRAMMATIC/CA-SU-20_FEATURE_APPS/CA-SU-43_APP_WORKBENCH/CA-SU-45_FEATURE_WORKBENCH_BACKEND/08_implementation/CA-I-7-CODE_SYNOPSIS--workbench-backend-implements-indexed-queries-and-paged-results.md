---
identity:
  id: CA-I-7
  ref_id: CA-I-7
context:
  container:
    scope_unit: CA-SU-45
  role: Implementation
  form: Code Synopsis
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Projection
  tier: 3
state:
  status: Active
  version: 1
  updated_at: 2026-11-09 07:55:38 +0400
destination:
  file:
    name: CA-I-7-CODE_SYNOPSIS--workbench-backend-implements-indexed-queries-and-paged-results.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/08_implementation
author: Anatoly Maslennikov
---

## Summary

Workbench Backend implements indexed queries and paged results

## Claim

### Prose Claim

The inspected Backend code reads source files into schema-driven DuckDB tables, applies incremental source and relation changes, and materializes query results for paged reads. Its module and evaluator comments pin older specification Versions.

## Details

Working-tree inspection on 9 November 2026; this describes code, not a new runtime or test result.

### Public query admission and result lifecycle

[query_store.py](../../../../../../../LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/query_store.py)

Native admission requires exactly one DuckDB SELECT, plans it in a read-only transaction, materializes a private result table, serves pages/grids, preserves a View pin, and prunes only unpinned results after the configured TTL.

### Whole-query cursor semantics

[statements.py](../../../../../../../LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/statements.py)

The optional cursor is UTF-16 boundary validation only; select_statement returns the complete SQL unchanged. WorkbenchService passes that complete SQL to QueryStore.

### Source capture, declared/observed schema, and incremental rebuild

[source_reader.py](../../../../../../../LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/source_reader.py)

The reader selects schema mode 1 or 2, maintains successful-row/signature caches and failed signatures, uses incremental changes when declarations permit, falls back to a full capture for schema changes, and derives source rows without source writes.

### Schema compilation and runtime selection

[workbench_schema_asset.py](../../../../../../../LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/workbench_schema_asset.py)

A deterministic image asset contains both mode-1 declared and mode-2 inferred Header schemas with the declared Content schema. A matching delivered asset is used only after exact source-input validation; otherwise the runtime compilation is used.

### Watcher boundary, directory fallback, and durable change log

[source_watcher.py](../../../../../../../LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/source_watcher.py)

The watcher reports repository-relative create/update/remove/rename/move observations under the configured control root. It uses actual filesystem directory inspection for bind-mount events reported as files and adds/removes direct child watches.

### Watcher observation retention and projection mirror

[watcher_change_log.py](../../../../../../../LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/watcher_change_log.py)

Observations append as NDJSON in normal operation. Only expiry or the fixed 100,000-row retention ceiling replaces the file; the database mirror receives the file owner's retained delta under the store lock.

### Synchronization state and refresh observability

[service.py](../../../../../../../LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/service.py)

The service serializes refresh, records owner-local syncing and last-success values without starting the service, emits capture/materialize/write timing fields, and stops the indexing boundary on an unrecoverable exception.

### Asynchronous query log

[query_log.py](../../../../../../../LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/query_log.py)

A single-worker executor accepts asynchronous Run-attempt append requests, writes UTC-hour NDJSON batches, keeps records strictly newer than 48 hours, reports background failures only to stderr, and drains explicitly on close.

### Canonical relation registry and build integration

[relation_registry.py](../../../../../../../LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_WORKBENCH_BACKEND/relation_registry.py)

Only Current Requirement declaration forms contribute relation metadata. Literal inverse bindings and aliases are compiled, ambiguous names are diagnosed and omitted, and incremental relation state keeps canonical/direct and derived facts separate.

### Isolated profiling

[profile_workbench.py](../../../../../../../LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/tests/profile_workbench.py)

The opt-in profiler records one initial index plus three full rebuilds, captures process/Python/DuckDB measurements and code/source hashes, and explicitly marks itself as not a performance-acceptance gate.

### Review decisions

Keep the code’s package-delivered `workbench_schema.json` separate from runtime projection and Content schema records. The Current M500 and D672 now make that distinction explicit. No code relocation is needed.

Reconcile exact implemented RED and non-Policy M pins and evaluator coverage in the next Epic; do not mass-update comments or treat generic Policies as direct module implementation. The existing isolated profiling tool is not a latency/throughput acceptance run.
