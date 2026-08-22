---
subject_scopes:
  - feature-boundary
tier: core
version: 1
updated_at: 2026-08-22 01:52:52
llm_session_ids:
  - codex:01a01cb6-4ee4-7553-b68d-0823dda35094
relations:
  child_of:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-703--define-apps-feature-scope
---
# Define the MCP unit

`MCP` with prefix `MCP` must be one `unordered_unit` owned immediately by `APPS` at Structural level `3`, addressed by `FRAMEWORK_ENGINE/APPS/MCP`; it owns the provider-neutral Model Context Protocol discovery, schema, and dispatch interface that projects active CAPRMEDIO Tools for agent use without owning Tool behavior, Skill procedures, or agent-host-specific packaging.
