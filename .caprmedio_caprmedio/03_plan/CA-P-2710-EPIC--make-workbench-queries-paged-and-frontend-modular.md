---
atom_id: CA-P-2710
label: Epic
status: Done
tier: 3
version: 5
updated_at: 2026-11-04 19:31:25 +0400
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  IS_CONTAINED_BY:
    scope_unit: caprmedio
role: Plan
form: Plan
carrier_destination:
  file:
    name: CA-P-2710-EPIC--make-workbench-queries-paged-and-frontend-modular.md
    path: .caprmedio_caprmedio/03_plan
---
## Summary

Make Workbench queries paged and the frontend modular

## Objective

Make ordinary Workbench queries usable without loading the complete result into server or browser memory. Keep implementation simple and scoped to Workbench.

## Workbench Scope Units

- WORKBENCH retains shared requirements and cross-interface contracts.
- WORKBENCH_BACKEND owns source reading, indexing, DuckDB/DuckPGQ and stable result pages.
- WORKBENCH_FRONTEND owns Svelte, TypeScript, Vite, the UX component palette and frontend state.
- Both are child Scope Units of WORKBENCH; this does not split all PROGRAMMATIC into Backend and Frontend.

## Tasks

1. Add and align RMED before implementation. Record Svelte + TypeScript + Vite and disk-backed, paged query results as engineering decisions. Record the reusable component palette as a UX requirement. Keep error-handling decisions in Methods.
2. Store the rebuildable DuckDB Projection and materialized query results under `.caprmedio_runtime/workbench`. Source files remain authoritative. Keep native DuckDB and DuckPGQ queries and the two public tables, `atoms` and `scope_units`.
3. Execute each Run once, preserve its column metadata and exact counts, and deliver bounded pages from that stable result through MCP and web. Check returns exact counts without fetching all rows into Python. Release successful parser caches after indexing; preserve invalid-source skip behavior.
4. Build the frontend with Svelte + TypeScript + Vite. Serve static build assets through the existing Python application. Move presentation, formatting, page navigation and UI state to the frontend; filtering, sorting and aggregation remain in DuckDB.
5. Create a small reusable component palette from the start and use it in the query UI. Keep HTML, CSS, JavaScript, TypeScript and Svelte files small. Splitting a source file above 300 lines is strongly recommended; above 500 lines it is mandatory. Split by responsibility, not arbitrary chunks. Svelte components should make a Python HTML builder unnecessary.
6. Serve `/caprmedio/workbench/<project_name>`, `/caprmedio/mcp` and `/caprmedio/health`. Update callers, fixtures, documentation and Docker packaging together.
7. Test native SQL and DuckPGQ, duplicate column names, page boundaries, stable pages after source refresh, invalid requests, full Markdown preservation and frontend build. Prove real-repository `SELECT * FROM atoms` returns paged results in Docker without a memory-limit kill.
8. Review RMED coverage, run focused Workbench and affected HTTP/startup checks, perform local release, and verify the new URLs and queries against the running container.

## Scope limits

Workbench only. No repair of unrelated lifecycle or model migrations, custom SQL parser, queue, scheduler, background query execution, automatic retry or automatic restart. Do not add indexes without evidence that a selective query benefits; an index does not reduce the output size of `SELECT *`.

## Definition of Done

- Current Workbench RMED matches these decisions and implementation references use its actual versions.
- Query pages preserve all selected values and report total counts explicitly; neither transport silently truncates a result.
- The frontend builds and uses its shared component palette. Source files obey the mandatory 500-line limit.
- Focused tests and real-repository Docker paging checks pass; local release and live endpoint checks are recorded separately from source completion.

## Status

Done. Workbench 0.4.4.15 is released and the Project-specific page, API, MCP, health, pagination and bounded result display are verified live.

## Verification checkpoint

- 61 focused Workbench tests passed, including native file watching, timestamp delivery, stable result pages, shared MCP/web behavior and frontend asset handling.
- 27 affected HTTP/MCP/health checks and the added native SDK page-dispatch regression passed.
- Svelte production build, TypeScript check and scoped Ruff checks passed. Nine frontend source files have at most 65 lines each.
- The declaration reader admits 46 Scope Units, including both new Workbench children.
- Three real-repository Docker tests passed in 67.102 seconds against image `sha256:8dfbacc858c29ad70c09047ee5764be2667737d07802bb13cca70be7613b29ee`. They cover native SQL/PGQ, MCP Run/Check/Page, 100-row SELECT-all pages, a disk database with read-only source mount, every built CSS/JS asset and bind-mount file watching.
- Docker reported no OOM kills. Peak container memory was 1,140,768,768 bytes under a 1,610,612,736-byte limit. This is a measured peak, not a promise of lower idle memory.
- Added the native DuckDB timezone dependency and a regression that failed before it was installed. No memory-limit increase was needed for that failure.
- Local release and live browser verification are still open. The unrelated repository-wide suite is outside this Workbench run.

## Final URL and presentation follow-up

The Operator selected `/caprmedio/workbench/caprmedio`, with `/caprmedio/mcp` and `/caprmedio/health` unchanged. Validate the URL Name against the selected Project; keep shared assets outside the Project path. Finish this routing change and bounded table/cell scrolling, verify them, and release.

Docker Desktop is now configured and verified at 32 GiB, as requested. Old unused runtime/probe images and the verified obsolete test-fixture container/image were removed. Only the current runtime image remains.

The 0.4.4.14 live API and browser returned 4,592 rows and 17 columns through 100-row pages. Run, Check, Next, Previous, visible query errors and a subsequent valid query all passed. The final follow-up must not be counted as deployed until separately released.

## Final result

- Local release `workbench-20261104-project-url` completed as 0.4.4.15. Its final gate passed nine tests with zero skips or failures, plus all launcher Docker groups. Earlier focused gates passed 61 Workbench tests, 27 HTTP checks, the SDK page-dispatch regression and 29 packaging tests.
- Live page: `http://127.0.0.1:56317/caprmedio/workbench/caprmedio`. MCP remains `/caprmedio/mcp`; health remains `/caprmedio/health`. Unqualified or mismatched Project pages return 404.
- Live web and MCP SELECT-all requests return 4,592 rows and 17 columns through bounded pages. Browser Run, Check, Next and Previous passed; query errors are visible and a subsequent valid query succeeds. The final Project-qualified page and scrolling result pane were inspected in the browser.
- Source files remain authoritative. The disk-backed database, internal results and spill live under `.caprmedio_runtime/workbench`. No custom SQL parser, extra server, queue, scheduler, retry or rollback was added.
- WORKBENCH_BACKEND and WORKBENCH_FRONTEND are declared child Scope Units; their code and specific RMED are separated. Shared Workbench contracts remain in the parent.
- Svelte + TypeScript + Vite, the component palette, >300-line recommendation and >500-line mandatory split are recorded in Current RMED. Frontend source files remain far below both thresholds.
- Docker's applied disk size is 32 GiB. Old unused images and the verified obsolete test fixture were removed; only the current runtime image remains.
- The release receipt is `.caprmedio_runtime/simple_local_release/reports/workbench-20261104-project-url.md`. Live API and browser evidence is retained under `.caprmedio_tmp/workbench`. The unrelated full repository suite was not run.
