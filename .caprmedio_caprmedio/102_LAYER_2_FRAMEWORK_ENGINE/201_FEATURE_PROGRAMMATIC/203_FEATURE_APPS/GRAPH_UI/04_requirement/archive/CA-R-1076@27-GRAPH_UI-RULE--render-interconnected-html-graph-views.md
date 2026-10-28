---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Subject/Graph Node/UX/Graph view presentation and navigation
  depends_on: []
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 27
updated_at: 2026-10-26 00:46:35 +0400
atom_id: CA-R-1076@27
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: APPS
type: Rule
tier: 1
---
# Render interconnected HTML graph views

the optional `GRAPH_UI` unit **must** render interconnected HTML graph views through `GRAPH_SERVER` from its current derived read model **and** the governed source frontier behind that model. It **may** also consume a persisted `GENERATE_ENTITY_GRAPH` Projection for declared Terms, their direct-parent tree, direct dependency graph, **and** complete dependency-Term closure. The views **must** provide short **and** detailed node presentation, tier, current Structural-unit, Content-role, **and** Type filters, orphan **and** cycle visibility controls, source lineage, unknown-region diagnostics, **and** access **to** current Atom content **without** treating **any** Projection as governed authority **or** modifying authority. Disabling or omitting `GRAPH_UI` **must not** disable `GRAPH_SERVER`, Tools, or MCP.
