# Workbench RAM report — 7 November 2026

## Measured deployed runtime

These are measurements of release **0.4.4.31**, container `1e55d3ba77ff`, before the pending source changes were deployed. PSS apportions shared pages between processes; RSS counts each process’s mapped pages and should not be added as unique usage.

| Process | PSS | RSS |
|---|---:|---:|
| uv launcher | 40.4 MiB | 41.6 MiB |
| HTTP gateway and Workbench | 675.1 MiB | 686.3 MiB |
| MCP hot-reload implementation child | 120.3 MiB | 131.6 MiB |

The container cgroup recorded 857.7 MiB, with a historical peak of 921.6 MiB and a 1,536 MiB limit. Docker’s displayed working-set figure was lower because its cache accounting differs. These figures describe one captured runtime state, not a fixed reservation.

DuckDB managed about **19 MiB**, including about **6 MiB of indexes**. Small retained query-result tables were present; neither they nor the indexes explain the main process footprint.

The Workbench process retains parsed source bodies, Headers, schema metadata, projected rows and relation state. Python/native allocators also retain memory after rebuilds. DuckDB’s own memory report does not measure that whole process.

## Source-cache analysis

The 5,493-Atom parity check found about **110 MiB of duplicated UTF-8 text** in `section_markdown` and `direct_markdown`. The candidate now reconstructs those values from the original Markdown body and line spans. All compiled Content values and public row hashes matched the previous representation. This is eliminated string payload, **not a measured 110 MiB RSS reduction**.

A separate object-graph traversal after section compaction but before direct-text compaction found about **175 MiB of reachable Python objects**. It included roughly 30 MiB each of original source bodies and duplicated direct text, 15 MiB of projected public rows, 6 MiB of relation facts and 4 MiB of graph state. Most reader/materializer/reuse maps point to shared objects. The reuse map itself owned about 0.6 MiB; deleting it would sacrifice incremental speed without recovering the apparent inclusive size. This diagnostic is a separate process and must not be added to the deployed-process totals.

## Rebuild behavior

An isolated real-source experiment ran three full derived-state rebuilds against one captured projection. RSS rose from 345 MiB initially to roughly 401–415 MiB after warm-up, with a 417 MiB peak. DuckDB-managed memory ranged from 9–25 MiB. The three cycles did not show runaway growth; they do not prove indefinite stability or explain every allocator page. Ordinary synthetic row deltas remained about 10–11 ms with stable RSS in that experiment.

## Changes and limits

- The candidate removes the resident `uv run` supervisor by starting the built Python interpreter directly. Its measured deployed PSS was about **40 MiB**.
- The compact source cache eliminates duplicate Markdown strings while retaining parsing/value/hash behavior.
- The opt-in profiler records CPU calls, Python allocation snapshots, high-water RSS and available DuckDB allocation data separately. Its durations are diagnostic, not performance acceptance results.
- AI Agent dispatch and its Docker service are removed from active source. MCP hot reload is separately optional and disabled by default; `CAPRMEDIO_HOT_RELOAD=1` enables its implementation child. Removing inactive Agent files alone is not evidence of a corresponding live RAM saving.

No memory cap reduction, forced garbage collection, allocator trimming or index removal was justified by these measurements. No local release was performed for this report.

## Evidence

Captured evidence is under `.caprmedio_tmp/workbench/performance-gates-20261107/`: `ram-process-accounting.json`, `ram-before.json`, `real-content-parity.json`, and `ram-native-results/full.json`. The opt-in command is `APP_WORKBENCH/tests/profile_workbench.py --project-root <project>`; use the repository’s supported Python environment. Diagnostic artifacts are intentionally outside source Atoms.


## Same-source container comparison

Two fresh disposable containers indexed the same **5,485 Atoms** with the same read-only Project sources, empty owned runtime directories and 1.5 GiB memory limits. The live Project MCP was not changed.

| Measurement | Previous image | Candidate image |
|---|---:|---:|
| Docker working-set RAM | 680.9 MiB | 410.1 MiB |
| Sum of observed process PSS | 711.0 MiB | 411.6 MiB |
| Persistent Python/launcher processes | 3 | 1 |

The Docker working set fell **270.8 MiB (39.8%)**. PSS and Docker working-set accounting differ; do not sum these rows. The candidate combines source-cache compaction, direct Python startup and default-off MCP hot reload; this test does not attribute the saving to each change separately.

Previous image: `sha256:bc37d7e2a68129583e0d6d394fbe843cc00a79909e0322895a3608d2bd92a0a7`. Candidate image: `sha256:c187a6aaab6c8588bffd395a26ce37f18a5344df2bb8a722cd0a2acb57167dbd`. Full raw results: `ram-same-source-comparison-20261107.json`. These are fresh-container diagnostics, not a deployment claim or steady-state endurance test.

## Deeper current-code census

An isolated read-only run captured 5,497 valid source records and indexed 5,485 Atoms plus 48 Scope Units. Before the ownership walker, the indexed process RSS was **318 MiB**. Its deduplicated reachable Workbench Python objects totaled **148 MiB**; DuckDB managed **24 MiB**. These overlap process RSS and are not additive to it.

| Retained Python component | Exclusive ownership |
|---|---:|
| Original Markdown body strings | 54.2 MiB |
| Per-source Header schema contributions | 18.7 MiB |
| Public Atom projection rows | 14.7 MiB |
| Parsed Content properties | 12.9 MiB |
| Raw Header maps | 6.8 MiB |
| Incremental source-row reuse map | 0.6 MiB |

The diagnostic ownership map itself temporarily inflated process RSS to over 900 MB and left allocator arenas behind. That is profiler overhead, not a normal Workbench peak. No leak or need for production forced GC was established.

## Ranked further candidates — not implemented

1. **Aggregate Header statistics without per-source contribution copies.** About **18.7 MiB** is owned by that map. `MaterializationDelta.old_atoms/new_atoms` already carries exact touched Headers; recompute contributions for those rows only and retain the small aggregate counters. Verify type changes, rename/delete, collisions and failed-transaction immutability. Avoid global scans.
2. **Cache original Markdown as UTF-8 bytes.** Current bodies occupy 54.2 MiB as Python strings versus 30.6 MiB as bytes, an estimated **23.6 MiB** saving. An em dash or arrow widens the whole Python string. Decode transiently for Content/schema extraction; benchmark ordinary edits, all 500-file phases and full rebuilds before adopting it. Public parser values, hashes and line breaks must stay identical.
3. **Avoid full generic catalog construction for MCP registration.** Registration currently builds 3,488 full Atom rows to retain 15 Tool declarations. The isolated probe estimates **24–43 MiB** of startup peak/allocator residency may be avoidable. This is an estimate, not a measured permanent saving; preserve duplicate/admission diagnostics and generic discovery behavior.

Do not add these estimates together as a guaranteed RSS reduction. The first two target retained objects; the third targets startup allocation.

## Result retention

A narrow 5,485-row query added about **0.26 MiB** of DuckDB-managed memory; a full 5,485×56-column result added about **12.2 MiB**. Dropping it removed its result table and released/evicted the buffers. `_results` stores metadata, not another Python row copy. Open Views intentionally pin results under the accepted retention rule. Changing that policy or deleting incremental caches is not justified by this experiment.
