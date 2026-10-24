---
subjects:
  governs: projection-pipeline
  depends_on: []
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 14
updated_at: 2026-10-24 01:28:26 +0400
atom_id: CA-R-1061@14
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Rule
---
# Rebuild one programmatic Projection

the framework **must** provide one deterministic Tool that rebuilds one registered programmatic Projection from its declared sources, writes `updated_at` **and** `source_frontier`, replaces the output atomically, **and** records the rebuild through the Work Journal Tool.
