---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: GRAPH_SERVER/Goal
  depends_on:
  - APPS
version: 3
updated_at: 2026-10-24 00:28:02 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1603@3
status: Archived
---
# Serve the Derived Graph Headlessly

GRAPH_SERVER **must** own the rebuildable non-authoritative graph read model **and** read-only service used by Tools, MCP, **and** optional interfaces without requiring GRAPH_UI.
