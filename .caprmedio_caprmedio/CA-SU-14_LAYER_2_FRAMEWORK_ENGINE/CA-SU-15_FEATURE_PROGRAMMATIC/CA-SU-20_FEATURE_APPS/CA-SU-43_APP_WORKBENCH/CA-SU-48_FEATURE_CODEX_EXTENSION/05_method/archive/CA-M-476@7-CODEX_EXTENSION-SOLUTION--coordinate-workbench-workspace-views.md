---
identity:
  atom_id: CA-M-476@7
  ref_id: CA-M-476@7
context:
  container:
    scope_unit: CA-SU-48
  role: Method
  form: Solution
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Development <+
      Architecture <+ Communication <+ Interface Contracts
    dependencies:
    - CAPRMEDIO_MODEL <+ Workspace
  tier: 4
relations:
  method_for:
  - CA-R-2902
  - CA-R-2903
state:
  status: Archived
  version: 7
  updated_at: 2026-11-09 07:45:15 +0400
destination:
  file:
    name: CA-M-476@7-CODEX_EXTENSION-SOLUTION--coordinate-workbench-workspace-views.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-48_FEATURE_CODEX_EXTENSION/05_method/archive
current_scope_unit: CODEX_EXTENSION
claim_target_scope_unit: CODEX_EXTENSION
author: Anatoly Maslennikov
---

## Summary

Coordinate Workbench Workspace Views

## Claim

### Prose Claim

Use the existing Codex chat as the native Workspace boundary and the existing `workspace_open` MCP operation as the native UI activation. Its host tool input is the sole native identity source: accept only non-empty `session_id` and explicit trusted `project_root`, and accept its initial structured result as the opened Workspace. Do not read URL parameters or localStorage in native mode, manufacture a native session, bind another Workspace, or call `workspace_open` a second time. Missing input or result is a visible binding error and makes no backend call.

Use one shared Svelte Workbench UI. Native bootstrap uses MCP Apps initialization and the `tools/call` bridge; it injects the explicit `project_root` into every call, preserves `structuredContent`, and rejects `isError`. It adds no domain logic, response adapter, MCP service, chat, or UI-specific handler.

The initial native Workspace result carries the selected Project's canonical project_name. Reuse the existing ProjectSelection settings/name reader at the public adapter boundary. Keep this derived name out of persisted Workspace documents and do not infer it from a directory basename or add a query, parser, fallback name, or tool. The native frontend uses that supplied name for its Project header.
