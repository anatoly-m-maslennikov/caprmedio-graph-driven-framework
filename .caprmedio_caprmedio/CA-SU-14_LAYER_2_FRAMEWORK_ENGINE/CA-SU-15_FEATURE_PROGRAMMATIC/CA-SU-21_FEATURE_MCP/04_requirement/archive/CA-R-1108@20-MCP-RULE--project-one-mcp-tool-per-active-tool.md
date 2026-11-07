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
version: 20
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: MCP
---
# Project one MCP tool per active Tool

MCP **must** project exactly one callable MCP tool for **every** valid active immediate Tool unit **and** no callable MCP tool **without** one such source Tool. The MCP tool identity **must** derive stably from the canonical Tool identity; aliases, accidental duplicates, implicit aggregation, **and** splitting one Tool into multiple public MCP identities are prohibited **unless** separately governed by new Tool authority.
