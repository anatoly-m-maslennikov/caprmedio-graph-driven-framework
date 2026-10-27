---
version: 26
updated_at: 2026-10-27 06:04:45 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  depends_on:
  - CA-R-1750
  - CA-R-1738
  - CA-R-1402
  child_of:
  - CA-M-002
  - CA-R-1421
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Project.Settings
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Domain/Continuant/Project.Framework Settings
  - Subject/Graph Node/Domain/Continuant/Term//Artifact
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Engineering/Data Handling/Source Selection
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
status: Active
atom_id: CA-R-622
type: Rule
tier: 1
claim_target_scope_unit: caprmedio
---
# Keep selected settings in their authoritative Settings Artifact

the CAPRMEDIO Framework Instance serving caprmedio **must** consume Project Settings **and** Framework Instance Settings according **to** Core Meta-Model authority under CA-R-1750, **without** redefining their purpose, locations, **or** selected values **in** Project Atoms.
