---
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Data Handling/Output Publication
  depends_on: []
version: 18
updated_at: 2026-10-26 00:46:35 +0400
relations:
  delivery_for:
  - CA-R-1070
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-D-055@18
status: Archived
content_role: Delivery
author: Anatoly Maslennikov
current_scope_unit: PROJECTION_ACTIONS
type: Eng Decision
tier: 2
claim_target_scope_unit: PROJECTION_ACTIONS
---
# Deliver the Project Graph State generator

the canonical source carrier for `GENERATE_PROJECT_GRAPH_STATE` is `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_PROJECT_GRAPH_STATE/generate_project_graph_state.py`. It exposes mutation-free description **and** dry-run modes, writes both current Scope Unit Graph Projections **only** with explicit apply through the selected installed Tool release, **and** owns no projected authority.
