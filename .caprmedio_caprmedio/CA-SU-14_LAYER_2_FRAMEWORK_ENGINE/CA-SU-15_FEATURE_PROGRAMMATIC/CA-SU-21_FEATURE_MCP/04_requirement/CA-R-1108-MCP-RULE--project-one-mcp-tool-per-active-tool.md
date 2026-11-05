---
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
version: 20
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1108
ref_id: CA-R-1108
status: Active
role: Requirement
author: Anatoly Maslennikov
current_scope_unit: MCP
form: Rule
tier: 1
container:
  scope_unit: CA-SU-21
---
# Project one MCP tool per active Tool

MCP **must** project exactly one callable MCP tool for **every** valid active immediate Tool unit **and** no callable MCP tool **without** one such source Tool. The MCP tool identity **must** derive stably from the canonical Tool identity; aliases, accidental duplicates, implicit aggregation, **and** splitting one Tool into multiple public MCP identities are prohibited **unless** separately governed by new Tool authority.
