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
status: Archived
version: 47
updated_at: 2026-11-06 20:11:57 +0400
carrier_destination:
  file:
    name: CA-P-2710@47-EPIC--make-workbench-queries-paged-and-frontend-modular.md
    path: .caprmedio_caprmedio/03_plan/archive
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

The input review covers 223 messages from 4 November 19:58:47 to 6 November 19:58:47, Asia/Tbilisi. Later Operator decisions override earlier ones. See `input-coverage-review-20261106.md` in this Epic folder for the decision reconciliation, RMED coverage and verification limits. The earlier completed cycle does not close these tasks.

- [x] Re-read the complete 48-hour input window and review RMEDO, tasks, implementation and verification in the scoped lanes.
- [ ] Reconcile the reviewed schema and interface RMED Drafts with every affected Current source, including E677; review, fix and adopt the final packet.
- [ ] Review the remaining model-declaration and shared Header handoff issues with their source owners; record Workbench compatibility and unresolved dependencies.
- [ ] Record the default query-writing style in the applicable Method guidance and reconcile examples and the compiled prompt.
- [ ] Record the remaining confirmed Workbench failures as Problems, link their regression Evaluations, and resolve each only from verified evidence.
- [ ] Complete the outstanding direct-implementation trace review and correct confirmed missing, stale or caller-only module references.
- [ ] Gather or refresh the applicable Policy prompt and accepted RED plus non-Policy Methods for each implementation scope.
- [ ] Complete and review implementation against those sources, including the existing native Codex plugin tasks.
- [ ] Complete the realistic watcher Docker acceptance and the existing approximately-5,000-source/new-directory checks, retaining operation timings.
- [ ] Complete local release of the tested Workbench and verify its public MCP, HTTP and browser behavior against the accepted sources.
- [ ] Review and adopt the live-project canary Evaluation, then execute the full Atom and Scope Unit Declaration operation matrix against the released candidate and verify cleanup.
- [ ] Verify the actual native Workbench interface in Codex with the current chat Workspace and Views.
- [ ] Reconcile the audit coverage and record final acceptance before considering Epic closure.

Use the standard cycle: RMEDO → review/fix/adopt → scoped Policy prompt → accepted RED and non-Policy Methods → implementation → behavior-focused E2E → actual runtime verification. Each subagent owns no more than one Scope Unit; root owns integration, source adoption, Git and release. Design stays in RMED. The tasks above reference the audited work; they do not introduce new product behavior.

## Scoped lanes

| Scope Unit | Owner responsibility |
| --- | --- |
| WORKBENCH | Shared capability RMED and integrated acceptance. |
| WORKBENCH_BACKEND | Backend RMED, database, watcher, result pages and lifecycle. |
| WORKBENCH_FRONTEND | Frontend RMED, interface, result grid and browser checks. |
| CODEX_EXTENSION | Native integration and unified Workspace/View delivery sources. |

Each subagent works within one Scope Unit. The main agent owns adoption, transport integration, shared-state changes, Git and release. Ready independent lanes may run in parallel. Drafts, tests and deployed runtime are distinct outcomes.

## Other open tasks

- [ ] Review the remaining unadopted PROGRAMMATIC proposals in CA-A-1322.
- [ ] Finish the remaining confirmed Workbench audit and trace issues recorded there.
- [ ] Implement and verify the integrated Codex plugin UI; the existing browser opener does not complete it.
- [ ] Review final Epic acceptance before closing it.

## Deferred

Standalone chat is disabled. Its remaining implementation, lifecycle repairs, tests and deployment stay deferred by the Operator and do not block the embedded Workbench.

## Current status

Active. The earlier query/View/grid cycle shipped, but the latest schema/interface RMED is still Draft and its implementation is not deployed. Read-only inspection on 6 November verified the running image as version 0.4.4.27, source commit `704877a8a35b3dbad5d90d5b90d3642ab7849a72`. Its live schema still exposes short Header aliases and Content names with spaces.

The latest working tree contains generated Header/Content schema assets, incremental refresh and the later interface fixes with focused verification. This is not a current-source adoption, release, full-suite or live-canary completion claim. Realistic watcher acceptance, the live all-operation canary, the complete native Codex Workbench UI and the current cycle remain open. Standalone chat remains disabled and deferred.

## Source and verification index

- General Policy proposal: CA-A-1322.
- MCP/discovery proposal: CA-A-1323.
- Source packets and adoption records: `.caprmedio_tmp/workbench/watcher-change-log/`, `sync-status/`, `grid-workbench/`, `result-display/`, `grid-backend/`, `unified-views/` and `result-retention/`.
- Per-scope Policy prompts and implementation source indices: `.caprmedio_tmp/workbench/scoped-implementation/`.
- Earlier grid-cycle release receipt: `.caprmedio_runtime/simple_local_release/reports/workbench-20261106-grid-lifecycle.md`.
- Latest input review: `input-coverage-review-20261106.md` in this Epic folder. Exact input index, scoped reviews and read-only live evidence: `.caprmedio_tmp/workbench/input-audit-20261106/`.
- Pending RMED packet: `.caprmedio_tmp/workbench/header-sql-column-names/drafts.json`. Source handoff status: `.caprmedio_caprmedio/02_analysis/draft/header-groups-20261106/workbench-readiness.md`.
- Live native MCP proof: `.caprmedio_tmp/workbench/grid-live-proof.json`. Browser proof: `.caprmedio_tmp/workbench/grid-live-browser.json`.

The backend baseline passed 77 host tests in 12 modules, seven real Docker cases and launcher integration. The final frontend-only correction passed TypeScript, build, 13 state tests and 15 real-browser flows. Backend and dependency inputs were verified unchanged before reusing that evidence and the dependency layers. The existing Codex package is a session hook and skill that opens a browser panel. The integrated plugin UI requested by the Operator is not implemented; installation alone does not complete it.

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
- [ ] Expand the Docker E2E to approximately 5,000 Atom sources; retain per-operation latency metrics and add the new-directory child case.
- [ ] Review and run behavior checks, then verify the live repository with the tested code.

Backend implementation and parent Workbench E2E work have separate owners; each worker edits one Scope Unit. Root owns source adoption, integration and release.

## Incremental implementation checkpoint

M465@16, E677@11, E780@3 and D675@13 are adopted after review. Normal source changes retain unchanged parses and apply row/edge deltas; no explicit application rollback was introduced. Successful writes and total/capture/materialization/write timings are INFO stdout, without a new DEBUG setting. The MCP stdio transport preserves protocol stdout by routing diagnostics to stderr.

Independent backend review passed. Native graph parity, first/last relation use and unchanged-row identity checks passed. Focused backend checks passed; the realistic Docker workload and live deployment remain pending.
