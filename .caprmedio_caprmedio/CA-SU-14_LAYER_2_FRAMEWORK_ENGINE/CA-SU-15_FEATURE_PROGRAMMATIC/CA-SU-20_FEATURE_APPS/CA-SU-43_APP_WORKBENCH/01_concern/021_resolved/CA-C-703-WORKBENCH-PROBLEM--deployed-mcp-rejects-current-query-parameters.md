---
atom_id: CA-C-703
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Resolved
version: 3
author: Anatoly Maslennikov
role: Concern
form: Problem
tier: 3
priority: medium
relations:
  concern_about:
  - CA-R-2728
  - CA-D-673
carrier_destination:
  file:
    name: CA-C-703-WORKBENCH-PROBLEM--deployed-mcp-rejects-current-query-parameters.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/01_concern/021_resolved
updated_at: 2026-11-10 20:47:54 +0400
ref_id: CA-C-703
container:
  scope_unit: CA-SU-43
topics:
  main_subject: MODEL//CAPRMEDIO <+ Projection
---

## Summary

The deployed MCP rejects current query parameters.

## Concern

The running MCP used the older query schema and rejected `preview: 0` and
`save: false`, even though the current source supported them. Source tests alone
did not establish deployed adoption.

## Resolution

The tested 0.4.4.22 image is running on port 56317. After the release startup
failed in an empty Python environment, the existing Project bootstrap restored
MCP using the tested installed package and its provisioned launcher environment.

A fresh native MCP SDK client confirmed that `query_run` advertises `preview`
and `save` and accepts `preview: 0, save: false`. It returned zero rows and one
column without creating a saved query. Workspace/View create, SQL update,
metadata-only Run, five-row fetch, focus and query-log checks also passed.

The endpoint verification is recorded in
`.caprmedio_tmp/workbench/codex-extension/live-proof.json`. The automated
release-caller correction and catalog completion remain separate work; the
query-parameter deployment mismatch itself is resolved.
