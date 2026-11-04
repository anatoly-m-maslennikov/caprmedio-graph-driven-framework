---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: artifact-query
  depends_on: []
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 21
updated_at: 2026-10-24 01:28:26 +0400
atom_id: CA-R-1077@21
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: APPS
type: Rule
---
# Serve live graph sources read-only

the headless `GRAPH_SERVER` unit **must** give Tools, MCP clients, **and** optional interfaces strictly read-only access **to** registered current Atoms, Journals, Projections, **and** derived graph data, including persisted `GENERATE_ENTITY_GRAPH` Projection carriers; return source kind, non-authoritative status, source-frontier lineage, raw content, canonical path, **and** current digest **where** applicable; operate without `GRAPH_UI`; **and** reject inactive **or** unregistered targets, path traversal, symlink escape, authority substitution, **and** **every** mutation.
