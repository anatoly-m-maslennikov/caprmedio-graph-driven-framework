---
atom_id: CA-P-2710
label: Epic
status: Archived
tier: 3
version: 1
updated_at: 2026-11-04 17:10:00 +0400
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  IS_CONTAINED_BY:
    scope_unit: caprmedio
role: Plan
form: Plan
carrier_destination:
  file:
    name: CA-P-2710@1-EPIC--make-workbench-queries-paged-and-frontend-modular.md
    path: .caprmedio_caprmedio/03_plan/archive
---
## Summary

Make Workbench queries paged and the frontend modular

## Objective

Make ordinary Workbench queries usable without loading the complete result into server or browser memory. Keep implementation simple and scoped to Workbench.

## Tasks

1. Add and align RMED before implementation. Record Svelte + TypeScript + Vite and disk-backed, paged query results as engineering decisions. Record the reusable component palette as a UX requirement. Keep error-handling decisions in Methods.
2. Store the rebuildable DuckDB Projection and materialized query results under `.caprmedio_runtime/workbench`. Source files remain authoritative. Keep native DuckDB and DuckPGQ queries and the two public tables, `atoms` and `scope_units`.
3. Execute each Run once, preserve its column metadata and exact counts, and deliver bounded pages from that stable result through MCP and web. Check returns exact counts without fetching all rows into Python. Release successful parser caches after indexing; preserve invalid-source skip behavior.
4. Build the frontend with Svelte + TypeScript + Vite. Serve static build assets through the existing Python application. Move presentation, formatting, page navigation and UI state to the frontend; filtering, sorting and aggregation remain in DuckDB.
5. Create a small reusable component palette from the start and use it in the query UI. Keep HTML, CSS, JavaScript, TypeScript and Svelte files small. Splitting a source file above 300 lines is strongly recommended; above 500 lines it is mandatory. Split by responsibility, not arbitrary chunks. Svelte components should make a Python HTML builder unnecessary.
6. Serve `/caprmedio/workbench`, `/caprmedio/mcp` and `/caprmedio/health`. Update callers, fixtures, documentation and Docker packaging together.
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

Active. Backend, adapters, frontend and Docker verification have separate owners. Integrated acceptance and local release remain pending.
