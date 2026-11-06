# Watcher visibility latency

Date: 2026-11-06

E780@2 adds mutation-to-DuckDB visibility timing to the existing Docker E2E. The timer starts before the actual file operation and stops only when SQL returns the expected Atom version/path, or no row after removal. It reports elapsed milliseconds and poll count; it adds no speed threshold.

## Small fixture E2E

Passed: one focused Docker E2E, nine measured cases, 33.239 seconds for the complete test including existing reread/restart/log checks. Ruff and Python compilation passed. The existing 20-second observation deadline remains; polling is 200 ms. Shared HTTP request timeout is 60 seconds, so the loop deadline is not a hard request deadline.

| Operation | Visibility, ms |
| --- | ---: |
| create | 241.3 |
| update | 241.4 |
| host_rename | 255.2 |
| host_move | 244.7 |
| container_rename | 328.4 |
| container_move | 287.7 |
| remove | 240.2 |
| enter_control_root | 242.9 |
| leave_control_root | 253.2 |

## Running project container

Local release 0.4.4.27, real repository, baseline 4,961 Atoms and 47 Scope Units. Host-side file mutations reached SQL through the running Docker backend. These are warm file-change measurements, not startup measurements. The existing-folder probe polled at 100 ms; the two-Draft batch polled at one second. Timings include mutation, watcher batching, refresh, query and polling overhead. The final small-fixture E2E briefly overlapped the first live lifecycle; these are observed workstation timings, not isolated laboratory measurements.

| Operation, one Draft | Visibility, seconds |
| --- | ---: |
| create | 52.547 |
| edit | 51.678 |
| host_rename | 59.896 |
| host_move | 52.091 |
| remove | 60.747 |

| Operation, two Drafts changed together | Both visible, seconds |
| --- | ---: |
| create | 47.820 |
| edit | 48.702 |
| remove | 52.218 |

All three temporary numbered Drafts were removed, and SQL confirmed no remaining rows for their IDs. Their files were never promoted or archived. The redundant remaining individual samples were stopped after the first lifecycle; the two-Draft batch completed create/edit/remove coverage instead.

## Open runtime findings

- A Draft created inside a newly host-created nested folder did not appear within 90 seconds. The technical change log contained directory create/remove events, but no child-file event for that probe. Its temporary files and folder were removed. This establishes a missed-event reproduction; the underlying cause was not established.
- Existing-folder changes took roughly a minute. Current service code captures all sources, rebuilds/materializes the graph, drops/recreates the public/internal tables and inserts the full dataset after a changed snapshot. That is the main optimization candidate; this task did not profile individual phases or change production behavior.

The fast fixture does not establish acceptable performance on a 5,000-Atom repository. No SLA, full-suite pass, runtime fix or new release is claimed.

## Evidence

- `.caprmedio_tmp/workbench/watcher-latency-e2e.log` and `watcher-latency-e2e.json`
- `.caprmedio_tmp/workbench/watcher-latency-live-single.json`
- `.caprmedio_tmp/workbench/watcher-latency-live-batch.json`
- `.caprmedio_tmp/workbench/watcher-latency-new-directory.json`
