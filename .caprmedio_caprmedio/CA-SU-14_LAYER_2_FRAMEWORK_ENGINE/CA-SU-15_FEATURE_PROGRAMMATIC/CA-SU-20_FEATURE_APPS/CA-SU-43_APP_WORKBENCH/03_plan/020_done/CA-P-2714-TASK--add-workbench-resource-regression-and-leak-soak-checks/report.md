# Workbench resource and leak acceptance

Completed a real 1800.0-second same-owner backend soak with 169 cycles on 5,000 disposable Atoms. No profiler or live Project source mutation was used. Image: `sha256:38f610345b6590560a52733b26af4bd653adea49cc3e98d306d52be6060df4db`. Container: one CPU, 1,536 MiB RAM. Filesystem fixtures are created inside the disposable container; separate unchanged performance tests use the existing host-mounted fixture.

## Fixed issues

- Empty relation buckets accumulated after unique Atom deletion. They now disappear while other edges and counterpart updates remain intact.
- Correct native directory events installed redundant observers. They now reuse the root recursive observer; the misreported-directory fallback remains tested.
- A destination-create event could precede source removal, retaining a physically missing alias and causing a 7–9 second full rebuild. Reconciliation now prunes only missing aliases of the affected reference. Real duplicate files remain rejected.

## Acceptance

- All 21 unchanged performance gates passed separately on the production-identical pre-oracle-correction image. Single-file visibility: 239.6–318.6 ms.
- 53 focused source/watcher/relation/resource-invariant checks passed.
- The short Docker guard and real 30-minute soak passed.
- The separately discovered required short guard passed through the standard suite loader: one test, zero skips. The long test remains optional in ordinary runs.
- Same PID and owner throughout the continuous phase; no early reread or forced garbage collection.
- Settled cgroup RAM: 420.3–507.5 MiB. Peak: 512.6 MiB. Idle CPU: 0.0349 seconds over 15 real seconds.
- Source/reference/relation inventories and exact key digests returned to baseline after every cleanup. No empty outgoing buckets remained.
- Exactly one intentionally open anchor result remained before reset. Reruns dropped prior tables; closed Views released pins and expired by TTL; duplicate Views ran independently.
- Watcher work and asynchronous query logging drained. Python threads and open descriptors stayed at 6 and 9. No OOM occurred.
- A final full reread cleared all process-local results and restored the same source inventory.

Frozen limits are in CA-M-508@4; numeric thresholds are never recalculated from acceptance output. Calibration observations and actual CLI mode are preserved separately. Earlier unsuccessful attempts are not counted as acceptance. Required short and optional long entrypoints are separate so the standard suite can require the short case without requiring the 30-minute case.

## Scope and limits

This is a bounded backend soak, with the real watchdog, DuckDB and shared Workbench Tool boundary. It is not a proof that no leak can ever occur or a long-running MCP transport test. The global legacy-fixture suite was not rerun. No local release or deployment was performed; the installed 0.4.4.34 service is unchanged.

## Running the checks

The normal suite discovers `test_workbench_resource_docker_e2e.py` as a required Docker case. To opt into the additional long case, set `CAPRMEDIO_WORKBENCH_SOAK_SECONDS=1800` or a larger duration. Both use the suite-prepared current-code image through `CAPRMEDIO_IMAGE`. A positive duration shorter than 1,800 seconds is rejected.

[Soak metrics](soak.json), [short guard](guard.json), [performance gates](performance.json), [source IDs](sources.json), [code provenance](frozen-code.json).

Final source-only ordering check: M508 Tier 5 uses IS_METHOD_FOR toward R2786 Tier 4; E799/E800 at Tier 6 evaluate M508 Tier 5. Their Claims and all tested behavior are unchanged. Module pins retain the implemented Claim versions. [Metadata review](tier-review.md).

After acceptance, extra blank lines at EOF were removed from two test modules. Behavior is unchanged; tested-to-final hashes are recorded in formatting-only.json.

## Subsequent local release

Version **0.4.4.35** was then installed and verified for Workbench and query_run. All 105 focused checks passed; the page/assets and real HTTP/MCP queries work. Other tools were outside the selected scope. One old image with unproven ownership was retained. See [local-release verification](local-release-0.4.4.35/verification.md). The no-deployment statement above describes the earlier resource-test pass.
