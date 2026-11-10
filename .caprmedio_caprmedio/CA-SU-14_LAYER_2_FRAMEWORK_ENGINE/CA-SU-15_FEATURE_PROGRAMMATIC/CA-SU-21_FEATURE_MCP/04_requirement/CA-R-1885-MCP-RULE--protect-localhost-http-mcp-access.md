---
identity:
  atom_id: CA-R-1885
  ref_id: CA-R-1885
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
    - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture
      <+ Communication <+ API
    - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution
      Control <+ Effect Authorization
  tier: 3
state:
  status: Active
  version: 15
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-R-1885-MCP-RULE--protect-localhost-http-mcp-access.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement
current_scope_unit: MCP
author: Anatoly Maslennikov
---
## Summary

protect localhost HTTP MCP access

## Claim scope

the additional localhost HTTP transport for the existing Project MCP Gateway.

## Claim

### Prose Claim

the HTTP endpoint **must** admit a Request only through its loopback Host/Origin boundary, without password, bearer, or other HTTP authentication, while preserving the existing Operator authorization and Tool permission boundaries.

## Details

1. publish the Docker port on host loopback **only**. Requests with an absent Origin are allowed for non-browser clients; a present Origin must be loopback-allowlisted.
2. hostile Hosts and hostile Origins fail closed before Tool handling. A password, bearer Token, Authorization value, or credential configuration is neither required nor validated.
3. preserve existing Operator authorization and Tool permission checks after the transport boundary; localhost transport admission does not grant mutation permission.
4. do not add HTTP credentials to discovery, results, diagnostics, logs, command arguments, image contents, committed carriers, or persistent configuration.
