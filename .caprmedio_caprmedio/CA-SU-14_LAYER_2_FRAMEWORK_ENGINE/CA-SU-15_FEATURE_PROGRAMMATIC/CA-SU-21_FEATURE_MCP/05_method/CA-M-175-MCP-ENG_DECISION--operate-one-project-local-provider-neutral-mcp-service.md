---
atom_id: CA-M-175
ref_id: CA-M-175
container:
  scope_unit: CA-SU-21
role: Method
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Entry
tier: 2
relations:
  method_for:
  - CA-R-1113
  derived_from:
  - CA-A-057
status: Active
version: 19
updated_at: 2026-11-05 13:48:40 +0400
carrier_destination:
  file:
    name: CA-M-175-MCP-ENG_DECISION--operate-one-project-local-provider-neutral-mcp-service.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-21_FEATURE_MCP/05_method
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
---

## Summary

Operate one project-local provider-neutral MCP service

## Claim

Apply **when** a Project exposes its generated Tool surface through MCP.

1. Bind one provider-neutral project-local service to one immutable ProjectSelection for each invocation; a shared service may serve multiple explicit Project bindings.
2. At the MCP Tool-call boundary, read the Codex hook's top-level project_root only as a Project-selection assertion. In single-Project mode, allow it to be omitted and use the fixed bound selection; when supplied, validate its canonical host path, container mapping and identity against that selection. In shared mode, require it and validate the selected admitted binding. Do not wrap initialize or tools/list in this Tool-call envelope; Prompt and Workflow wrappers retain their normal native dispatch.
3. Reject malformed, escaping, symlink-substituted, foreign or mismatched project_root values before native Tool dispatch, source effects or Journal effects. Remove the hook envelope field before passing the remaining native arguments to a Tool.
4. Expose each eligible Tool through that service without requiring a user interface or agent-host plugin. Do not let a request select a different Project after the service has been bound.

The complete MCP Tool surface remains headless, project-local and provider-neutral for each bound Project invocation.

Stop **when** an additional service becomes a competing authority, a project_root assertion does not match its bound ProjectSelection, or a capability depends on App presentation. Do not introduce a process-global Project selector.
