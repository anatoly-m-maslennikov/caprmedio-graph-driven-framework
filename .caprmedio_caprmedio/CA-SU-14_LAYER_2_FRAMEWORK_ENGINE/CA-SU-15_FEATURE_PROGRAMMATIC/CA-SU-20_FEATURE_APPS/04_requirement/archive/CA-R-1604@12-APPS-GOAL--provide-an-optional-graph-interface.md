---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Architecture/Communication
  depends_on:
  - Subject/Graph Node/Engineering/Continuant/App Interface
  - Subject/Graph Node/Engineering/Aspect/Architecture/Component Structure
version: 12
updated_at: 2026-10-26 14:22:14 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1604@12
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: APPS
type: Goal
tier: 1
---
# Provide an Optional Graph Interface

GRAPH_UI **must** own the optional human-facing interface over GRAPH_SERVER and **must not** become a prerequisite for headless graph access, Tools, **or** MCP.
