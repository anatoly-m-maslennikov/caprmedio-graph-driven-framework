# DuckDB query Projection: current-code review

## Result

The 26 RMEDO Drafts and `CA-A-1316` describe new functionality. The current repository has no DuckDB dependency, database schema, synchronizer, native-SQL connector, `expand` helper, public Run/Check tool, or SQL page. It does have useful building blocks: governed-source traversal with stable reads, strict YAML parsing, a byte-preserving heading scanner, a per-Project gateway and a Docker image. Those are not an implementation of the proposal.

Two reuse boundaries need an explicit design decision before code is added:

1. A DuckDB owner cannot live inside the reloadable MCP implementation generation. The existing reload sequence starts the candidate generation before it closes the old one, so that placement permits two owners.

2. `connector_atom_read` is deliberately fail-closed for its current public Atom Read/Query contract. It aborts the entire inventory on one malformed Atom or changing read. That conflicts with the proposed synchronizer for the certain invalid-carrier case, which must exclude the invalid carrier and continue indexing unrelated valid carriers. The treatment of a transient unreadable source remains a policy decision outside this report.

No deployed/runtime behaviour is claimed: this review traced source and tests only, and did not run tests or start Docker.

## Evidence

The matrix and the numbered findings below link every conclusion to the Draft
contract and the current code path that would be reused or conflicts with it.

## Capability matrix

| Capability | Current evidence | Assessment | Smallest safe use/change |
| --- | --- | --- | --- |
| Docker dependency and derived state | [`pyproject.toml:13-17,27-33`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/pyproject.toml:13) has no DuckDB group; Docker syncs only the four existing groups at [`docker/Dockerfile:18-21`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKFLOW_ORCHESTRATOR/docker/Dockerfile:18). | **Missing — implementation gap.** | Add one pinned DuckDB dependency group and include it in the existing image build; put the derived file in Project runtime state, not the scheduler database. |
| Governed source reader | `connector_atom_read.py:50-122` filters a bound Project/control inventory, excludes `_projection` and installed roots, preserves raw bytes and fingerprints; `read_io.py:73-90,98-150` gives no-follow stable reads and inventory/currentness. | **Reusable, but only as leaf mechanics.** | Reuse `ReadContext`, `parse_carrier`, raw-byte fingerprinting, and admitted inventory selection. Do not call `_sources()` as the synchronizer. |
| Nested Header | `parsing.py:64-84` uses `UniqueSafeLoader`; duplicate YAML keys become `CarrierError`. `connector_atom_read.py:112-114` retains parsed metadata and raw bytes. | **Partial.** | Persist parsed mapping plus original frontmatter; add a Projection representation without coercing null/empty/list/scalar values. |
| Nested Markdown tree | `connector_section_parse.py:45-92` detects ATX headings outside fences and records byte spans and immediate nesting; tests cover fence/span preservation (`tests/test_connector_section_parse.py:22-36`). | **Partial.** | Reuse only heading/fence/span detection. Add declared-property admission, normalized sibling-collision checks, path segments, direct-body versus full-section extraction, and Claim/Prose Claim handling. |
| Sync / one DB owner / hot reload | `Gateway` is per Project ([`hot_reload.py:331-347`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/hot_reload.py:331)); the pool retains one initialized gateway per loaded Project and closes evicted entries ([`shared_project_pool.py:114-148`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/shared_project_pool.py:114)). | **Partial, with a handoff conflict.** | Keep a Project-local owner above reloadable child generations, or make all old-owner close/drain complete before a successor may open DuckDB. Serialize RW reconciliation and RO SQL there. |
| Native SQL and relation expansion | Existing `query_actions.py:16-55` dispatches only legacy artifact/journal routes and closed request shapes. `connector_atom_parse.py:48-92` is a Subject-filter parser, not SQL. | **Missing — implementation gap.** | Add DuckDB-native Run/Check and one indexed-edge `expand` helper; do not adapt the Subject filter or CFEL extraction as a SQL evaluator. |
| MCP Run/Check | `implementation_server.py:73-96` registers the orchestrator, selected routes, and catalog descriptors; no DuckDB tool is registered. | **Missing — implementation gap.** | Register one admitted SQL tool backed by the shared owner. Run and Check must call the same connector. |
| Web and errors | `http_server.py:112-141` exposes health only; `create_app()` installs `/health` alongside MCP at `http_server.py:144-170`. | **Missing — implementation gap.** | Add one local page/endpoint under the existing app, using the MCP connector result contract; preserve stderr for source diagnostics and return SQL errors to callers. |
| Scheduler separation | Scheduler SQLite is explicitly created at `backend.py:33-37`. | **Reusable boundary.** | Use a distinct runtime path/database; never attach the Projection to `dbos.sqlite`. |

## Actionable findings

### 1. Must fix: reload starts a successor before the predecessor is closed

**Draft requirement.** [`CA-M-463@1-draft:34-42`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/05_method/draft/duckdb-query-projection/CA-M-463@1-draft-FRAMEWORK_ENGINE-ENG_DECISION--keep-duckdb-projection-ownership-in-the-existing-server.md:34) and [`CA-E-674@1-draft:36-38`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/06_evaluation/draft/duckdb-query-projection/CA-E-674@1-draft-FRAMEWORK_ENGINE-EVAL_CASE--enforce-native-read-only-and-exclusive-owner-handoff.md:36) require exactly one owner and require the old owner to close before a replacement opens. [`CA-O-240@1-draft:40`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/09_operations/draft/duckdb-query-projection/CA-O-240@1-draft-FRAMEWORK_ENGINE-ACTION--execute-one-read-only-duckdb-query.md:40) and [`CA-O-241@1-draft:40`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/09_operations/draft/duckdb-query-projection/CA-O-241@1-draft-FRAMEWORK_ENGINE-ACTION--reconcile-the-duckdb-query-projection.md:40) repeat the no-overlap rule. The governing proposal says the same at [`CA-A-1316:47-57`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis/CA-A-1316-FRAMEWORK_ENGINE-SPECIFICATION_PROPOSAL--query-atoms-through-a-synchronized-duckdb-projection.md:47).

**Code evidence.** [`Gateway.publish()`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/hot_reload.py:472) calls `await self._prepare(fingerprint)` before it assigns the candidate as active. [`_prepare()`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/hot_reload.py:383) starts an implementation child; the old child is only closed later, and only immediately when `old.in_flight == 0` ([`hot_reload.py:490-495`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/hot_reload.py:490)). A DuckDB owner constructed in that implementation child can therefore coexist with the prior owner during candidate startup.

**Concrete failure.** Reload while a query is in flight. The new child opens a RW or RO DuckDB connection while the old child still owns a connection. This breaks the Draft's exclusive mode/owner invariant and can cause lock failures or two independent writers.

**Smallest change.** Put the database owner in the stable `Gateway`/shared Project gateway layer, not the reloadable `implementation_server` process, and pass only request work into it. If that is impossible, make reload drain and close the old owner before `_prepare()` can start a successor; retain an explicit unavailable/retry result while it drains. Add the `CA-E-674` active-query + pending-sync + reload test before exposing SQL.

### 2. Must fix before reusing the reader: one invalid YAML carrier aborts all sources

**Draft requirement.** [`CA-R-2725@1-draft:32-40`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/04_requirement/draft/duckdb-query-projection/CA-R-2725@1-draft-FRAMEWORK_ENGINE-RULE--expose-only-valid-synchronized-source-state-through-query-projection.md:32), [`CA-M-464@1-draft:36-40`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/05_method/draft/duckdb-query-projection/CA-M-464@1-draft-FRAMEWORK_ENGINE-ENG_DECISION--preserve-governed-atom-data-and-reuse-native-sql.md:36), and [`CA-E-677@1-draft:43-63`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/06_evaluation/draft/duckdb-query-projection/CA-E-677@1-draft-FRAMEWORK_ENGINE-EVAL_CASE--reconcile-source-lifecycle-and-invalid-repair-state.md:43) require an invalid carrier to lose only its own rows, write a path/location diagnostic to stderr, and leave unrelated valid carriers queryable. Stable-read races must be deferred rather than published mixed ([`CA-M-465@1-draft:34-42`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/05_method/draft/duckdb-query-projection/CA-M-465@1-draft-FRAMEWORK_ENGINE-ENG_DECISION--reconcile-duckdb-derived-state-from-stable-governed-inventory.md:34)).

**Code evidence.** [`_sources()`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/connector_atom_read.py:79) catches a `CarrierError` or read error and raises `AtomReadError` for any selected Atom-looking source, then rejects any competing original identity for the whole view ([`connector_atom_read.py:106-116`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/connector_atom_read.py:106)). Its existing test deliberately expects a malformed source to make `query_atoms()` fail ([`test_connector_atom_read.py:177-185`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/tests/test_connector_atom_read.py:177)). [`ReadContext.read()`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/VALIDATE_ATOMS/validate_atoms_workers/read_io.py:73) correctly detects an in-read change, but `_sources()` turns that signal into the same whole-inventory refusal.

**Concrete failure.** A valid carrier A and a newly edited carrier B with a YAML duplicate key are present. The proposed Projection must remove B's old rows and continue serving A. Reusing `_sources()` makes reconciliation fail before A can be indexed or queried. A transient unreadable/read-race state is a separate policy case: the Draft requires a deferred stable capture, but this report does not decide whether a prior row is removed before that capture succeeds.

**Smallest change.** Keep `ReadContext` and `parse_carrier` but add a synchronizer-specific collector that returns per-path outcomes: valid capture, invalid/excluded (with sanitized stderr diagnostic), and changed/deferred. Apply each source's Atom/property/edge deletion or replacement atomically. Resolve the transient-unreadable retained-row policy with report 01; do not weaken the existing public Atom Read/Query contract, whose all-or-nothing behaviour is tested and has different semantics.

### 3. Implementation gap: the repository does not declare or build DuckDB's enforcement boundary

**Draft requirement.** [`CA-M-462@1-draft:34-43`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/05_method/draft/duckdb-query-projection/CA-M-462@1-draft-FRAMEWORK_ENGINE-ENG_DECISION--constrain-public-duckdb-queries-to-native-read-only-access.md:34), [`CA-R-2728@1-draft:32-38`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/04_requirement/draft/duckdb-query-projection/CA-R-2728@1-draft-FRAMEWORK_ENGINE-RULE--provide-native-sql-query-capability-over-query-projection.md:32), and [`CA-D-675@1-draft:36-40`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/07_delivery/draft/duckdb-query-projection/CA-D-675@1-draft-FRAMEWORK_ENGINE-ENG_DECISION--place-duckdb-projection-in-rebuildable-runtime-state.md:36) require native DuckDB read-only connections, external-access configuration/locking, and a Project-local rebuildable database.

**Code evidence.** The declared default runtime has no required dependency ([`pyproject.toml:13-17`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/pyproject.toml:13)); the only dependency groups are shown at [`pyproject.toml:27-33`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/pyproject.toml:27), and DuckDB is absent from both `pyproject.toml` and `uv.lock`. The Docker image performs a locked install of the listed groups only ([`docker/Dockerfile:18-21`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKFLOW_ORCHESTRATOR/docker/Dockerfile:18)).

**Impact.** The repository declarations and image build provide no DuckDB engine or native read-only/configuration boundary. A keyword filter over existing request/filter code would violate the stated security boundary, including data-modifying CTEs and external access. The installed or deployed image was not inspected.

**Smallest change.** Add a pinned DuckDB runtime group and include it in the existing `uv sync --locked` build. Keep public enforcement in DuckDB's read-only connection/configuration mode; do not create a CFEL or keyword-based parser.

### 4. Implementation gap: neither a Projection schema nor a shared public surface exists

**Draft requirement.** [`CA-R-2726@1-draft:32-41`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/04_requirement/draft/duckdb-query-projection/CA-R-2726@1-draft-FRAMEWORK_ENGINE-RULE--preserve-atom-header-and-markdown-content-faithfully-in-query-projection.md:32) and [`CA-D-672@1-draft:34-48`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/07_delivery/draft/duckdb-query-projection/CA-D-672@1-draft-FRAMEWORK_ENGINE-ENG_DECISION--deliver-duckdb-atom-content-and-relation-records.md:34) require atoms, nested content properties, and typed relation edges. [`CA-R-2729@1-draft:32-39`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/04_requirement/draft/duckdb-query-projection/CA-R-2729@1-draft-FRAMEWORK_ENGINE-RULE--return-complete-consistent-results-for-query-run-and-check.md:32), [`CA-D-673@1-draft:36-42`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/07_delivery/draft/duckdb-query-projection/CA-D-673@1-draft-FRAMEWORK_ENGINE-ENG_DECISION--deliver-shared-query-run-and-check-results.md:36), and [`CA-R-2727@1-draft:32-38`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/.caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/04_requirement/draft/duckdb-query-projection/CA-R-2727@1-draft-FRAMEWORK_ENGINE-RULE--provide-a-simple-web-query-interface-over-the-shared-query-capability.md:32) require shared Run/Check and a simple local page.

**Code evidence.** [`connector_atom_read.py:128-174`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/connector_atom_read.py:128) exposes only read/query of a fixed Atom result-field set ([`connector_atom_parse.py:18-20`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/connector_atom_parse.py:18)), not nested properties, relations, SQL, counts, or column types. Current workflow query adapters only import artifact and journal tools ([`query_actions.py:37-45`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKFLOW_ORCHESTRATOR/query_actions.py:37)), and HTTP serves health responses/pages only ([`http_server.py:112-141`](/Users/am/Documents/My_Repos/caprmedio-graph-driven-framework/LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_MCP/http_server.py:112)).

**Impact.** There is no dormant DuckDB code to expose. Reusing the legacy workflow adapter would also retain its fixed filter/snapshot vocabulary instead of accepting exact SQL.

**Smallest change.** Implement one Project-owner API with two operations (`Run`, `Check`), then make MCP registration and one local page call that same API. Store ordinary rows, names/types, and exact counts from one execution; leave TABLE/DOC/TREE rendering and CFEL evaluation out.

## Reuse notes and implementation order

1. Establish dependency/image and a stable per-Project owner outside reload generations. Keep its file separate from `backend.py`'s `dbos.sqlite`.

2. Build the per-carrier collector on `ReadContext`/`parse_carrier`; retain raw source, frontmatter, parsed Header, Markdown body, and fingerprints. Add the Markdown-property index beside—not inside—the edit-oriented `connector_section_parse` API.

3. Reconcile the complete governed inventory at owner startup and periodically. Serialize the transaction and public RO execution; test move, confirmed deletion, invalid edit, repair, read race, and restart.

4. Add native SQL plus indexed-edge `expand`, then one MCP Run/Check route and a thin local page. Do not reuse the legacy `query_actions` request parser.

## Verification and uncertainty

Read-only evidence inspected: all 27 manifest-pinned sources (26 RMEDO Drafts plus `CA-A-1316`), the named reader/parser/alias/stable-I/O files and tests, MCP gateway/pool/hot-reload/HTTP files, workflow query/scheduler files, and Docker/dependency declarations. No tests, fixtures, Docker build/start/restart, MCP call, or source mutation was performed.

Not checked: live Docker image contents, DuckDB behaviour (not declared in the lockfile), runtime Project selection/configuration, and external deployment. The source evidence establishes available code paths, not a running service.

## Changed files

None in the reviewed implementation, Drafts, Current carriers, tests, fixtures,
Docker, or Git/index. This report is the sole requested review artifact.

## Next action

Resolve finding 1's owner location first. Then implement the smallest dependency + stable-owner + per-source reconciliation slice and its handoff/invalid-source tests before any MCP or web work.

