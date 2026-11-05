# Codex plugin UI capability check

Date: 2026-11-06

The requested integrated Workbench plugin UI is not implemented. The current package is a SessionStart hook and Skill that opens the existing Workbench URL in a browser panel. That does not satisfy the Operator's request.

## Verified

- The existing backend already supplies chat-bound Workspaces, View operations, metadata-only Run and paginated Fetch. It can be reused.
- Codex CLI 0.166.0's generated app-server schema carries `McpAppUi.resourceUri` and `preferredModelDisplayMode`, with `inline` and `fullscreen` values. This is protocol support, not proof of a rendered UI.
- A disposable read-only MCP Apps probe passes initialization, tool discovery, UI-resource retrieval and tool invocation through the installed MCP SDK.
- The probe's HTML connects and calls its read-only tool through a synthetic host bridge in a real headless browser, without uncaught errors. This is not a Codex rendering test.

## Unverified

- Whether the running Codex app renders a local MCP Apps UI.
- Whether Codex supplies a persistent custom side-panel surface. The official panel documentation found describes ChatGPT.
- Whether registering a new local MCP connection refreshes the current Codex chat. Agents API session behavior is not evidence of Codex Desktop behavior.

Computer-use access to the Codex app was refused. No app bundle was patched, plugin installed, server published, or configuration changed during this check.

## Next acceptance check

Load the read-only probe through Codex's local plugin/MCP connection support and invoke `workbench_ui_probe`. A native component must appear and its **Test tool bridge** button must report success. A text response or an ordinary browser panel does not pass.

Only after that proof should the existing Workbench UI be connected to the host bridge. A passing inline component would not prove a persistent side panel.

Scratch probe and evidence: `.caprmedio_tmp/workbench/codex-ui-probe/`.

## Official sources

- [Plugin packaging](https://developers.openai.com/plugins/build/plugins)
- [MCP Apps UI contract](https://developers.openai.com/plugins/build/chatgpt-ui)
- [ChatGPT plugin extensions](https://developers.openai.com/plugins/build/extensions)

Current metadata schemas and source files were checked directly. Product claims beyond the verified boundaries above remain open.
