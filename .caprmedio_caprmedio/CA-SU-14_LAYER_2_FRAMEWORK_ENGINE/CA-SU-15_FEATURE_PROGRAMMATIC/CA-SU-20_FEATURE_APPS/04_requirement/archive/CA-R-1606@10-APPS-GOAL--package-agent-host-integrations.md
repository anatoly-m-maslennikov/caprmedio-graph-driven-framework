---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Delivery
  depends_on:
  - Subject/Graph Node/Engineering/Aspect/Delivery
version: 10
updated_at: 2026-10-26 14:22:14 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1606@10
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: APPS
type: Goal
tier: 1
---
# Package Agent-Host Integrations

AGENT_HOST_PLUGINS **must** own installable host-specific integration packages and wiring while referencing, rather than duplicating, provider-neutral Tools, Prompts, Skills, MCP, Apps, **and** methodology behavior.
