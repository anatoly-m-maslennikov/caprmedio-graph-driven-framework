---
subjects:
  governs: artifact-migration
  depends_on: []
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 12
updated_at: 2026-10-24 01:28:26 +0400
atom_id: CA-R-1138@12
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Rule
---
# Plan an artifact migration

the framework **must** provide one deterministic read-only Tool that expands a declared artifact transformation into a reviewable migration plan containing source preconditions, identity mappings, collision checks, affected references, affected Projections, **and** expected postconditions.
