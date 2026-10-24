---
subjects:
  governs: feature-boundary
  depends_on: []
version: 13
updated_at: 2026-10-24 02:14:24 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1164@13
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Definition
tier: 1
---
# Define the GENERATE_PROJECT_GRAPH_STATE Tool unit

`GENERATE_PROJECT_GRAPH_STATE` **must** be one projection Doer Tool owned immediately by `TOOLS` as an `unordered_unit` at Structural level `4`, addressed by `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_PROJECT_GRAPH_STATE`, **and** realized under `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/GENERATE_PROJECT_GRAPH_STATE/`; it derives the current Project Scope Unit Graph **and** Sources Projections from admitted authority **without** owning the projected facts.
