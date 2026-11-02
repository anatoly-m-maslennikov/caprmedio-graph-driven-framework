---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 22
updated_at: 2026-10-27 19:59:49 +0400
atom_id: CA-R-1062
status: Active
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Rule
tier: 1
---
# Validate Projection currentness

the framework **must** provide one deterministic read-only Tool that validates one programmatic-generated **or** LLM-generated Projection's declared Projection Type, `updated_at`, `source_frontier`, source availability, **and** currentness **without** treating the Projection as independent authority.
