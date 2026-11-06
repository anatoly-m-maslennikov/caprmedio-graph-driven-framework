# Workbench performance results

Runtime: **0.4.4.31**, local release `workbench-perf-20261107-r3`, port 56317. Workflows and Atom migrations were not changed.

## Real-project watcher latency

Same schema-preserving create, four edits and delete through the running backend. Times include mutation, watcher, indexing, HTTP request and polling. The temporary probe was removed; the schema stayed unchanged.

| Operation | Before (seconds) | After (seconds) |
|---|---:|---:|
| create 1 | 3.4291 | 0.2042 |
| update 2 | 3.3033 | 0.2027 |
| update 3 | 3.4431 | 0.2010 |
| update 4 | 3.2097 | 0.2065 |
| update 5 | 3.2750 | 0.2088 |
| delete 6 | 3.0470 | 0.2729 |

Median improvement: **16.0×** in this six-operation observation. This is a small latency sample, not a throughput benchmark.

## Verification

- 284 tests in 40 selected modules, one opt-in canary skipped, zero failed modules. This is not the full repository suite.
- Seven Docker acceptance cases and all launcher integration groups passed.
- A 5,000-Atom fixture exercised 12 watcher lifecycle cases at 240.8–307.7 ms, including host/container rename and move.
- Integrated tests reject full Header inference, Content compilation and graph reconstruction during ordinary edit, delete, reappearance and rename. Failed writes preserve the previous accepted state.
- Independent review found no actionable correctness issues.
- Read-only profiling of 4,988 actual source Atoms and 47 Scope Units measured 12.7–13.9 ms for changed-row materialization plus SQL application. It excludes watcher/request latency.

## Changes

- Reuse unchanged public rows, source facts, Header statistics and compiled Content declarations.
- Update changed direct relations and their inverse neighbours; preserve dangling-reference counts.
- Skip byte-identical edits.
- Append normal watcher-history rows and write automatic query history in the background. Explicit saves remain synchronous.
- Reuse Docker dependency layers across version bumps; the cache-backed dependency install completed in under two seconds.

## Limits and remaining work

- Startup, schema, Scope and actual Relation-registry changes retain the safe full-rebuild path.
- Native Codex UI acceptance C705 and optional performance experiments remain open; the Epic stays Active.
- The release deployed successfully but retained one image without Project ownership proof. Its receipt is completed_with_cleanup_pending.
- The attempted CA #3 report handoff was rejected by automatic approval review because destination permission was not confirmed. No message was delivered; the report is kept locally.

Evidence: `.caprmedio_tmp/workbench/performance-20261107/` contains `live-before.json`, `live-after.json`, `integrated-delta-profile.json`, `incremental-review.json` and `release-r3.log`. The release receipt is `.caprmedio_runtime/simple_local_release/reports/workbench-perf-20261107-r3.md`.
