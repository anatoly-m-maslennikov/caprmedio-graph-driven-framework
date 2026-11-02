---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit.Scope
  depends_on: []
version: 1
updated_at: 2026-10-29 20:32:25 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-draft
status: Draft
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: APPS
type: Scope Definition
tier: 1
claim_target_scope_unit: GRAPH_SERVER
---
## Summary

Own a rebuildable read-only graph service independent of the graph interface

## Claim scope

Scope and obligations of GRAPH_SERVER

## Claim

GRAPH_SERVER **must** own the rebuildable non-authoritative graph read model **and** read-only service used by Tools, MCP, **and** optional interfaces without requiring GRAPH_UI.
