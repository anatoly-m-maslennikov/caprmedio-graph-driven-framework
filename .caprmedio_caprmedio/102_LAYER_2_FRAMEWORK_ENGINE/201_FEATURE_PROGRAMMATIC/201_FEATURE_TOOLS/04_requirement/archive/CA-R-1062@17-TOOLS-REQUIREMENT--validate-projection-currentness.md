---
subjects:
  governs: projection-pipeline
  depends_on:
  - Subject/Domain/Node/Continuant/Projection
  - Subject/Domain/Node/Continuant/Projection/Type
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 17
updated_at: 2026-10-24 01:28:26 +0400
atom_id: CA-R-1062@17
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Rule
---
# Validate Projection currentness

the framework **must** provide one deterministic read-only Tool that validates one programmatic-generated **or** LLM-generated Projection's declared Projection Type, `updated_at`, `source_frontier`, source availability, **and** currentness **without** treating the Projection as independent authority.
