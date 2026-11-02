---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/UX
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure
version: 1
updated_at: 2026-10-29 23:57:07 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-2431@1
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: APPS
type: Goal
tier: 0
claim_target_scope_unit: GRAPH_UI
---
## Summary

GRAPH_UI owns an optional GRAPH_SERVER interface without becoming a prerequisite

## Claim

GRAPH_UI:

- **must** own the optional human-facing interface over GRAPH_SERVER; **and**
- **must not** become a prerequisite for headless graph access, Tools, **or** MCP.
