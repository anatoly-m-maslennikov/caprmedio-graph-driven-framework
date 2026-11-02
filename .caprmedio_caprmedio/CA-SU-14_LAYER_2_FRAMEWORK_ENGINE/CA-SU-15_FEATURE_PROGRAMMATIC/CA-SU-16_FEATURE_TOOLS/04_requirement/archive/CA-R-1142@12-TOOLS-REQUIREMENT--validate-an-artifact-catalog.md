---
subjects:
  governs: artifact-catalog
  depends_on: []
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 12
updated_at: 2026-10-24 01:28:26 +0400
atom_id: CA-R-1142@12
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Rule
---
# Validate an artifact catalog

the framework **must** provide one deterministic read-only Tool that compares a registered artifact catalog with its declared authoritative source frontier **and** fails closed on missing, stale, duplicate, unknown, **or** inconsistent entries.
