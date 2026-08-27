---
subject_scopes:
  - framework-engine-mcp
  - security
version: 1
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Reject one unauthorized MCP capability call

Given a valid MCP request whose authorization context lacks the required capability permission, submit it through the admitted transport. Verify rejection before project access, stable protocol error mapping, no credential or token material in logs, and no reuse of credentials bound to another resource.

Candidate alignment: CA-E-001, CA-E-002, CA-R-004, CA-R-827, CA-R-861.

## Sources

- [Model Context Protocol: authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [Model Context Protocol security guidance](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization#security-considerations)
