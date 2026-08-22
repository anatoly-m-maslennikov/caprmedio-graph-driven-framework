---
subject_scopes:
  - framework-engine-mcp
version: 1
updated_at: 2026-08-22 01:50:50
relations: {}
---
# Expose MCP capabilities through bounded protocol adapters

Implement each Model Context Protocol server or client as a replaceable adapter over existing FRAMEWORK_ENGINE capabilities. Keep project meaning and business decisions outside the protocol carrier. Declare the supported protocol revision and capabilities, negotiate them during initialization, validate every message against the admitted schema, and map internal results and failures to stable protocol responses without leaking implementation details.

Apply explicit timeouts, cancellation, progress, and bounded resource use to long-running requests. Enforce the least authority needed for each capability, bind credentials to their intended transport and resource, and exclude secrets from diagnostics. Keep version negotiation and capability discovery observable so an incompatible host fails clearly rather than silently changing behavior.

Candidate alignment: CA-M-002, CA-M-005, CA-M-006, CA-D-001, CA-D-002.

## Sources

- [Model Context Protocol: lifecycle](https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle)
- [Model Context Protocol: base protocol](https://modelcontextprotocol.io/specification/2025-06-18/basic/index)
- [Model Context Protocol: authorization](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [Model Context Protocol: tasks](https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/tasks)
