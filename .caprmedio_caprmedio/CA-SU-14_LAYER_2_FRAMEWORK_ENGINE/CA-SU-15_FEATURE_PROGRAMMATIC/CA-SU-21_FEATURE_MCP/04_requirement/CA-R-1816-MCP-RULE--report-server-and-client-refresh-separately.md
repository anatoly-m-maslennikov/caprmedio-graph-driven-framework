---
identity:
  atom_id: CA-R-1816
  ref_id: CA-R-1816
context:
  container:
    scope_unit: CA-SU-21
  role: requirement
  form: rule
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
      <+ Architecture <+ Communication
    dependencies:
    - MODEL//CAPRMEDIO <+ Actor/Operator
    - MODEL//CAPRMEDIO <+ Project
    - MODEL//CAPRMEDIO <+ Atom/(.Header.Role := Operations)/Workflow
    - MODEL//CAPRMEDIO <+ Atom
  tier: 3
state:
  status: Active
  version: 13
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-R-1816-MCP-RULE--report-server-and-client-refresh-separately.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement
current_scope_unit: MCP
author: Anatoly Maslennikov
---
## Summary

Report server and client refresh separately

## Claim scope

server-side hot reload for the Project-local MCP gateway.

## Claim

### Prose Claim

the MCP gateway **must** distinguish successful server publication from confirmed client discovery of the published Tool registry.

## Details

- publish changed Tool names, schemas **and** descriptions as one validated registry generation.
- announce a changed registry through the negotiated MCP Tool-list-change notification capability.
- notification delivery does **not** prove that Codex refreshed its cached Tool list.
- report client refresh as unconfirmed unless evidence from that client establishes the current registry.
- clients that do **not** refresh require an explicit reconnect; the gateway **must not** claim to modify the Codex desktop application.
- the initial gateway installation requires a reconnect from the currently running server.

