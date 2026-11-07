---
atom_id: CA-P-2710
ref_id: CA-P-2710
container:
  scope_unit: CA-SU-00
role: Plan
form: Plan
label: Epic
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 3
status: Active
version: 64
updated_at: 2026-11-07 14:32:40 +0400
carrier_destination:
  file:
    name: CA-P-2710-EPIC--make-workbench-queries-paged-and-frontend-modular.md
    path: .caprmedio_caprmedio/03_plan
---

## Summary

Make Workbench queries paged and the frontend modular

## Objective

Improve Workbench queries, Views and the read-only result grid according to the reviewed RMEDO.

## Scope

Workbench RMEDO, implementation, tests, documentation and local deployment. Unrelated Engine and methodology migrations remain outside this Epic. Design belongs in RMED, not in task descriptions.

## Completed work

- [x] Implement and release the shared paged SQL backend, Svelte frontend and saved-item Journal.
- [x] Implement and verify MCP query/discovery, Project context and full reread.
- [x] Declare CODEX_EXTENSION and implement Workspace/View controls and the session-hook/skill scaffold.
- [x] Fix the four reported defects, record Resolved Problems C700–C703 and retain linked regression Evaluations E750–E753.
- [x] Correct the local-release startup caller and complete local release 0.4.4.23.
- [x] Prepare, review and adopt watcher change-log and initial sync/interface RMED.
- [x] Implement the watcher, change log, nonblocking status, initial interface refinements and ordinary-file disappearance fix in source.

## Earlier completed implementation cycle

The following checklist records the earlier grid/View cycle, not the later changes audited on 6 November.

- [x] Create remaining RMED for the requested Workbench changes.
- [x] Review against the latest Operator input and related Current sources; fix contradictions and gaps.
- [x] Adopt the reviewed RMED.
- [x] Gather or reuse applicable Method Policies from PROGRAMMATIC through each target Scope Unit and compile one implementation prompt for that Scope Unit.
- [x] Gather the adopted Requirements, Evaluations, Delivery and non-Policy Methods for each implementation scope.
- [x] Implement those sources and reconcile callers, fixtures, configuration and documentation.
- [x] Implement and run behavior-focused end-to-end tests.
- [x] Review and fix the integrated changes.
- [x] Perform local release and verify the running MCP and browser behavior.
- [x] Record verified completion.

The reviewed source packets cover the result grid, display settings, unified Views, transient result retention and hourly query-log batches. Query-log retention is now two days, following the latest Operator decision. Temporary result retention follows its separate Workbench contract.

## Current implementation cycle — 48-hour input review

Review record: `input-coverage-review-20261106.md` in this Epic folder. Specification belongs in RMEDO; these tasks track the work.

- [x] Review the complete 48-hour input window against RMEDO, tasks, implementation and verification.
- [x] Update, review and adopt the RMEDO identified by the audit, including E677 and the pending Draft packet.
- [x] Record Header read-compatibility readiness and the held source/writer cutover boundary.
- [x] Create and review the Method guidance for query-writing style.
- [x] Resolve C704 and verify its linked watcher Evaluation.
- [x] Complete the Workbench backend module-trace audit.
- [x] Complete the remaining MCP adapter/test trace corrections.
- [x] Gather the applicable Policy prompt and accepted implementation sources for each scope.
- [x] Complete and review implementation of the accepted RMEDO.
- [x] Run the outstanding E780 Docker acceptance and record the results.
- [x] Perform local release and verify the released Workbench backend.
- [x] Adopt E794.
- [x] Run E794 against the released candidate and record the live-project results.
- [x] Complete the native Codex Workbench implementation and disposable-host bridge verification.
- [ ] Resolve C705 and verify the native UI in the actual Codex host.
- [ ] Review final coverage and record Epic acceptance.

## Editor formatting cycle

- [x] Update, review and adopt the formatter RMED.
- [x] Refresh the frontend Policy prompt and implementation source index.
- [x] Implement the accepted formatter RMED.
- [x] Verify formatting through editor and command-palette end-to-end tests.
- [x] Review the integrated formatter change.
- [x] Verify the editor in the released, tested artifact.

Source and review index: `.caprmedio_tmp/workbench/rmed-reconcile-20261106/formatter-adoption.json`.

Verification: three formatter checks, all 17 frontend Node tests, TypeScript, shared builds, two actual-backend Chrome formatter scenarios and independent code review passed. Existing result identities survived both successful formatting and parse failure. Evidence: `formatter-root-verification.json` and `formatter-code-review.md` in the same packet. This source change is not deployed yet.

## View actions cycle

- [x] Update, review and adopt the View-action RMED.
- [x] Refresh the scoped Policy prompt and implementation-source index.
- [x] Implement the accepted View-action RMED across its interfaces.
- [x] Run the View-action end-to-end checks and review the integrated change.
- [x] Verify the released View actions through MCP and the tested shared artifact.

Source, review and verification index: `.caprmedio_tmp/workbench/view-actions-20261106/`.

Source acceptance passed: 23 browser cases, three disposable-host native bridge cases, five backend tests, 12 MCP/HTTP tests and 17 frontend Node tests. TypeScript, builds, scoped reviews and diff checks passed. Deployment and actual Codex-host acceptance remain open. Permanent record: `view-actions-acceptance-20261106.md` in this Epic folder.

## Real-project performance cycle — row reuse and logs

- [x] Measure ordinary real-project edits before the change, without changing the schema.
- [x] Update, review and adopt the Backend RMED for the approved performance and log changes.
- [x] Refresh the Backend Policy prompt and accepted implementation-source list.
- [x] Implement and review the approved changes.
- [x] Run the targeted regressions and realistic end-to-end checks.
- [x] Release and compare the same real-project operation matrix before and after.
- [x] Record measured results and remaining acceptance items.

## Current priority — bounded source deltas

Sources: CA-M-465@19, CA-M-500@2 and CA-E-677@14.

- [x] Review and adopt the incremental schema/graph RMED.
- [x] Refresh the accepted implementation-source packet.
- [x] Implement Header contribution updates.
- [x] Reuse compiled Content declarations and expose affected source paths.
- [x] Implement changed relation and graph/public-row deltas.
- [x] Integrate and review the four lanes.
- [x] Run parity, failure-boundary and end-to-end checks.
- [x] Release and measure real-project latency.
- [x] Record the results before selecting further experiments.

First-cycle evidence: 252 tests passed in 35 selected modules, with one opt-in live-canary skip. All seven Docker Workbench cases and launcher integration passed. The local release failed at `prepare_candidate_image` during dependency downloads; no replacement runtime was deployed. An isolated CPU profile of roughly 5,000 source Atoms measured 0.66–0.75 seconds per edited Atom, including database application but excluding watcher/request latency. This is not a live-watcher result.

Release follow-up: [dependency-cache report](CA-P-2710-EPIC--make-workbench-queries-paged-and-frontend-modular/release-dependency-cache-20261107.md).

- [x] Fix and verify Docker dependency caching within the authorized runtime scope.

Latest cycle: runtime 0.4.4.31 is deployed. All 284 tests in 40 selected modules passed, with one opt-in canary skipped; seven Docker cases and launcher integration passed. The real-project create/edit/delete matrix improved from 3.05–3.44 seconds to 0.20–0.27 seconds. Details: [performance results](CA-P-2710-EPIC--make-workbench-queries-paged-and-frontend-modular/performance-results-20261107.md).

Release cleanup retained one image without Project ownership evidence; obsolete proven Project resources were removed. The receipt reports completed_with_cleanup_pending. Native UI acceptance C705 and the optional experiments below remain open.

## Performance regression and RAM diagnostics

- [x] Create, review and adopt the latency, throughput and rebuild Evaluation criteria.
- [x] Reuse the verified Backend Policy prompt and gather accepted sources.
- [x] Add an enforceable latency check to the existing watcher tests.
- [x] Implement and review the randomized bulk-mutation and rebuild tests.
- [x] Run the controlled Docker tests and record the regression limits and measured baseline.
- [x] Measure current RAM ownership and review the compact source-cache change.
- [x] Implement and verify the reviewed RAM change.
- [x] Create the profiler RMED.
- [x] Review and fix the profiler RMED.
- [x] Implement the accepted profiler RMED.
- [x] Test the profiler and record its results separately from acceptance timings.
- [x] Review the integrated changes and record completion.

The retained real-project test Atoms remain outside these source/code edits. Specification belongs in RMED; this section tracks execution.

## Performance experiments

Proposal: [CA-A-1329@1-draft](../CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/02_analysis/draft/CA-A-1329@1-draft-WORKBENCH_BACKEND-SPECIFICATION_PROPOSAL--compare-workbench-performance-options.md).

- [x] Benchmark bulk edits, deletes and Scope Unit move/rename operations for latency and throughput.
- [ ] Evaluate bulk SQL mutations (E01).
- [ ] Evaluate event batching (E02).
- [ ] Evaluate a shorter database critical section (E03).
- [ ] Evaluate concurrent connections and, where useful, disjoint writers (E04).
- [ ] Benchmark signed +1/-1 state against bulk delete/insert (E05).
- [ ] Compare latest-version state with deletion markers (E06).
- [ ] Measure optional index/constraint cost (E07).
- [ ] Evaluate faster libraries where profiles justify them (E08).
- [ ] Evaluate a native hot function only if it remains necessary (E09).
- [ ] Evaluate retained-log CPU work at realistic sizes (E10).
- [ ] Evaluate lighter durability for disposable derived state (E11).
- [ ] Compare alternative watcher libraries (E12).
- [ ] Benchmark parallel Python preparation, including free-threaded CPython (E13).
- [ ] Revisit physical partitioning only when a larger workload justifies it.
- [ ] Review measurements and adopt RMED for selected changes before implementation.

The experiment list is proposed work, not completion or adoption. The +1/-1 option is included; it does not replace the current transaction model in this cycle.

## Scoped lanes

| Scope Unit | Owner responsibility |
| --- | --- |
| WORKBENCH | Shared capability RMED and integrated acceptance. |
| WORKBENCH_BACKEND | Backend RMED, database, watcher, result pages and lifecycle. |
| WORKBENCH_FRONTEND | Frontend RMED, interface, result grid and browser checks. |
| CODEX_EXTENSION | Native integration and unified Workspace/View delivery sources. |

Each subagent works within one Scope Unit. The main agent owns adoption, transport integration, shared-state changes, Git and release. Ready independent lanes may run in parallel. Drafts, tests and deployed runtime are distinct outcomes.

## Other open tasks

- [x] Complete source acceptance for the confirmed Workbench audit findings.
- [ ] Review final Epic acceptance before closing it.

## Deferred

Standalone chat is disabled. Its remaining implementation, lifecycle repairs, tests and deployment stay deferred by the Operator and do not block the embedded Workbench.

CA-A-1322 remains a Draft. Its general PROGRAMMATIC Policy proposals require separate adoption outside this Workbench release. Its concrete Workbench failure and trace items are tracked above; the projection-only refresh optimization remains nonblocking and deferred.

## Current status

Active. Local release 0.4.4.29 completed. All 34 selected modules passed: 233 tests, with the live mutation canary initially skipped because it is opt-in. All seven Docker cases and launcher integration passed. E794 then passed explicitly against the live project, including cleanup. C704 is Resolved.

Accepted Workbench RMED is promoted. Backend and browser implementation is released, but native UI delivery remains incomplete: the Operator sees no interface after `workspace_open`. The live descriptor and current UI artifact are correct; C705 tracks the unresolved host presentation issue. The Epic stays Active until that acceptance passes.

The five remaining Workbench RMED Drafts belong to disabled standalone chat. General PROGRAMMATIC Policy proposals and native MODEL/Header source cutover remain outside this release. The full repository suite is not claimed green.

## Source and verification index

- General Policy proposal: CA-A-1322.
- MCP/discovery proposal: CA-A-1323.
- Source packets and adoption records: `.caprmedio_tmp/workbench/watcher-change-log/`, `sync-status/`, `grid-workbench/`, `result-display/`, `grid-backend/`, `unified-views/` and `result-retention/`.
- Per-scope Policy prompts and implementation source indices: `.caprmedio_tmp/workbench/scoped-implementation/`.
- Earlier grid-cycle release receipt: `.caprmedio_runtime/simple_local_release/reports/workbench-20261106-grid-lifecycle.md`.
- Latest input review: `input-coverage-review-20261106.md` in this Epic folder. Exact input index, scoped reviews and read-only live evidence: `.caprmedio_tmp/workbench/input-audit-20261106/`.
- Adopted RMED packet: `.caprmedio_tmp/workbench/header-sql-column-names/drafts.json`. Source handoff status: `.caprmedio_caprmedio/02_analysis/draft/header-groups-20261106/workbench-readiness.md`.
- Live native MCP proof: `.caprmedio_tmp/workbench/grid-live-proof.json`. Browser proof: `.caprmedio_tmp/workbench/grid-live-browser.json`.

The backend baseline passed 77 host tests in 12 modules, seven real Docker cases and launcher integration. The final frontend-only correction passed TypeScript, build, 13 state tests and 15 real-browser flows. Backend and dependency inputs were verified unchanged before reusing that evidence and the dependency layers. The existing Codex package is a session hook and skill that opens a browser panel. The integrated UI is now implemented and tested with a disposable host; installation and actual Codex-host acceptance remain open.

## Earlier grid-cycle verification

- [x] Review, fix and adopt the five Method and five Evaluation prevention amendments.
- [x] Implement and review the adopted M492@2/E783@2 grid lifecycle correction.
- [x] Verify cached Adaptive results, resize and View rebuild while capturing uncaught browser errors.
- [x] Verify the deployed 0.4.4.25 MCP and browser, including Adaptive paging without rerunning SQL.

The startup guard prevents provisional Workspace state from replacing early user input. Grid updates wait for Tabulator's public tableBuilt event and deferred callbacks target only the current live instance. No extra update queue was added: the selected local-array data path updates synchronously.

The 0.4.4.24 standard run passed its tests and completed Docker's build, then stopped during verification. That failed receipt remains intact. The completed image was independently verified against its reconstructed package and Current code before an actual completion invocation installed it. Version 0.4.4.25 then replaced only the frontend and version inputs on those verified dependency layers. Receipts record which evidence was reused rather than claiming repeated tests.

Native in-container rename/move events and host-side indexing are tested. Docker Desktop can forward host renames as remove/create events; the log keeps those observed events without guessing a move.

The earlier grid-cycle image is sha256:c7d3c9cd43845007177625bc833056ae7df700d8c3edeea345e00959dac9cc63, built from source commit 29c172bb1f6a9330487828140064ad8fc77c14c8. Its package fingerprint is verified. Proven obsolete Project images were removed; unrelated resources were retained.

Automatic property-column discovery and schema generation were not implemented in that earlier cycle. They now exist in the latest working tree; their RMED reconciliation, release and live acceptance remain in the current cycle.

## Codex plugin cycle

- [x] Verify a supported Codex custom-UI integration with a minimal rendering proof.
- [x] Create, review and adopt the corresponding RMED.
- [x] Reuse the applicable Policy prompt and gather the accepted implementation sources.
- [ ] Implement and test the plugin.
- [ ] Install and verify the integrated UI with the current chat Workspace and Views.
- [x] Correct and verify the default standalone URL.

An ordinary page opened in the Codex browser is insufficient for the requested plugin. Current ID formats stay unchanged. The standalone Workspace remains browser-owned; removing its default URL parameter must preserve existing state and explicit chat-bound links.

## Native UI compatibility progress

- [x] Implement and test the read-only compatibility probe through the existing MCP.
- [x] Register and install the local plugin package.
- [x] Correct and verify the standalone URL in source and isolated browser tests.
- [x] Release the tested changes and verify the running MCP.
- [x] Observe native inline rendering and the host tool bridge before implementing the full native UI.

Plugin package 0.1.1 is installed through the local marketplace. This does not establish native UI activation. After Codex reload, CAPRMEDIO tools are exposed and the inline native probe passes. Computer-use access to Codex was refused.

Checks passed: seven native MCP/HTTP cases, two shared-project MCP cases, one component browser bridge case, four plugin package cases, 16 Workbench browser flows, 13 frontend state cases, build, TypeScript, and focused Python lint/type checks. Synthetic component tests do not count as native Codex rendering.

## Verified local release 0.4.4.26

The project MCP is healthy on the existing port. Both read-only probe tools and the exact UI resource were exercised through the deployed MCP; discovery contains 45 tools. The standalone page was checked in a fresh real browser: its URL stays clean and the same local Workspace identity survives reload, without SQL execution or uncaught errors.

The local plugin is installed and enabled at version 0.1.1. The complete native Workbench interface is still unfinished. The Operator verified the native inline component after reloading Codex. Do not count the server verification or synthetic host browser test as native rendering.

Source commit: `539f0f555a77dac6c2ce1c9de8d7eb9b0953f93e`. Live proof: `.caprmedio_tmp/workbench/codex-plugin-panel/live-proof.json`. Standalone proof: `.caprmedio_tmp/workbench/clean-standalone-url/live-proof.json`.

## Native inline proof and presentation check

The Operator screenshot shows the actual in-session component with the initial MCP result and “Tool bridge passed”. Inline rendering and the UI-to-MCP bridge are verified. It is not on the right panel; that presentation is not verified. The full Workbench interface remains unfinished.

- [x] Record the native inline result.
- [x] Create the presentation-check RMED Drafts.
- [x] Review, fix and adopt those Drafts.
- [x] Reuse the scoped Policy prompt and gather implementation sources.
- [x] Implement and test the accepted source changes.
- [ ] Verify the actual host presentation before counting the right-panel target complete.

## Presentation probe release 0.4.4.27

D681@6 and E684@4 are adopted. The presentation probe passed independent review, two focused browser tests covering four display outcomes and host-context updates, the focused MCP test, Ruff and mypy. The local release serves the exact v2 resource and both read-only tools; 45 tools remain advertised. Unchanged runtime and frontend tests were reused.

The agent called the probe after deployment. The Operator screenshot still shows the first UI without Presentation text or Expand. The new UI has not been observed in Codex; stale launch metadata or a retained earlier card is the current hypothesis. The documented app-server MCP refresh API exists, but the CLI cannot reach a running control daemon here. A host-side connection refresh is still needed. Right-panel placement and the full Workbench interface remain unfinished.

Source commit: `704877a8a35b3dbad5d90d5b90d3642ab7849a72`. Verification: `.caprmedio_tmp/workbench/codex-presentation/live-proof.json`.

## Native presentation proof and watcher performance

The Operator screenshot confirms the native MCP App tool bridge and fullscreen presentation. The full Workbench interface is still unfinished.

- [x] Add mutation-to-DuckDB visibility latency metrics to the existing watcher Docker E2E test.
- [x] Measure create, edit, rename, move and remove visibility through the running Docker watcher on this repository, then remove the temporary Draft fixtures.
- [x] Review the measurements and record the test evidence. No new speed threshold or runtime optimization is part of this task.

## Watcher metrics verification

E780@2 is implemented in the existing Docker E2E. All nine measured cases passed; fixture visibility was 240–328 ms. The live repository took about a minute per individual change. Two Drafts were also tested together; create/edit/remove completed and all temporary source rows were removed. Independent review passed.

Open findings: slow full-index refresh and a child-file event missed under a newly host-created directory. No production fix, full-suite rerun or local release was performed. Evidence and exact timings: `watcher-latency-review.md` in this Epic folder.

## Incremental source refresh

Operator correction: an ordinary source file change must insert/update/remove its row and affected relations, rather than rebuild and reinsert every Atom. Preserve the full rebuild for startup, explicit full reread and actual structural or Relation registry/schema changes. Keep existing source error handling, identity checks and stable query results.

- [x] Update and review the scoped Method and Evaluation sources.
- [x] Reuse the scoped Policy prompt and implement incremental backend refresh.
- [x] Expand the Docker E2E to approximately 5,000 Atom sources; retain per-operation latency metrics and add the new-directory child case.
- [ ] Review and run behavior checks, then verify the live repository with the tested code.

Backend implementation and parent Workbench E2E work have separate owners; each worker edits one Scope Unit. Root owns source adoption, integration and release.

## Incremental implementation checkpoint

M465@16, E677@11, E780@3 and D675@13 are adopted after review. Normal source changes retain unchanged parses and apply row/edge deltas; no explicit application rollback was introduced. Successful writes and total/capture/materialization/write timings are INFO stdout, without a new DEBUG setting. The MCP stdio transport preserves protocol stdout by routing diagnostics to stderr.

Independent backend review passed. Native graph parity, first/last relation use and unchanged-row identity checks passed. Focused backend checks passed; the realistic Docker workload and live deployment remain pending.

## Latest acceptance

C704 is Resolved in source. The unchanged 5,000-Atom watcher matrix passed twelve timed mutations, immediate INFO timings, full reread and restart in 96 seconds. Visibility was 1.34–1.40 seconds. Native name binding, Header compatibility and MCP traces pass their focused checks. Local release, live-project canary and actual Codex-host acceptance remain open. See `release-acceptance-20261107.md` in this Epic folder.

## Released acceptance

Release 0.4.4.29, source `e972fa26abbf8d75c150f610a809e5d832d492fc`, passed the scoped suite and launcher gate. The live lifecycle canary passed fourteen visibility checks and cleanup in 235 seconds. Its real-project timings are separate from the 5,000-small-Atom fixture: ordinary update/move took 3.7–3.9 seconds, while scope/schema rebuilds took roughly 18–24 seconds. Native descriptor/resource checks and installed MCP View operations pass; the actual UI remains open under C705.


## AI Agent runtime retirement

- [x] Commit and push the complete pre-removal checkout to amm/dev (`e332bcdb58`).
- [x] Record and review the runtime retirement sources (M504, E796).
- [x] Remove the retired code and update retained callers, configuration and tests.
- [x] Verify retained runtime behavior and record the result.

Controlled performance acceptance and the same-source RAM comparison are complete; see the reports below. The live container remains unchanged.


## Optional code hot reload

- [x] Record the general Policy and update MCP RMED.
- [x] Apply default-off hot reload to runtime and development launch paths.
- [x] Verify both default and explicit opt-in modes.

## Batch rename correctness

- [x] Fix the relation loss found by the offline 500-Atom rename preflight.
- [x] Verify relation parity and rerun the performance gates.


## Runtime and RAM acceptance — 7 November 2026

Four controlled Docker tests passed, including all 21 measured gates. Fresh same-source containers indexed 5,485 Atoms; Docker working-set RAM fell from 680.9 MiB to 410.1 MiB (39.8%). This combines compact source caching, direct Python startup and default-off hot reload; it is not attributed to a single change. No live deployment was performed.

Evidence: [runtime acceptance](CA-P-2710-EPIC--make-workbench-queries-paged-and-frontend-modular/runtime-acceptance-20261107.md), [raw performance metrics](CA-P-2710-EPIC--make-workbench-queries-paged-and-frontend-modular/performance-acceptance-20261107.json), [RAM report](CA-P-2710-EPIC--make-workbench-queries-paged-and-frontend-modular/ram-report-20261107.md).

- [x] Investigate deeper retained memory and query-result ownership.
- [x] Benchmark aggregate-only Header schema bookkeeping against current behavior.
- [x] Benchmark UTF-8 source-body caching for memory and edit/rebuild speed.
- [x] Supersede the narrower Atom-catalog proposal with the adopted code/configuration registration work.
- [ ] Route the unchanged migration/Journal fixture failures to their owning work; preserve current validation.

The Header and UTF-8 candidates and code-owned MCP registration were subsequently adopted and completed below. Other optional experiments remain deferred. The Epic remains Active; native-host UI acceptance, live release/canary and other explicitly deferred work are still open.


## Code-owned MCP registration and further RAM work

- [x] Update, review and adopt the MCP registration/build RMED.
- [x] Reuse the scoped PROGRAMMATIC Policy prompt.
- [x] Implement and review the accepted MCP changes.
- [x] Verify build/local-release generation and registration without source Atom discovery.
- [x] Update and review the Backend RAM sources (M465@23, E677@20).
- [x] Implement and review the accepted Header and UTF-8 cache changes.
- [x] Run unprofiled correctness, speed and same-source RAM comparisons.
- [x] Record measured results and remaining limitations.

This extends the current runtime work. Workflow definitions and Atom migrations remain outside scope. Controlled builds and tests do not establish a live deployment.


## Shared backend API and follow-up acceptance

- [x] Record and review the shared-backend architecture in RMED (M506@2).
- [x] Review MCP and web call paths for duplicated operation logic, schemas and validation.
- [x] Refactor identified duplication behind the shared backend API, preserving public behavior.
- [x] Add or reuse MCP/web parity tests and record the result.
- [x] Run the first unprofiled Header-only and UTF-8 cache comparison.
- [x] Remove the duplicate full-build public-row conversion and remeasure decoding cost.
- [x] Run the final Docker latency, throughput and rebuild gates.
- [x] Record the final unprofiled RAM comparison and review the integrated changes.

The current MCP library is retained. Task checkmarks record completed work only; design and expected behavior remain in the applicable RMED. Native-host UI acceptance and a live release remain separate open tasks.


## Code/configuration and cache acceptance

The latest tracked runtime tasks are complete in source and controlled tests. No MCP library change was made. Four Docker tests and all 21 performance gates passed; shared MCP/web requests reuse the existing backend without the shared HTTP protocol detour. Fresh profiler-off containers reading the same 5,489 Atoms measured 653.5→297.9 MiB Docker working-set RAM; this cumulative comparison includes earlier runtime optimizations. The separate Backend comparison measured 33.2 MiB less RSS from the accepted cache/rebuild work.

Evidence and limits: [runtime optimization report](CA-P-2710-EPIC--make-workbench-queries-paged-and-frontend-modular/runtime-optimization-20261107.md). The Epic stays Active for its remaining native-host UI, release/canary and explicitly deferred work. No live deployment or migration/Workflow repair is implied.


## Runtime release follow-up

- [ ] Run the scoped release gate and deploy the accepted runtime changes.
- [ ] Verify code-owned tool registration, discovery and shared MCP/web behavior in the installed runtime.
- [ ] Run the real-project lifecycle canary and record visibility, rebuild and cleanup results.
- [x] Recheck the native Codex UI acceptance boundary and record the remaining action.

The Operator deferred actual native Codex UI acceptance on 7 November 2026. C705 remains unresolved and explicitly deferred; no browser substitute or full native-host acceptance is claimed.
- [ ] Reconcile the current Epic status with the verified release evidence.

The baseline is commit `8a74633801`. Root owns release, live mutations and Git. Independent read-only lanes prepare parent Workbench canary acceptance and CODEX_EXTENSION UI acceptance; each lane has one Scope Unit. Performance experiments stay deferred unless a measured regression requires work.


## Native UI deferral — 7 November 2026

Actual Codex Workbench rendering and C705 acceptance are deferred by the Operator. The runtime release and live-project canary continue independently. Earlier open native-presentation tasks remain historical requirements, now held rather than a release blocker.
