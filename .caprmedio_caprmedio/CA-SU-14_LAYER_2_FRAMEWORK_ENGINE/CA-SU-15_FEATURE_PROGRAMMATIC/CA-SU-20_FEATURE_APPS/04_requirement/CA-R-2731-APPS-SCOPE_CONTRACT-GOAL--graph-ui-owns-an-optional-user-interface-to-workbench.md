---
cce_version: cce_1
cce_form: obligation
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/UX
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure
version: 1
updated_at: 2026-11-03 23:17:14 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-2731
ref_id: CA-R-2731
status: Active
role: Requirement
author: Anatoly Maslennikov
current_scope_unit: APPS
form: Goal
tier: 0
claim_target_scope_unit: GRAPH_UI
container:
  scope_unit: CA-SU-20
---
## Summary

GRAPH_UI owns an optional user interface to WORKBENCH

## Claim

GRAPH_UI **must** own the optional human-facing interface over WORKBENCH. GRAPH_UI **must not** be a prerequisite for **any** of the following:

- headless graph access;
- Tools; **or**
- MCP.
