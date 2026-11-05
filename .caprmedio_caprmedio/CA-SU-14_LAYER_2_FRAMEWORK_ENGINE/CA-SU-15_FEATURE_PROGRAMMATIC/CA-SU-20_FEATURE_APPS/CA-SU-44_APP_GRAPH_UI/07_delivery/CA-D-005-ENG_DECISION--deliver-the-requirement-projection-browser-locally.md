---
subject_scopes:
- projection-pipeline
version: 19
updated_at: 2026-11-04 15:23:33 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  delivery_for:
  - CA-R-1076
  - CA-M-153
author: Anatoly Maslennikov
role: Delivery
current_scope_unit: APPS
status: Active
atom_id: CA-D-005
ref_id: CA-D-005
form: Eng Decision
tier: 2
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Discovery and Navigation
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
---
# Deliver the Requirement Projection browser locally

the optional GRAPH_UI Requirement Projection browser **must** be delivered as exactly one project-local, non-authoritative `.caprmedio/mrt_atoms.html` file with embedded JavaScript, backed by strictly read-only access **to** the current per-structural-unit Requirement STG files **and** actual Atom Markdown; this Delivery creates no sibling web assets, is not required for headless service, **and** does **not** publish, host, **or** distribute the MRT outside the project.
