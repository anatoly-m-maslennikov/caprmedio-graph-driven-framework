---
subjects:
  governs: Subject/Graph Node/Engineering/Data Handling/Data Validation
  depends_on: []
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 18
updated_at: 2026-10-27 06:04:45 +0400
atom_id: CA-R-1143@18
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Rule
tier: 1
---
# Patch project settings

the framework **must** provide one deterministic Tool that applies a schema-validated key-level patch **to** project settings, preserves unrelated values, emits the exact effective diff, **and** rejects direct edits **to** values declared as generated.
