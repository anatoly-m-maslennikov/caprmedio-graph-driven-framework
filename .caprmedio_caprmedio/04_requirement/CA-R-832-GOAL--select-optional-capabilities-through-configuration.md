---
cce_version: cce_1
cce_form: obligation
version: 29
updated_at: 2026-10-27 06:04:45 +0400
relations:
  child_of:
  - CA-R-1421
  - CA-R-815
  - CA-M-006
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Governing Configuration
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Product/Extension
  - 'Subject/Graph Node/Product: CAPRMEDIO Framework'
  - Subject/Graph Node/Domain/Continuant/Project.Framework Settings
  - Subject/Graph Node/Domain/Continuant/Scope Unit//PROJECT_CONFIGURATION
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-832
status: Active
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: caprmedio
type: Goal
tier: 5
claim_target_scope_unit: FRAMEWORK_ENGINE
---
# Select optional capabilities through Configuration

the CAPRMEDIO Framework Instance **must** provide configuration capabilities **to** select, combine, parameterize, **or** disable available optional canonical **and** Extension capabilities **only** within declared configuration boundaries **and** **without** redefining governed meanings.

current Extension activation **and** selected Extension revisions use their authoritative Framework Instance Settings under CA-R-1207; this capability does **not** make Project Configuration Atoms a second owner of those selections.
