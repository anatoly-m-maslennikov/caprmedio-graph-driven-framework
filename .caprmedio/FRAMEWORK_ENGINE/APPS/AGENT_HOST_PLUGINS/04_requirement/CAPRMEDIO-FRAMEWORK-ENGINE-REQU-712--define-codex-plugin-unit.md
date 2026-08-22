---
subject_scopes:
  - feature-boundary
tier: core
version: 3
updated_at: 2026-08-22 03:09:20
relations:
  child_of:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-711--define-agent-host-plugins-unit
---
# Define the CODEX_PLUGIN unit

`CODEX_PLUGIN` with prefix `CODEX_PLUGIN` must be one `unordered_unit` owned immediately by `AGENT_HOST_PLUGINS` at Structural level `4`, addressed by `FRAMEWORK_ENGINE/APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN`, and realized under `FRAMEWORK_ENGINE/APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN/`; it owns the installable Codex-specific plugin package and Codex host wiring while referencing rather than redefining provider-neutral CAPRMEDIO behavior.
