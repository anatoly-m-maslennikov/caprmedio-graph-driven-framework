---
name: caprmedio-workbench
description: Operate a CAPRMEDIO Workbench Workspace and Views in the current native Codex session through the host-configured CAPRMEDIO MCP.
---

# CAPRMEDIO Workbench

Use the native session ID supplied at session start and the explicitly trusted Project root. Do not infer either value, start a service, or configure another MCP connection.

First discover the Workspace and View operations advertised by the existing CAPRMEDIO MCP. Call `workspace_open(session_id)` for this native session, then append `embedded=1` to the returned `workspace_url`, preserving its existing `workspace` and `project_root` parameters. Open that URL with `open_in_codex` beside the current chat (`placement: right`). Do not add the embedding marker to ordinary standalone browser URLs.

For ordinary work, create or select a View, update its SQL with its required revision, then run it. Use returned metadata; fetch result rows only when needed. Focus a View when that helps the current task. Save only when asked. Do not copy tool implementations or schemas into this skill.
