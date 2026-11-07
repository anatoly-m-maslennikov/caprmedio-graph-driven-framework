---
atom_id: CA-R-1106
ref_id: CA-R-1106
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Selection
tier: 1
status: Active
version: 20
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
---
# Discover active Tool units

MCP **must** discover the complete current set of immediate Tool units owned by `TOOLS` from the current project graph **and** their corresponding Tool folders. Every registered immediate Tool unit is eligible for MCP exposure **unless** current project authority **or** Configuration explicitly disables it; nested implementation helpers **and** folders that are **not** Tool units **must not** become MCP tools.
