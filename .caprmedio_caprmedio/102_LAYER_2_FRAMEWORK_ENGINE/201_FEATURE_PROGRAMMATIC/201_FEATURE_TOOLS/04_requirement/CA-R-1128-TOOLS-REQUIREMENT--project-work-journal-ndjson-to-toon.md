---
subjects:
  governs: journal-projection
  depends_on: []
version: 13
updated_at: 2026-10-24 02:14:24 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1128
status: Active
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Rule
tier: 1
---
# Project Work Journal NDJSON to TOON

CAPRMEDIO provides a deterministic Tool that losslessly projects a bounded, identified Work Journal NDJSON frontier into a reproducible non-authoritative TOON view while preserving source identity, ordering, frontier, **and** encoder provenance **and** failing **before** publication on malformed **or** changed input.
