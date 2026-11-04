---
atom_id: CA-D-674
current_scope_unit: WORKBENCH_FRONTEND
claim_target_scope_unit: WORKBENCH_FRONTEND
status: Archived
version: 6
author: Anatoly Maslennikov
role: Delivery
form: Eng Decision
tier: 4
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  delivery_for:
  - CA-R-2727
carrier_destination:
  file:
    name: CA-D-674@6-WORKBENCH_FRONTEND-ENG_DECISION--deliver-simple-sql-query-page.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/07_delivery/archive
updated_at: 2026-11-04 18:09:13 +0400
---

## Summary

Deliver a simple SQL query page through the shared connector

## Claim scope

The Workbench frontend and its same-listener HTTP delivery.

## Claim

### Prose Claim

Build the Workbench frontend with Svelte, TypeScript and Vite. Serve its static production assets through the existing Python application at `/caprmedio/workbench`; Node is a build dependency, not a second runtime server.

Provide a SQL editor, Run and Check controls, exact counts, query errors and ordinary result rows with Previous and Next page controls. Use shared components from a small component palette. Keep display formatting, page navigation and UI state in the frontend; the database executes SQL filtering, sorting and aggregation.

Use `/caprmedio/workbench/run`, `/caprmedio/workbench/page` and `/caprmedio/workbench/check` for the shared connector. Fetch only the requested result page. Preserve positional values and duplicate column names. Show loading and error states and accessible labels for controls. Do not add custom TABLE, DOC or TREE modes, a second query evaluator or a separate web service.

When the frontend build is missing, keep the query API and MCP available. The Workbench page returns HTTP 503 with an explicit build-required error; do not build assets or start a frontend server automatically.
