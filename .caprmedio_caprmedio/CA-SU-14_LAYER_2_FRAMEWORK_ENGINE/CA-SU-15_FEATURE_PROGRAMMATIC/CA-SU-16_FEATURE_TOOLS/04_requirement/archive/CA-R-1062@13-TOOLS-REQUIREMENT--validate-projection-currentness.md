---
subjects:
  governs: "projection-pipeline"
  depends_on:
    - "Projection"
    - "Projection/Type"
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 13
updated_at: 2026-10-23 03:17:34 +0400
atom_id: CA-R-1062@13
status: Archived
---
# Validate Projection currentness

the framework **must** provide one deterministic read-only Tool that validates one programmatic-generated **or** LLM-generated Projection's declared Projection Type, `updated_at`, `source_frontier`, source availability, **and** currentness **without** treating the Projection as independent authority.
