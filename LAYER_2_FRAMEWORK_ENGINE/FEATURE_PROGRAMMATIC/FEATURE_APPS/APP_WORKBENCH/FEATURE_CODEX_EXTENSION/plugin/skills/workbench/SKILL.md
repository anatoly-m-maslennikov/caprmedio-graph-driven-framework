---
name: caprmedio-workbench
description: Operate a CAPRMEDIO Workbench Workspace and Views in the current native Codex session through the host-configured CAPRMEDIO MCP.
---

# CAPRMEDIO Workbench

Use the native session ID supplied at session start and the explicitly trusted Project root. Do not infer either value, start a service, or configure another MCP connection.

For Workspace work, call `workspace_open` once with that native session ID and trusted Project root. Its existing UI-bearing descriptor activates the MCP Workbench UI; use its structured result as the opened Workspace. Keep the current chat and Project boundary, and do not open a browser or make another connection.

The read-only `workbench_ui_probe` remains compatibility evidence only; it does not activate Workbench. If native UI does not render, report it as unverified rather than substituting a browser opener. For ordinary work, discover the existing MCP operations and use their returned metadata; fetch rows or save only when needed. Do not copy schemas or tool implementations into this skill.
