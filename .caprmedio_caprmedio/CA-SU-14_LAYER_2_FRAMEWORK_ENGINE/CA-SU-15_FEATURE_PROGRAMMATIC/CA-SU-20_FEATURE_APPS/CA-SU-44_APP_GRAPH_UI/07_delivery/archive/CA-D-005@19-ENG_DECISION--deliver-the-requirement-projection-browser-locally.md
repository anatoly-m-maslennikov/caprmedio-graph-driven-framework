---
atom_id: CA-D-005
ref_id: CA-D-005@19
role: Delivery
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Discovery and Navigation
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
tier: 2
relations:
  delivery_for:
  - CA-R-1076
  - CA-M-153
status: Archived
version: 19
updated_at: 2026-11-04 15:23:33 +0400
subject_scopes:
- projection-pipeline
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: APPS
carrier_destination:
  file:
    name: CA-D-005@19-ENG_DECISION--deliver-the-requirement-projection-browser-locally.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-44_APP_GRAPH_UI/07_delivery/archive
---
## Summary

Deliver the Requirement Projection browser locally

## Claim

### Prose Claim

the optional GRAPH_UI Requirement Projection browser **must** be delivered as exactly one project-local, non-authoritative `.caprmedio/mrt_atoms.html` file with embedded JavaScript, backed by strictly read-only access **to** the current per-structural-unit Requirement STG files **and** actual Atom Markdown; this Delivery creates no sibling web assets, is not required for headless service, **and** does **not** publish, host, **or** distribute the MRT outside the project.
