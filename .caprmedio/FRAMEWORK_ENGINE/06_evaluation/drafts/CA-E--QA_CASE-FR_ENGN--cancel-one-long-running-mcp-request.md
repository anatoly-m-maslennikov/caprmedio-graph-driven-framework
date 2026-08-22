---
subject_scopes:
  - framework-engine-mcp
  - failure-recovery
version: 1
updated_at: 2026-08-22 02:15:57
relations: {}
---
# Cancel one long-running MCP request

Given one long-running MCP request with a progress identity, issue cancellation before completion. Verify that the adapter stops or isolates downstream work according to its declared boundary, releases bounded resources, emits no successful terminal result, and handles a late completion without reviving the cancelled request.

Candidate alignment: CA-E-001, CA-E-002, CA-D-001, CA-R-827, CA-R-861.

## Sources

- [Model Context Protocol: cancellation](https://modelcontextprotocol.io/specification/2024-11-05/basic/utilities/cancellation)
- [Model Context Protocol: tasks](https://modelcontextprotocol.io/specification/2025-11-25/basic/utilities/tasks)
