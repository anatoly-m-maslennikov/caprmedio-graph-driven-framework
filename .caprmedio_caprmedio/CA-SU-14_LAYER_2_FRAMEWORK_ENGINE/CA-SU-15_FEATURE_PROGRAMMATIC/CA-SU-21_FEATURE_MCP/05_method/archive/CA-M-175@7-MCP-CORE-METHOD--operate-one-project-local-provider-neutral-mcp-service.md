---
cce_version: cce_1
cce_form: method
subjects:
  governs: framework-engine-mcp
  depends_on: []
version: 7
updated_at: 2026-10-23 03:17:34 +0400
relations:
  method_for:
  - CA-R-1113
  derived_from:
  - CA-A-057
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-M-175@7
status: Archived
---
# Operate one project-local provider-neutral MCP service

## Applicable when

Apply **when** a project exposes its generated Tool surface through MCP.

## Procedure

1. Bind one provider-neutral project-local service **to** the current registry
   and selected Project frontier for each invocation; the shared service may
   serve multiple explicit Project bindings.
2. Expose each eligible Tool through that service **without** requiring a user interface **or** agent-host plugin.
3. Permit a plugin **to** package **or** connect **to** the service **without** moving provider-neutral MCP **or** Tool ownership into the plugin.

## Outcome

the complete MCP Tool surface remains headless, project-local, **and**
provider-neutral for each bound Project invocation.

## Failure or stop

Stop **when** an additional service becomes a competing authority **or** a
capability depends on App presentation. Do not introduce a process-global
Project selector.
