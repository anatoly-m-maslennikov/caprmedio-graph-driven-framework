---
atom_id: CA-R-1885@7
content_role: Requirement
current_scope_unit: MCP
status: Archived
author: Anatoly Maslennikov
version: 7
updated_at: 2026-10-24 01:37:42 +0400
subjects:
  governs: Subject/Engineering/MCP/HTTP endpoint/Access boundary
  depends_on:
  - Subject/Engineering/MCP
  - HTTP
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Permission
  - Request
  - Subject/Engineering/MCP.Localhost Access Boundary
relations:
  relates_to:
  - CA-R-1118
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
