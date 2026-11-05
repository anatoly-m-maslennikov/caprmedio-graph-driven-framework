---
name: caprmedio-workbench
description: Operate a CAPRMEDIO Workbench Workspace and Views in the current native Codex session through the host-configured CAPRMEDIO MCP.
---

# CAPRMEDIO Workbench

Use the native session ID supplied at session start and the explicitly trusted Project root. Do not infer either value, start a service, or configure another MCP connection.

Discover the operations advertised by the existing CAPRMEDIO MCP. To test native UI support, call `workbench_ui_probe` with the trusted Project selector when required. The component must display the initial tool result and its button must complete a read-only bridge call. This is a compatibility probe, not the complete Workbench UI. If it does not render, report that native UI is unverified; do not substitute a browser opener.

For Workspace operations, call `workspace_open(session_id)` for this native session. Its URL is for browser use, not plugin activation. Keep the current chat and the explicit Project boundary.

For ordinary work, create or select a View, update its SQL with its required revision, then run it. Use returned metadata; fetch result rows only when needed. Focus a View when that helps the current task. Save only when asked. Do not copy tool implementations or schemas into this skill.
