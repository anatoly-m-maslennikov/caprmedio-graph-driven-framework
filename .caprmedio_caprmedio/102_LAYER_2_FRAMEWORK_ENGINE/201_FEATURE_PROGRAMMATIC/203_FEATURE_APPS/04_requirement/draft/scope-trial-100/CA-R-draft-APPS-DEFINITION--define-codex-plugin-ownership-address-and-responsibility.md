---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure
  depends_on: []
version: 1
updated_at: 2026-10-29 20:32:25 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-draft
status: Draft
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: APPS
type: Definition
tier: 1
---
## Summary

Define CODEX_PLUGIN ownership, address, and responsibility

## Claim scope

Within the source applicability.

## Claim

`CODEX_PLUGIN` with prefix `CODEX_PLUGIN` **must** be one `unordered_unit` owned immediately by `AGENT_HOST_PLUGINS` at Structural level `5`, addressed by `002_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN`, **and** realized under `002_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/AGENT_HOST_PLUGINS/CODEX_PLUGIN/`; it owns the installable Codex-specific plugin package **and** Codex host wiring while referencing rather than redefining provider-neutral CAPRMEDIO behavior.

## Details

Verify the recorded address, structural level, prefix and parent against the current Scope Unit registry before admission; preserve the source responsibility.
