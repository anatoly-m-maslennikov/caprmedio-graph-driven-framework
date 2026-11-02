---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/UX
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure
version: 15
updated_at: 2026-10-29 22:26:56 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1604@15
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: GRAPH_UI
type: Rule
tier: 0
claim_target_scope_unit: GRAPH_UI
---
## Summary

Provide an Optional Graph Interface

## Claim

GRAPH_UI **must** own the optional human-facing interface over GRAPH_SERVER and **must not** become a prerequisite for headless graph access, Tools, **or** MCP.
