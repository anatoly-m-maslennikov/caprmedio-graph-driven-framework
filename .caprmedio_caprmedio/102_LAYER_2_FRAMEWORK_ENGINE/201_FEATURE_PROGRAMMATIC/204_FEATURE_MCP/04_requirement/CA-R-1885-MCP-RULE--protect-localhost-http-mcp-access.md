---
atom_id: CA-R-1885
content_role: Requirement
current_scope_unit: MCP
status: Active
author: Anatoly Maslennikov
version: 14
updated_at: 2026-10-27 20:00:05 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication/API
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect Authorization
relations: {}
tier: 3
type: Rule
---
# Summary

protect localhost HTTP MCP access

## Scope

the additional localhost HTTP transport for the existing Project MCP Gateway.

## Claim

the HTTP endpoint **must** admit a Request only through its loopback Host/Origin boundary, without password, bearer, or other HTTP authentication, while preserving the existing Operator authorization and Tool permission boundaries.

## Details

1. publish the Docker port on host loopback **only**. Requests with an absent Origin are allowed for non-browser clients; a present Origin must be loopback-allowlisted.
2. hostile Hosts and hostile Origins fail closed before Tool handling. A password, bearer Token, Authorization value, or credential configuration is neither required nor validated.
3. preserve existing Operator authorization and Tool permission checks after the transport boundary; localhost transport admission does not grant mutation permission.
4. do not add HTTP credentials to discovery, results, diagnostics, logs, command arguments, image contents, committed carriers, or persistent configuration.
