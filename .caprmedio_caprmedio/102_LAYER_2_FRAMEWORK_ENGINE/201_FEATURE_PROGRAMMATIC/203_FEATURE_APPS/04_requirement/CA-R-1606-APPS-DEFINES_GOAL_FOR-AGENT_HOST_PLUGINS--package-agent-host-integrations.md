---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: AGENT_HOST_PLUGINS/Goal
  depends_on:
  - APPS
version: 6
updated_at: 2026-10-24 02:14:24 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1606
status: Active
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: APPS
type: Goal
tier: 1
---
# Package Agent-Host Integrations

AGENT_HOST_PLUGINS **must** own installable host-specific integration packages and wiring while referencing, rather than duplicating, provider-neutral Tools, Prompts, Skills, MCP, Apps, **and** methodology behavior.
