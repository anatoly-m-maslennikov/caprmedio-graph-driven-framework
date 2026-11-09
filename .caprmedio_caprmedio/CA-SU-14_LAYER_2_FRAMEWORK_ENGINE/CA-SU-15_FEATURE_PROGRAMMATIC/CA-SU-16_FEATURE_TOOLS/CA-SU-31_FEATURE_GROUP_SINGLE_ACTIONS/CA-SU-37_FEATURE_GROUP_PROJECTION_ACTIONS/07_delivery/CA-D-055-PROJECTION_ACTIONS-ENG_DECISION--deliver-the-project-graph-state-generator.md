---
atom_id: CA-D-055
ref_id: CA-D-055
container:
  scope_unit: CA-SU-37
role: Delivery
form: Eng Decision
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Output Publication"
tier: 2
relations:
  delivery_for:
  - CA-R-1070
status: Active
version: 22
updated_at: 2026-11-02 19:46:47 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: PROJECTION_ACTIONS
claim_target_scope_unit: PROJECTION_ACTIONS
---
# Deliver the Project Graph State generator

the canonical source carrier for `GENERATE_PROJECT_GRAPH_STATE` is `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/GENERATE_PROJECT_GRAPH_STATE/generate_project_graph_state.py`. It exposes mutation-free description **and** dry-run modes, writes both current Scope Unit Graph Projections **only** with explicit apply through the selected installed Tool release, **and** owns no projected authority.
