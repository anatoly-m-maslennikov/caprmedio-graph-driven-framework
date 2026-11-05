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

## Subsequent implementation and local release

The local marketplace was registered and plugin `caprmedio-workbench@caprmedio-local` version `0.1.1` was installed and enabled. Its Skill now uses the compatibility probe instead of opening a browser as a substitute for native UI. The hook was not automatically trusted.

Local release `0.4.4.26` serves the probe through the existing MCP connection. Live checks passed for 45 tool descriptors, the exact package-local HTML resource, both read-only tools and the Workbench HTTP page. A separate live browser check confirmed the clean standalone URL and preserved local identity after reload.

The agent still has no exposed CAPRMEDIO tool handles in this chat. Native Codex rendering and its host bridge remain unverified. The complete native Workbench interface is not delivered. Next: invoke `workbench_ui_probe` from a Codex chat where the refreshed connection is available and observe the component and button.

## Operator screenshot: file preview

The Operator opened `workbench/codex-ui-probe/probe.html` in a file preview. It displayed “Tool bridge failed: Inline visualizations cannot call tools” and “Waiting for the host tool result.” This confirms HTML rendering in that preview, but not an MCP App launched by `workbench_ui_probe`. No native tool result or successful tool bridge was observed. The native-host acceptance gate remains open; do not count this screenshot as a successful plugin launch or infer that a genuine MCP App launch is unsupported.

## After Codex reload

CAPRMEDIO tool handles became available in this chat. The agent invoked `workbench_ui_probe` through that connection and received the expected structured message. The MCP Apps side-panel inventory was empty; an inline component, if shown, is not exposed through that inventory until expanded. Native component rendering and the button bridge remain awaiting observation. No HTML file or browser page was opened as a substitute.

## Successful inline native test

The Operator confirmed that the actual component is inside the Codex session, not the right panel. Their latest screenshot shows both “CAPRMEDIO MCP App resource loaded” and “Tool bridge passed”. This establishes native inline rendering, receipt of the initial tool result and a successful UI-initiated MCP call. It does not establish a persistent right-panel surface or the full Workbench interface. The earlier failed file-preview observation is superseded for the inline native capability check.
