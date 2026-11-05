---
atom_id: CA-E-679
ref_id: CA-E-679
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Active
version: 1
author: Anatoly Maslennikov
role: Evaluation
form: Eval Case
tier: 5
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
updated_at: 2026-11-05 05:49:16 +0400
carrier_destination:
  file:
    name: CA-E-679-WORKBENCH-EVAL_CASE--verify-explicit-workbench-restart-through-mcp.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation
relations:
  evaluation_for:
  - CA-R-2782
container:
  scope_unit: CA-SU-43
---

## Summary

Verify explicit Workbench restart through MCP

## Claim

An explicit MCP Workbench restart returns only after a fresh owner is ready, clears old query-result IDs, preserves sources and saved items, and leaves the MCP session and unrelated services usable. Invalid startup returns an explicit error and does not trigger automatic recovery.

## Details

| Scenario | Expected outcome |
| --- | --- |
| Run, save a query, restart, query again through one MCP session | Restart succeeds; fresh queries work; old Page ID is rejected; saved SQL still loads. |
| Scope Unit Declaration becomes invalid | Workbench reports unavailable. A restart while the Declaration is still invalid fails explicitly. |
| Declaration is corrected after that failure | It stays unavailable until explicit restart; restart then succeeds and reads corrected sources. |
| Another Workbench call is in flight | Restart waits for that call before closing its owner; no call uses a closed owner. |
| Request is cancelled while its synchronous work is in flight | Restart cannot close that owner until the synchronous work finishes. |
| Unexpected restart arguments | Rejected before a service effect. |
| Other MCP tools and source files | The same MCP session remains usable; source bytes and saved-item history remain unchanged. |
