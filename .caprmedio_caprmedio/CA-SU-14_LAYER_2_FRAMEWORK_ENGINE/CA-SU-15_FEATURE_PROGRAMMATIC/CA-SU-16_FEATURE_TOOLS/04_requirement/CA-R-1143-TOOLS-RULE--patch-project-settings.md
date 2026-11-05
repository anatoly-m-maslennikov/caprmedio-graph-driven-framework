---
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Data Validation
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 20
updated_at: 2026-11-02 19:44:26 +0400
atom_id: CA-R-1143
ref_id: CA-R-1143
status: Active
role: Requirement
author: Anatoly Maslennikov
current_scope_unit: TOOLS
form: Rule
tier: 1
container:
  scope_unit: CA-SU-16
---
# Patch project settings

the framework **must** provide one deterministic Tool that applies a schema-validated key-level patch **to** project settings, preserves unrelated values, emits the exact effective diff, **and** rejects direct edits **to** values declared as generated.
