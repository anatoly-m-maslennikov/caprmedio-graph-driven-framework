---
subject_scopes:
- scope-topology
version: 17
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  depends_on:
  - CA-D-359
  - CA-D-364
  child_of:
  - CA-R-622
current_scope_unit: PROJECT_CONFIGURATION
status: Active
atom_id: CA-R-621
tier: 2
subjects:
  active: Carrier/File
claim_target_scope_unit: caprmedio
role: Requirement
form: Rule
---
## Summary
Use settings locations defined by the Core Meta-Model

## Claim

the caprmedio Implementation **must** resolve both Settings Artifacts through the Core Meta-Model Carrier rules CA-D-359 **and** CA-D-364 **without** defining a Project-specific competing location.
