---
atom_id: CA-R-1142
ref_id: CA-R-1142
container:
  scope_unit: CA-SU-16
role: Requirement
form: Rule
topics:
  main_subject: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Catalog'
tier: 1
status: Active
version: 18
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Validate an artifact catalog

the framework **must** provide one deterministic read-only Tool that compares a registered artifact catalog with its declared authoritative source frontier **and** fails closed on missing, stale, duplicate, unknown, **or** inconsistent entries.
