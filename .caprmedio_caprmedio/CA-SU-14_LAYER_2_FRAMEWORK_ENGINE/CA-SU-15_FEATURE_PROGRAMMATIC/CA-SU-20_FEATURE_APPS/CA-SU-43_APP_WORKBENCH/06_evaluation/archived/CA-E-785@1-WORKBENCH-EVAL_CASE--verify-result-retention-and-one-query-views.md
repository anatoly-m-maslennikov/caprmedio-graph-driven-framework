---
atom_id: CA-E-785
ref_id: CA-E-785@1
container:
  scope_unit: CA-SU-43
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 5
relations:
  evaluation_for:
  - CA-R-2776
  - CA-M-470
  - CA-D-675
status: Archived
version: 1
updated_at: 2026-11-05 20:27:41 +0400
carrier_destination:
  file:
    name: CA-E-785@1-WORKBENCH-EVAL_CASE--verify-result-retention-and-one-query-views.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation/archived
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Verify Workbench result retention and one-query Views

## Claim scope

The shared Workbench result cache, open-View pinning, runtime TTL setting and whole-query execution as observed through MCP and the web frontend.

## Claim

### Prose Claim

Using a real user-facing end-to-end run against one Project, exercise the same shared Workbench backend through MCP and the Workbench web frontend. The evaluation **must**:

- read `.caprmedio_runtime/caprmedio_runtime_settings.toml` at Workbench start. With the file missing, observe the 3,600-second default. With `[workbench] result_ttl_seconds = 1`, perform an explicit `workbench_restart`/reread and observe the new positive-integer value; editing the file without restart does not hot-reload it. An existing invalid value such as `0` fails the start/reload boundary on stderr and is not silently replaced by the default. The settings file is outside watcher `control_root` and creates no `change_log` row.
- run one query through one frontend, page or inspect its result through the other, and confirm the same backend result owner is used rather than a second frontend cache. Record a monotonic creation time and verify that an unpinned result remains available while its age is below the configured TTL and can expire after the TTL on the existing idle-owner wait and Run/Page cleanup.
- keep the View open past the TTL and confirm its result remains available while pinned. Close the View, confirm it is unpinned, and verify that a young result remains until the TTL while an old unpinned result may be expired. Do not require a heartbeat, cross-process lease, crash recovery path, scheduler or new service.
- run a query in a View, rerun it, and confirm the previous result is dropped before the replacement starts. Force the replacement to fail and confirm that the old result and ID are not returned or restored; a successful replacement exposes only the new result.
- restart the Workbench backend and confirm every transient result table and result ID is gone while the rebuildable source Projection is recreated. No permanent saved query or View Journal entry is deleted.
- leave an unfinished SQL edit in the View and confirm it remains editable. Run and Check must reject multiple whole queries, including semicolon-delimited statements, rather than executing only the query at the editor caret. A cursor position may persist as caret metadata but does not select execution.

The evaluation passes only when real MCP and browser-visible behavior matches every case, both surfaces observe the same retention rules, and no source file or watcher change log is modified by the runtime settings file.
