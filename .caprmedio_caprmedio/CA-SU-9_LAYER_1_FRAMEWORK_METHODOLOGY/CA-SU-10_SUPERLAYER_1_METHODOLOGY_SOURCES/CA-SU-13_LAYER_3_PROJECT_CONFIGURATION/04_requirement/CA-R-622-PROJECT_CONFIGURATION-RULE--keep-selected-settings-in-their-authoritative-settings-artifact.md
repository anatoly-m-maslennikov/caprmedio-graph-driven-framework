---
version: 34
updated_at: 2026-11-02 18:35:20 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  depends_on:
  - CA-R-1750
  - CA-R-2532
  - CA-R-1402@27
  child_of:
  - CA-M-446
  - CA-R-1421
cce_version: cce_1
cce_form: obligation
subjects:
  active: CAPRMEDIO_MODEL <+ Project.Settings
  passive:
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Term//Artifact
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Data Handling <+ Source Selection
current_scope_unit: PROJECT_CONFIGURATION
status: Active
atom_id: CA-R-622
tier: 1
claim_target_scope_unit: caprmedio
role: Requirement
form: Rule
---
## Summary
Keep selected settings in their authoritative Settings Artifact

## Claim

the CAPRMEDIO Framework Instance serving caprmedio **must** consume Project Settings **and** Framework Instance Settings according **to** Core Meta-Model authority under CA-R-1750, **without** redefining their purpose, locations, **or** selected values **in** Project Atoms.
