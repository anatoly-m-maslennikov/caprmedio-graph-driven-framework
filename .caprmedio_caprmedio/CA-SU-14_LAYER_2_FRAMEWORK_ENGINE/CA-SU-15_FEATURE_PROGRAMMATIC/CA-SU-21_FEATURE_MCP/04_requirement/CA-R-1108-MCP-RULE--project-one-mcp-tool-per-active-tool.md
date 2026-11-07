---
atom_id: CA-R-1108
ref_id: CA-R-1108
container:
  scope_unit: CA-SU-21
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
tier: 1
status: Active
version: 21
updated_at: 2026-11-07 13:19:43 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
---
# Project one MCP tool per active Tool

MCP must expose exactly one callable endpoint for each enabled public Tool name in the installed registration configuration, backed by its canonical code handler and request/result contract. Source-only providers have no public endpoint. Reject duplicate public identities and preserve canonical operation meaning. No current Atom declaration is required merely to register or list an implemented, configured Tool.
