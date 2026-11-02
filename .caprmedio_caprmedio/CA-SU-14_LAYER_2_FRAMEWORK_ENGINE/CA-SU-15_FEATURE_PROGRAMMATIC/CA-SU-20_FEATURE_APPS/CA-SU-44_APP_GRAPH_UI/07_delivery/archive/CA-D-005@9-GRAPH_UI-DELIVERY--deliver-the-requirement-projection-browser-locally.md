---
subject_scopes:
- projection-pipeline
version: 9
updated_at: 2026-10-24 01:33:47 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  delivery_for:
  - CA-R-1076
  - CA-R-1077
  - CA-M-153
  - CA-M-154
author: Anatoly Maslennikov
content_role: Delivery
current_scope_unit: APPS
status: Archived
atom_id: CA-D-005@9
---
# Deliver the Requirement Projection browser locally

the optional GRAPH_UI Requirement Projection browser **must** be delivered as exactly one project-local, non-authoritative `.caprmedio/mrt_atoms.html` file with embedded JavaScript, backed by strictly read-only `GRAPH_SERVER` access **to** the current per-structural-unit Requirement STG files **and** actual Atom Markdown; this Delivery creates no sibling web assets, is not required for headless service, **and** does **not** publish, host, **or** distribute the MRT outside the project.
