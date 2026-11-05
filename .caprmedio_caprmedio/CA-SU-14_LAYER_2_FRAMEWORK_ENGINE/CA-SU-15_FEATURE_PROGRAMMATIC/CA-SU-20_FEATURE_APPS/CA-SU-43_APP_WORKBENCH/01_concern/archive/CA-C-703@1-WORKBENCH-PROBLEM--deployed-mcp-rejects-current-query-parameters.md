---
atom_id: CA-C-703
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
version: 1
author: Anatoly Maslennikov
role: Concern
form: Problem
tier: 3
priority: medium
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  concern_about:
  - CA-R-2728
  - CA-D-673
carrier_destination:
  file:
    name: CA-C-703@1-WORKBENCH-PROBLEM--deployed-mcp-rejects-current-query-parameters.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/01_concern/archive
updated_at: 2026-11-05 17:43:47 +0400
---

## Summary

The deployed MCP rejects current query parameters.

## Concern

The deployed MCP schema exposes only `sql`, `page_size`, and
`cursor_position` for the Workbench query operation, so it rejects
`preview: 0` and `save: false`. The current source schema includes these
options, and the SDK regression passes the exact `preview: 0` and `save: false`
request, but no deployed verification has been completed. Local source success
therefore does not establish deployed adoption.

## Resolution

This Problem remains open. The source correction and local regression evidence
are recorded, but deployment must still be verified to advertise and accept
optional `preview` and `save`, including `preview: 0` and `save: false`. Do not
mark the deployed boundary resolved until that endpoint-level check succeeds.
