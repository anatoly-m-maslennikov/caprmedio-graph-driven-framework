---
identity:
  atom_id: CA-D-707
  ref_id: CA-D-707@1-draft
context:
  container:
    scope_unit: CA-SU-48
  role: Delivery
  form: Solution
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Delivery <+ Packaging
    dependencies:
    - CAPRMEDIO_MODEL <+ Workspace
    - CAPRMEDIO_MODEL <+ View
  tier: 4
state:
  status: Draft
  version: 1
  updated_at: 2026-11-10 06:28:05 +0400
destination:
  file:
    name: CA-D-707@1-draft-SOLUTION--deliver-the-native-workbench-mcp-app.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-48_FEATURE_CODEX_EXTENSION/07_delivery/draft
relations:
  delivery_for:
  - CA-R-2902
author: Anatoly Maslennikov
---

## Summary

Deliver the native Workbench MCP App

## Claim

### Prose Claim

The shared Svelte Workbench UI **must** use MCP Apps initialization and the `tools/call` bridge in native mode. It **must** inject the explicit `project_root` into every call, preserve `structuredContent`, reject `isError`, and add no domain logic, response adapter, MCP service, chat, or UI-specific handler. Standalone mode retains the existing HTTP bootstrap; native mode and standalone mode use the same `App.svelte` and Workbench backend.

`workspace_open` is the sole UI-bearing MCP tool. Its descriptor **must** link `ui://caprmedio/workbench.html`, served as `text/html;profile=mcp-app`. `workbench_app.html` **must** be one self-contained MCP App resource built with the existing Vite/Svelte toolchain: its JavaScript and CSS are inline, it opens no browser, makes no Workbench HTTP request, and needs no second server. `FEATURE_MCP` adds that resource URI only to the existing `workspace_open` descriptor and serves the built resource through its existing registry/read handler; existing dispatch, Project validation, and structured-result paths remain unchanged.

`FEATURE_CODEX_EXTENSION` instructions **must** direct the caller to invoke `workspace_open` with the host-supplied session ID and trusted Project root. Its hook supplies context only, starts nothing, and registers no panel; `plugin.json` adds no panel or connection declaration. The existing `caprmedio-workbench` package **must** be registered in `.agents/plugins/marketplace.json` under `caprmedio-local` with local source `./LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_APPS/APP_WORKBENCH/FEATURE_CODEX_EXTENSION/plugin`. The desktop app discovers it after restart and the Operator installs it and explicitly trusts the bundled hook through `/hooks`. Activation requires a new or resumed native chat; building or releasing the backend neither installs the plugin nor retroactively runs a hook.
