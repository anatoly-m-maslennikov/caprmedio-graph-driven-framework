---
atom_id: CA-R-1125
ref_id: CA-R-1125
container:
  scope_unit: CA-SU-16
role: Requirement
form: Rule
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Data Transformation"
tier: 1
status: Active
version: 20
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Validate generated-data stage pipelines

the framework **must** provide a deterministic Tool that validates the registered `src → stg → mrt → biz` prefixes, forward-only dependencies, declared source frontiers, **and** the separation of generated outputs from semantic authority.
