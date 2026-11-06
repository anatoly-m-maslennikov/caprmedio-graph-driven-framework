---
atom_id: CA-A-1329
ref_id: CA-A-1329@1-draft
container:
  scope_unit: CA-SU-45
role: Analysis & Advisory
form: Specification Proposal
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 4
relations:
  depends_on:
  - CA-M-465
  - CA-M-490
  - CA-M-502
  - CA-E-677
status: Draft
version: 1
updated_at: 2026-11-07 01:34:24 +0400
carrier_destination:
  file:
    name: CA-A-1329@1-draft-WORKBENCH_BACKEND-SPECIFICATION_PROPOSAL--compare-workbench-performance-options.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/02_analysis/draft
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---

## Summary

Compare Workbench performance options

## Proposal

Measure two things separately: latency from one source edit to query visibility, and throughput for mass operations. Use the actual repository as well as the existing approximately 5,000-Atom fixture. Include content-only updates, relation additions/removals, file create/delete, mass find-and-replace, and Scope Unit moves/renames with Declaration updates. Report changed rows, affected neighbours, elapsed time, rows per second, query responsiveness and memory. Keep cold load and structural/schema rebuilding separate from ordinary edits.

The current implementation cycle keeps DuckDB and its transaction model. It reuses unchanged parsed/materialized/public rows and their hashes, processes changed direct relations and affected inverse neighbours, skips no-op events, appends watcher history and writes automatic query history asynchronously. These adopted changes are the comparison baseline, not a proposal to rewrite the backend.

## Experiments

| ID | Option | Comparison and limit |
| --- | --- | --- |
| E01 | Bulk SQL mutations | Compare individual DELETE calls plus executemany with set-based DELETE USING and native bulk INSERT for the same delta and one transaction. Preserve atom/graph consistency and result snapshots. |
| E02 | Event batching | Compare existing queue draining with bounded batching for large edit bursts. Parse each affected path once per batch. Preserve every watcher-history observation. Measure the latency/throughput tradeoff; do not add an arbitrary delay to ordinary edits. |
| E03 | Shorter database critical section | Move preparation that does not access mutable database state outside the connection lock. Keep commit/publication and connection access protected. Measure query responsiveness during indexing. |
| E04 | Concurrent database connections | Test a dedicated writer and separate reader connections inside the existing process. Verify DuckPGQ and cached-result behavior before adopting. Never share one connection unsafely or remove its lock alone. Add parallel writers only if disjoint writes show a measured benefit. |
| E05 | Append-only state with +1/-1 | Compare signed cancellation/insertion rows and a collapsed current-state view against bulk delete/insert. Include ordinary SQL and graph queries, duplicate events, deletion, inverse edges, storage growth and compaction. DuckDB has no ClickHouse CollapsingMergeTree engine; do not assume automatic collapse. Included for evaluation, not selected as current storage. |
| E06 | Latest-version state | As an alternative to E05, compare append-only row versions plus deletion markers and a current-state view. Apply the same query/graph/compaction checks. Do not implement both alternatives in production. |
| E07 | Index cost | Measure database mutation time with the existing primary/unique constraints and with optional constraints removed in an isolated experiment. Identify constraints needed by DuckPGQ. Do not remove live uniqueness checks or assume indexes rebuild after every edit. |
| E08 | Faster serialization/parsing libraries | If profiles still show significant serialization cost, benchmark orjson. Check exact canonical hash behavior, datetimes, nulls, numbers and Unicode. For cold reading, evaluate the installed safe LibYAML backend without changing validation. Shared parser changes remain a separate owned implementation lane. |
| E09 | Native hot function | If a measured CPU hotspot remains after incremental processing, benchmark a small Rust/PyO3 implementation; consider Go only where its library or standalone boundary gives a concrete advantage. Include conversion/call/build costs. Do not rewrite the backend or add a service merely to change language. |
| E10 | Log-retention CPU work | At realistic retained-history sizes, compare normal append without scanning all unexpired rows against the current retention pass. Preserve exact 48-hour expiry, the watcher row cap and duplicate observations. |
| E11 | Lighter derived-state durability | Benchmark supported DuckDB persistence/checkpoint settings for the disposable index and result cache. Compare buffered/batched writes where supported and, only within the memory budget, in-memory derived state. Do not invent an unsupported WAL-off option or relax explicit saved-query/View persistence. Keep coherent committed query results. |
| E12 | Alternative file watchers | Compare watchdog with alternatives that preserve native create/update/delete and old/new move/rename reporting, repository boundaries and shutdown. Include Rust notify (which exposes old/new rename paths) and evaluate watchfiles only if its added/deleted/modified public events can preserve the required move semantics without guessing. A faster watcher that loses required event meaning is not equivalent. |
| E13 | Parallel Python preparation | Compare ordinary I/O threads, a free-threaded CPython build, and bounded processes or isolated interpreters for independent changed-file parsing. Include dependency compatibility, GIL state after imports, memory and data-transfer costs. Keep one coherent publication step; measure bulk throughput separately from single-edit latency. |

## Conditional option

Physical partitioning is a later, growth-dependent experiment. Try it only if profiles on a larger dataset show scans or compaction dominate and a real partition key enables pruning. Roughly 5,000 Atoms alone do not justify splitting tables. SQL window PARTITION BY is not physical partitioning.

## Decision boundary

Keep the design simple. Add no generic persistence layers or services for disposable derived data. The durability experiment concerns disposable database/cache state; source Atoms and explicit saved items remain outside that tradeoff.

Keep source Atoms authoritative and unchanged by these experiments. Keep hashes in derived cache/database state rather than writing a hash into every source Atom. Do not weaken explicit Save durability: saved queries and Views finish persistence before their IDs are returned. Automatic logs may be delayed as already adopted. A rebuildable database may be discarded and reread after failure, but queries must still expose coherent committed state.

Run experiments in disposable state. Record before/after evidence, retain only useful changes, then update and review the relevant RMED before implementing a selected alternative. No experiment in this proposal changes the current runtime contract by itself.

## Sources

- DuckDB indexes: https://duckdb.org/docs/current/sql/indexes
- DuckDB concurrency: https://duckdb.org/docs/2.0/connect/concurrency
- ClickHouse signed collapsing: https://clickhouse.com/docs/reference/engines/table-engines/mergetree-family/collapsingmergetree
- PyO3: https://pyo3.rs/main/index.html
- orjson: https://github.com/ijl/orjson
- PyYAML safe LibYAML loaders: https://pyyaml.org/wiki/PyYAMLDocumentation

Free-threading reference: https://docs.python.org/3.14/howto/free-threading-python.html
Watcher references: https://docs.rs/notify/latest/notify/event/enum.RenameMode.html ; https://watchfiles.helpmanual.io/api/watch/
