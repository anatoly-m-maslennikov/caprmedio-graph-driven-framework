# Runtime optimization acceptance — 7 November 2026

Implemented and tested in source. No local release or live-service restart was performed. The Epic remains Active.

## Code/configuration registration and shared backend

MCP registration reads the code-owned `tool_providers.json` inventory's generated `tool_registry.json`. The generator derives descriptors and schemas from the installed package's code; it does not read Atom declarations. Local-release packaging generates that asset before final package identity verification and image preparation. Docker regenerates it after copying engine code. The post-readiness `tools_catalog.json` remains discovery output only.

Startup and generic Tool invocation no longer build a full Atom catalog to authorize exposure or freshness. Project configuration still controls exact exclusions, and each operation retains its own source/business validation. An empty selected-route list means no ordinary selected routes. Provider loading uses the selected package root. Missing/malformed configuration fails explicitly rather than falling back to Atom scanning.

MCP and HTTP reuse the same backend operation path. Shared HTTP no longer constructs/unpacks MCP request/result envelopes. The common boundary retains Project selection, current-contract checks, exclusions, owner leases, cancellation cleanup and health observations. Transport envelope parsing stays in the adapters; redundant HTTP operation checks were removed in favor of existing backend validation. The official MCP Python SDK is unchanged; no new dependency or server was added.

Sources: M506@2, D704@1, E798@1, D673@14 and the ten reconciled registration/frontier sources indexed in the working packet. Actual runtime handlers, Workflow definitions and Atom-migration behavior were not rewritten.

## Backend cache and rebuild work

M465@23 and E677@20 cover aggregate-only Header counters, private UTF-8 source bodies and reuse of one full public-row projection for SQL insertion and the retained snapshot. There is no second retained decoded body or per-source Header contribution map. Candidate state publication remains after a successful transaction.

The first exploratory UTF-8 run exposed an existing duplicate full-build public conversion. That work was removed, then all variants were rerun against one captured source state. Public row values and hashes match across all three variants; the raw evidence includes the identical source fingerprint and public-row digest. The normal parser continues returning strings and original line breaks are preserved.

## Unprofiled Backend comparison

Each variant ran in a fresh host Python interpreter, without cProfile, tracemalloc tracing, a heap ownership walk or a watcher. It read the same 5,501 source records and indexed 5,489 Atoms plus 48 Scope Units. The previous Backend source comes from commit `6d86a5d9df`; the Header variant also uses the accepted full-build reuse; the final variant adds byte caching. These are direct Backend timings, not filesystem-watcher latency.

| Backend variant | RSS MiB | Cold seconds | Median direct delta ms |
|---|---:|---:|---:|
| Previous Backend | 337.7 | 20.96 | 8.02 |
| Header aggregates + full-build reuse | 326.9 | 21.78 | 8.34 |
| Both caches + full-build reuse | 304.5 | 19.81 | 7.42 |

The final combined Backend used **33.2 MiB less RSS** in this run. Body-object payload fell from about **54.2 MiB to 30.6 MiB**; retained per-source Header contributions fell from 5,489 to zero, with aggregate counters retained. Do not add payload estimates to RSS savings. Allocator residency and a single timing sample can vary; the Docker gates below provide separate end-to-end acceptance.

## Fresh same-source container RAM

Two fresh disposable containers read the same current Project sources through read-only mounts and indexed **5,489 Atoms**. Both had a 1.5 GiB limit and no profiler. The running Project container was not used as one of the measurement processes or restarted.

| Measurement | Deployed-image baseline | Candidate |
|---|---:|---:|
| Docker working set | 653.5 MiB | 297.9 MiB |
| Summed process PSS | 684.4 MiB | 341.2 MiB |
| Persistent launcher/Python processes | 3 | 1 |

Working-set reduction: **355.6 MiB (54.4%)**. This is cumulative across compact source records, direct Python startup, default-off reload, code/config registration and the new Backend cache/rebuild changes. It is not attributed wholly to either new cache. PSS and Docker working set use different accounting and are not additive. The earlier 680.9→410.1 MiB capture used an earlier source/runtime capture and must not be subtracted as an exact isolated saving for this pass.

Baseline image: `sha256:bc37d7e2a68129583e0d6d394fbe843cc00a79909e0322895a3608d2bd92a0a7`.
Candidate image: `sha256:726b32fc48f0d9ae42425cbef766cfd9f84769d4960c0a39f988c7e487e5407c`.

## Docker acceptance

Four Docker tests passed in **217.931 seconds**: the 5,000-Atom performance matrix, watcher lifecycle/reread/restart, actual MCP query/save/schema operations and HTTP query/check/assets/read-only behavior. All **21** measured hard gates passed without changing their limits.

| Operation | Seconds | Limit |
|---|---:|---:|
| cold_index | 23.739 | 45 |
| batch_create | 3.804 | 15 |
| batch_update | 4.707 | 15 |
| batch_rename | 5.041 | 30 |
| batch_rename_update | 5.132 | 30 |
| batch_move | 4.921 | 30 |
| scope_rename | 28.867 | 60 |
| batch_remove | 2.335 | 15 |
| full_reread | 25.008 | 45 |

Twelve single-source visibility operations took **240.7–309.1 ms**, below the 1.5-second gate. Container peak was **427,483,136 bytes (407.7 MiB)**, with zero OOM kills. The previous controlled image run peaked at 481,996,800 bytes; these peaks belong to the controlled fixture, not the same-source idle RAM table above.

## Focused checks and scope limits

- 98 Backend cache/schema/Content/hash/failure-publication tests passed.
- 32 focused registry/asset/error/route checks and 14 bootstrap/default/blacklist checks passed.
- 24 shared HTTP/MCP parity, Project denial, cancellation and observation tests passed.
- 30 existing local-release tests plus three generation/package-order/stale-output/failure tests passed. Release tests use disposable fixtures; no release was performed.
- Changed Backend and new focused code lint checks passed. Existing C901 warnings in unrelated/unchanged release-support bodies remain; no validation was weakened to silence them.

After image acceptance, only module trace comments and source/report bookkeeping were updated; executable behavior was not changed.

The full repository suite is not claimed green. Previously documented lifecycle/Atom-migration and Journal fixtures remain outside this runtime task; seven direct-subject protocol cases still reach existing `complete-carrier-invalid` source validation after registration succeeds. Native-host UI acceptance C705 and live release/canary remain open. Retained 500 real-project benchmark Atoms were not removed.

Raw evidence: `optimization-performance-20261107.json`, `optimization-ram-20261107.json`, `optimization-backend-variants-20261107.json`. Diagnostic runners and detailed logs remain under `.caprmedio_tmp/workbench/code-registry-ram-20261107/`.
