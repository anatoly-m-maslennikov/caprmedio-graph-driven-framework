---
atom_id: CA-R-2731
ref_id: CA-R-2731
container:
  scope_unit: CA-SU-20
role: Requirement
form: Goal
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/UX
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure
tier: 0
status: Active
version: 1
updated_at: 2026-11-03 23:17:14 +0400
cce_version: cce_1
cce_form: obligation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: APPS
claim_target_scope_unit: GRAPH_UI
---
## Summary

GRAPH_UI owns an optional user interface to WORKBENCH

## Claim

GRAPH_UI **must** own the optional human-facing interface over WORKBENCH. GRAPH_UI **must not** be a prerequisite for **any** of the following:

- headless graph access;
- Tools; **or**
- MCP.
