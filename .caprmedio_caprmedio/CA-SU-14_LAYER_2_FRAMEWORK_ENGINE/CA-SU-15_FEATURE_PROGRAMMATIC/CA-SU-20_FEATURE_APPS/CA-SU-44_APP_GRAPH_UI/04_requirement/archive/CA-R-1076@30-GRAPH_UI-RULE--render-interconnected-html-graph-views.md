---
atom_id: CA-R-1076
ref_id: CA-R-1076@30
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Discovery and Navigation
tier: 1
status: Archived
version: 30
updated_at: 2026-11-03 23:17:14 +0400
cce_version: cce_1
cce_form: obligation
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: APPS
carrier_destination:
  file:
    name: CA-R-1076@30-GRAPH_UI-RULE--render-interconnected-html-graph-views.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-44_APP_GRAPH_UI/04_requirement/archive
---
## Summary

Render interconnected HTML graph views

## Claim

### Prose Claim

the optional `GRAPH_UI` unit **must** render interconnected HTML graph views through `WORKBENCH` from its current derived read model **and** the governed source frontier behind that model. It **may** also consume a persisted `GENERATE_ENTITY_GRAPH` Projection for declared Terms, their direct-parent tree, direct dependency graph, **and** complete dependency-Term closure. The views **must** provide short **and** detailed node presentation, tier, current Structural-unit, Content-role, **and** Type filters, orphan **and** cycle visibility controls, source lineage, unknown-region diagnostics, **and** access **to** current Atom content **without** treating **any** Projection as governed authority **or** modifying authority. Disabling or omitting `GRAPH_UI` **must not** disable `WORKBENCH`, Tools, or MCP.
