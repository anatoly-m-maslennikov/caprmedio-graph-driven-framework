# Workbench runtime completion — 7 November 2026

The five runtime objectives are accepted. Local release **0.4.4.34** is installed and healthy. Native Codex UI acceptance remains explicitly deferred under C705; it is outside this completion scope.

## Objectives

| Objective | Verified result |
|---|---|
| Less latency | All twelve controlled single-source gates passed at 0.241–0.310 seconds; the existing 1.5-second limit is unchanged. |
| More throughput | The controlled 500-Atom batches passed all existing limits, including exact Header, carrier and Relation checks. |
| Less RAM and CPU | The same-source, profiler-off comparison below shows lower cold/rebuild CPU work and lower cold, peak and idle memory. |
| Less boilerplate | MCP and HTTP call the same Workbench backend API; HTTP no longer constructs and unpacks MCP envelopes. |
| Better architecture | Installed code/configuration owns Tool exposure; registry generation runs before package/image readiness. Runtime reload is default-off; registration avoids a full Atom catalog. |

## Same-source resources

Both fresh disposable containers indexed **5,483 Atoms** from one immutable copy of the actual Project's Current/Draft sources, with identical resource budgets and no profiler. Archives, Journals, projections and the installed Framework copy were excluded. This source snapshot is different from earlier reports; only the paired columns below are directly comparable.

| Measurement | Previous deployed image | Released image |
|---|---:|---:|
| Cold startup plus first index, wall seconds | 51.05 | 37.16 |
| Cold CPU seconds | 43.41 | 32.15 |
| Cold cgroup memory, MiB | 800.4 | 429.0 |
| Full reread, wall seconds | 37.21 | 32.57 |
| Full reread CPU seconds | 33.40 | 30.40 |
| Peak cgroup memory, MiB | 1070.7 | 559.3 |
| Memory after 15 seconds idle, MiB | 804.2 | 513.7 |
| CPU seconds during 15 seconds idle | 0.155 | 0.142 |
| Sampled uncapped CPU peak, percent of one core | 123.68% | 140.22% |

Cold CPU work fell **25.9%**; reread CPU work fell **9.0%**. Peak memory fell **47.8%**. Idle CPU remains about 1% of one core; this short window and boundary-reader overhead do not establish a reliable idle-CPU reduction.

The uncapped diagnostic had a higher brief CPU peak, despite less total work and faster completion. The Operator explicitly accepted keeping speed and recording this caveat. The deployed service remains capped at **one CPU and 1.5 GiB RAM**, with code hot reload disabled. No performance limit was relaxed.

CPU time is cumulative cgroup work, not elapsed time or peak utilization. Cgroup memory includes its accounting overhead/cache; Docker working-set samples in the raw evidence use different accounting and must not be added or substituted. Docker stats ran only on the host during reread; the idle window had no polling. Single-run variation and host contention remain limits. The measurements completed and matched; the diagnostic's empty snapshot-directory cleanup initially reported a permission error, then explicit owned-directory cleanup completed. All diagnostic containers and the held obsolete baseline image were removed.

Raw evidence: [resources](completion-resources-20261107.json). The baseline image and released image IDs are recorded there; [running runtime](completion-runtime-20261107.json) records the installed identity and limits.

## Latency and throughput regression gates

All **21 unchanged gates** passed on the controlled 5,000-Atom fixture. Bulk throughput counts changed Atoms through exact query-visible verification, not queued events. No weaker limits, indexes or constraints were introduced.

| Operation | Seconds | Atoms/second |
|---|---:|---:|
| cold_index | 27.876 | — |
| batch_create | 3.990 | 125.326 |
| batch_update | 4.962 | 100.769 |
| batch_rename | 5.274 | 94.806 |
| batch_rename_update | 5.338 | 93.674 |
| batch_move | 5.229 | 95.623 |
| scope_rename | 28.932 | 17.282 |
| batch_remove | 1.924 | 259.829 |
| full_reread | 27.203 | — |

Evidence: [controlled performance](completion-performance-20261107.json). These fixture timings are distinct from the larger real-source resource workload above.

## Live-project acceptance

MCP and HTTP returned identical query rows; frontend HTML and both assets loaded; query checking and the native tool bridge ping passed. All 54 configured Tools are advertised. The generated installed registry has 14 ordinary public code providers; Workbench and selected-route Tools complete the interface. Ordinary exposure is code/configuration-owned, while actual operation validation and Project exclusions remain in force.

The strengthened live canary passed **16 visibility checks in 220.341 seconds** on the running release. It checks exact nested Header container ID, Scope Unit name and destination filename/path through Atom create/update/file rename/move and retained-child Scope Unit move/rename, then verifies removal. The Scope Unit ID stays stable during its move/rename. No owned fixture or cleanup error remains.

Schema-preserving live Atom update, file rename and move took **0.339–0.350 seconds**. Creating/removing the first/last nested-Header fixture changed the observed schema and took about 20 seconds; Scope Declaration changes also rebuilt structure. Those are separate rebuild cases, not ordinary-edit latency. The canary validates direct source changes reaching the watcher/index; it does not claim lifecycle Workflows perform those edits.

The preflight originally tried binding not-yet-observed Header columns and stopped before source writes. It now checks stable identity first, then exact metadata after indexing, and uses stable identity for absence after last-column removal. Source schema validation was preserved.

Evidence: [live canary](completion-canary-20261107.json), [API parity](completion-api-20261107.json). Project-wide row counts in different reports may differ because separate methodology work continued; each resource pair used the same frozen inventory and matched row counts.

## Review and release evidence

- 390 tests ran in 54 selected modules in the initial release gate, with one explicitly opt-in canary skip. All eight Workbench Docker cases and all 21 performance gates passed. Three legacy fixtures failed; their expectations were corrected to explicit reload opt-in, code-owned registration and the full native Tool set.
- The corrected host/release gate passed **38 tests in eight selected modules**, without skips. Passing unchanged runtime checks were reused rather than rerun as a false full-suite claim.
- The real all-groups launcher proof passed. It also found and fixed the Compose boundary dropping the explicit reload opt-in; client/inspection environments remain sanitized and production defaults remain off.
- Real package verification found generated bytecode beside the registry. Generation now uses Python's no-bytecode mode; the importing-generator regression test and actual package identity verification pass. A stray generated test environment was moved out of the source tree; no source-safety check was weakened.
- Independent review accepted E677@21; E794@2 now requires exact live Header coverage. Existing scoped Policy prompts were reused; no new dependency or MCP library was introduced.
- Local release receipt: `.caprmedio_runtime/simple_local_release/reports/workbench-runtime-20261107-code-config-r6.md`. The original failed receipts remain; version numbers 32 and 33 were prepared but not installed. The installed version is 34.
- Release cleanup retains two legacy images whose Project ownership is unproven. The explicitly held old benchmark image was verified, released and removed after measurement. No unrelated resource was deleted.

The reviewed registration modules remain below 500 lines; the shared gateway is 246 lines, HTTP adapter 206 lines and QueryStore 479 lines. The work reused the existing backend and SDK rather than adding another server, service or generic framework. Production changes and the additional live-canary test changes are distinct: the canary was run from the host against the verified installed image.

## Deferred work outside these objectives

- C705: native Codex Workbench UI acceptance, explicitly deferred by the Operator.
- A1329: optional unselected performance experiments. They are not required to preserve the existing gates.
- A1322: general PROGRAMMATIC Policy proposals, still unadopted.
- Unchanged lifecycle/Atom-migration and Journal fixture failures belong to their owning work. The full repository suite is not claimed green. See [handoff](legacy-fixture-followups-20261107.md).

RMED contains design and evaluation criteria; the Epic records execution and acceptance only.

Final source verification: the running MCP queried exactly one Current row for `CA-P-2710`, with Status `Done` and Version `66`.
