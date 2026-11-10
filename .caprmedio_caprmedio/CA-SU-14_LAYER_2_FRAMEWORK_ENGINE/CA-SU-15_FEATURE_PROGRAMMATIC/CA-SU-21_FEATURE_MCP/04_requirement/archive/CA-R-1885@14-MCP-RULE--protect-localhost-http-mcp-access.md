---
atom_id: CA-R-1885
ref_id: CA-R-1885@14
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication/API
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Effect
    Authorization
tier: 3
status: Archived
version: 14
updated_at: 2026-10-27 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-1885@14-MCP-RULE--protect-localhost-http-mcp-access.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/04_requirement/archive
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
