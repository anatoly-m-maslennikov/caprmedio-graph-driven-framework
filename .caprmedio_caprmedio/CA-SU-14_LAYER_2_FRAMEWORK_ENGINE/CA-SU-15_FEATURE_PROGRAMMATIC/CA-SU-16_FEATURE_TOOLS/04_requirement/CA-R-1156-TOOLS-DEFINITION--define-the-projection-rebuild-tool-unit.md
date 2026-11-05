---
atom_id: CA-R-1156
ref_id: CA-R-1156
container:
  scope_unit: CA-SU-16
role: Requirement
form: Definition
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Output Publication
tier: 1
status: Active
version: 30
updated_at: 2026-11-02 19:46:47 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Define the PROJECTION_REBUILD Tool unit

`PROJECTION_REBUILD` **must** be one Doer Tool owned immediately by `TOOLS` as an `unordered_unit` at Structural level `4`, addressed by `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/PROJECTION_REBUILD`, **and** realized under `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/PROJECTION_REBUILD/`; it derives the complete affected Projection set from changed source frontiers, orders rebuilds by declared dependencies, previews **every** output effect, materializes **only** explicitly approved outputs, **and** verifies currentness **and** idempotence **after** publication.
