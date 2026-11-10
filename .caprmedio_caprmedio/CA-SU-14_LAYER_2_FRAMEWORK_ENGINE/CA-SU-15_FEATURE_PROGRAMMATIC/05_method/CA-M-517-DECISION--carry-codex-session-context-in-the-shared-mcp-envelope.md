---
identity:
  atom_id: CA-M-517
  ref_id: CA-M-517
context:
  container:
    scope_unit: CA-SU-15
  role: Method
  form: Decision
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
      <+ Architecture <+ Communication <+ Interface Contracts
  tier: 5
state:
  status: Active
  version: 1
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-M-517-DECISION--carry-codex-session-context-in-the-shared-mcp-envelope.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method
relations:
  method_for:
  - CA-R-3016
author: Anatoly Maslennikov
---

## Summary

Carry Codex session context in the shared MCP envelope

## Claim



### Prose Claim
Pass the existing trusted Project binding and native session ID without requiring a plugin. Do not invent a session ID, choose another Project or alter native Tool arguments.

Read the native Codex session identifier from hook input `event.session_id` as the hook's `codex_session_id`. Before submitting the MCP call, put that unchanged value in generic `caller_context.session_id`, alongside the existing `project_root` binding. Other client adapters use the same generic caller context.

The MCP adapter validates `caller_context` and passes its `session_id` into separate runtime request context. Runtime schemas and behavior do not use a Codex-specific field or branch on the harness or LLM provider. Remove only the outer caller context from native arguments; preserve a native Tool's own `session_id` argument. Require the session binding for session-scoped Workflow Run operations; allow it to be absent for stateless operations. Reject disagreement with supplied context instead of silently replacing it.

Deliver the receiving schema and gateway support before enabling the hook to send the new field. No plugin or transcript parsing is required.
