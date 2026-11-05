---
atom_id: CA-M-466
ref_id: CA-M-466
container:
  scope_unit: CA-SU-46
role: Method
form: Eng Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 4
relations:
  method_for:
  - CA-R-2727
status: Active
version: 5
updated_at: 2026-11-04 21:06:25 +0400
carrier_destination:
  file:
    name: CA-M-466-WORKBENCH_FRONTEND-ENG_DECISION--use-svelte-typescript-and-vite-for-workbench.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/05_method
current_scope_unit: WORKBENCH_FRONTEND
claim_target_scope_unit: WORKBENCH_FRONTEND
author: Anatoly Maslennikov
---

## Summary

Use Svelte, TypeScript and Vite for Workbench

## Claim scope

The Workbench frontend.

## Claim

### Prose Claim

Use Svelte components and TypeScript for the Workbench frontend, and Vite for its production build. Serve static assets through the existing Python application. Node is required for building, not for serving the running application.

Keep presentation, formatting, page navigation and UI state in the frontend. Keep SQL execution, filtering, sorting, aggregation and stable result materialization in DuckDB. The browser requests bounded pages and does not load a complete large result to reproduce database operations.

Use the connector's `columns[].has_values` metadata, computed across the complete result, to hide fully empty columns in non-empty results. For this metadata only, NULL, empty strings, empty arrays and empty objects are empty; false and zero are values, and a nested object with keys is non-empty even when a nested value is null. For a zero-row result, the connector sets `has_values: true` for every returned column so all headers remain visible. This display choice does not change SQL values, row counts or column counts, and it stays identical across pages.

Reuse a small component palette from the start. Do not add a frontend router, state framework or separate web server for this query page.

When the frontend build is missing, keep the query API and MCP available. The Workbench page returns HTTP 503 with an explicit build-required error; do not build assets or start a frontend server automatically.

Use `/caprmedio/workbench/<project_name>` for the selected Project. Read its declared Name from the existing gateway selection; do not infer it from a folder name or discover other repositories. A mismatched name returns HTTP 404. Shared-server requests retain their existing explicit Project-root selection and the URL Name must match it. Keep MCP at `/caprmedio/mcp` and health at `/caprmedio/health`.
