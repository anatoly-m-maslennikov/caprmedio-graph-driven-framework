---
subject_scopes:
- scope-topology
version: 13
updated_at: 2026-10-27 20:00:10 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  depends_on:
  - CA-D-359
  - CA-D-364
  child_of:
  - CA-R-622
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
status: Active
atom_id: CA-R-621
type: Rule
tier: 2
subjects:
  governs: Subject/CAPRMEDIO/Carrier/File
  depends_on: []
claim_target_scope_unit: caprmedio
---
# Use settings locations defined by the Core Meta-Model

the caprmedio Implementation **must** resolve both Settings Artifacts through the Core Meta-Model Carrier rules CA-D-359 **and** CA-D-364 **without** defining a Project-specific competing location.
