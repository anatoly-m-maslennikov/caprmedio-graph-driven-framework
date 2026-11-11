# Runtime acceptance — 7 November 2026

## Controlled Docker acceptance

Four current-image tests passed in 238.571 seconds: performance gates, watcher mutations/rebuild/restart, actual MCP query/save/load/schema calls, and HTTP query/check/static assets. Sources were read-only. The live Project container was not restarted or replaced.

Image: `sha256:6ffb6fb667f4960837089c6c7fb97734a6b168b69effd35c339b96f9e353c836`.

| Operation | Items | Seconds | Limit |
|---|---:|---:|---:|
| cold_index | 1 | 24.534 | 45 |
| batch_create | 500 | 3.790 | 15 |
| batch_update | 500 | 4.644 | 15 |
| batch_rename | 500 | 5.036 | 30 |
| batch_rename_update | 500 | 5.146 | 30 |
| batch_move | 500 | 4.877 | 30 |
| scope_rename | 500 | 32.443 | 60 |
| batch_remove | 500 | 2.629 | 15 |
| full_reread | 1 | 27.160 | 45 |

All twelve single-mutation visibility checks passed at 0.241–0.306 seconds, below the 1.5-second limit. The fixture contains 5,000 baseline Atoms. Bulk checks verify final content, version, filename/path, container, direct and derived relations, rather than counting filesystem events alone. Throughput is changed Atoms divided by elapsed time through verified query visibility. Cold indexing proves that the database was absent before the timer. Full reread is measured separately. Raw metrics are in `performance-acceptance-20261107.json`.

Container peak: 481,996,800 bytes (459.7 MiB); OOM kills: zero. These controlled-fixture results are not a new live-project deployment claim. The separate real-source RAM comparison is in `ram-report-20261107.md`.

## Retained runtime

Focused checks cover real DBOS queued Revert execution, rejection of retired AI execution before durable writes, MCP request context and confirmation checks, default single-process startup, explicit hot-reload opt-in, frontend development reload settings, Docker launch/network behavior, profiler isolation and relation parity across renamed batches. AI Agent adapters, transports, mock runtime and agent image/service are removed from active source. Generic deterministic execution and queues remain. Historical delivery snapshots and Run data remain unchanged.

The image acceptance predates the final wrapper-only restoration of bounded/redacted Docker startup diagnostics; the focused network tests (3) and HTTP tests (15, one Docker opt-in skip) passed after that correction.

The final MCP cleanup also postdates the image: the removed AI-integrated profile/continuation modules no longer have an active caller. The retained source tool name returns `disposition: rejected`, `outcome: retired`, before any queue/profile load. Three isolated retirement tests and six default-MCP tests pass; the worker also verified generic queue freeze and preview routing. The new regression test explicitly adds its required Tools path, so it does not depend on another test importing it first. This focused source proof is not a new image acceptance.

## Broader suite boundary

A broader APP discovery run collected 494 tests and finished with 11 failures, 82 errors, 14 skips and one expected failure. It began before the retirement fixture cleanup completed, so its totals include subsequently fixed stale Agent/mock assertions and imports. Do not treat that run as final green or as a current count of unresolved failures.

Independent unresolved groups remain in unchanged Atom-migration/lifecycle and Journal fixtures:

- Subject-update setup rejects changed/missing preserved legacy root fields (`ProposedCarrierError`). A fresh focused reproduction confirms this remains; source validation was not weakened.
- Status-matrix and legacy Subject fixtures conflict with current carrier assumptions.
- Journal fixtures raise `PartialAppendError` in selected observation/creation/replacement tests.

Those migration/Workflow repairs are outside this runtime task. The full 42-minute run was not repeated after focused retirement repairs. Its captured log is `.caprmedio_tmp/workbench/performance-gates-20261107/core-retirement-suite.log`. Fresh APP collection resolves 522 tests without failed imports; collection does not establish passing execution.

## Not deployed

The running 0.4.4.31 container is unchanged. A local release and live canary are separate acceptance steps. Keep the Epic Active: native UI acceptance and the recorded optional experiments are also open.
