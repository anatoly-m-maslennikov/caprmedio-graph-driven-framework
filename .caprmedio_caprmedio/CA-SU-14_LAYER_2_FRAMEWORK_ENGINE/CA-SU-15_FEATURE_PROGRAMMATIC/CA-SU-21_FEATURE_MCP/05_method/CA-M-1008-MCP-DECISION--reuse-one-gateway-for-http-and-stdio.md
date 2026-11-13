---
atom_id: CA-M-1008
ref_id: CA-M-1008
container:
  scope_unit: CA-SU-21
role: Method
form: Decision
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
    <+ Architecture <+ Communication
  dependencies:
  - MODEL//CAPRMEDIO <+ Package/Project Package
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture
    <+ Component Structure
  - MODEL//CAPRMEDIO <+ Runtime/Session
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution
    Control <+ Recovery
tier: 4
relations:
  method_for:
  - CA-R-1884
  is_replacement_for:
  - CA-M-341
status: active
version: 2
updated_at: '2026-11-12T17:03:37.731536+00:00'
carrier_destination:
  file:
    name: CA-M-1008-MCP-DECISION--reuse-one-gateway-for-http-and-stdio.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/05_method
current_scope_unit: MCP
author: Anatoly Maslennikov
---
## Summary

Reuse one Gateway for HTTP and stdio

## Claim

### Prose Claim

Use the same MCP Gateway handlers and Tool registration for HTTP and stdio. The installed runtime provides one set of Tool behavior for both transports.

## Details

Use the installed MCP SDK’s Streamable HTTP application for HTTP Sessions. Close Sessions on shutdown. Apply code and compiled contract changes by starting a rebuilt runtime under CA-M-551.

For a saved Bookmark or View, derive its URL from the bound HTTP request when available. For stdio, use the bound Project's optional `workbench.public_url` in `.caprmedio_runtime/caprmedio_runtime_settings.toml`. It identifies the absolute HTTP or HTTPS Workbench page for that Project. If the URL is unavailable, return the saved ID with `saved_query_url: null` and `saved_query_url_reason: workbench_url_unknown`. Saving remains successful and the saved ID remains usable. Use the same rule for saved-item lists.
