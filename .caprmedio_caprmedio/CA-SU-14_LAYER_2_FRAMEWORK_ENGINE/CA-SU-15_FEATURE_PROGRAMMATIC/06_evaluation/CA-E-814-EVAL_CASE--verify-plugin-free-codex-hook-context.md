---
identity:
  atom_id: CA-E-814
  ref_id: CA-E-814
context:
  container:
    scope_unit: CA-SU-15
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development
      <+ Architecture <+ Communication <+ Interface Contracts
  tier: 6
state:
  status: Active
  version: 1
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-E-814-EVAL_CASE--verify-plugin-free-codex-hook-context.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
relations:
  evaluation_for:
  - CA-M-517
  - CA-R-3016
author: Anatoly Maslennikov
---

## Summary

Verify plugin-free Codex hook context

## Claim

### Prose Claim

With no Workbench plugin installed, send a native Codex hook event containing a Project binding, session ID and CAPRMEDIO Tool arguments. Verify that the public MCP schema accepts the added outer context, the hook reads `event.session_id` as `codex_session_id`, sends its unchanged value as `caller_context.session_id`, and the adapter passes it as generic runtime context `session_id`, and native Tool arguments remain unchanged.

Include a Tool with its own `session_id` argument. Verify that this native argument survives unchanged and is separate from runtime context `session_id`. Check that the backend accepts generic session context without a Codex-specific field or plugin. Check absent, invalid and conflicting context, an unrelated Tool call, and a stateless call without a session. Context errors must not select a fallback Project or session.
