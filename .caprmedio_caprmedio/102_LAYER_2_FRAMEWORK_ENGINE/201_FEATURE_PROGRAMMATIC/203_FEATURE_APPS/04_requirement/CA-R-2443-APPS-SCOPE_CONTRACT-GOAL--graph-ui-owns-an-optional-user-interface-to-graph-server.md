---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/UX
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure
version: 1
updated_at: 2026-10-30 03:11:57 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-2443
status: Active
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: APPS
type: Goal
tier: 0
claim_target_scope_unit: GRAPH_UI
---
## Summary

GRAPH_UI owns an optional user interface to GRAPH_SERVER

## Claim

GRAPH_UI **must** own the optional human-facing interface over GRAPH_SERVER. GRAPH_UI **must not** be a prerequisite for **any** of the following:

- headless graph access;
- Tools; **or**
- MCP.
