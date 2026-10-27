---
cce_version: cce_1
cce_form: obligation
version: 28
updated_at: 2026-10-26 05:59:45 +0400
relations:
  child_of:
  - CA-R-1421
  - CA-R-815
  - CA-M-006
subjects:
  governs: Subject/Graph Node/Engineering/Configuration/Tool Selection and Activation Precedence
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Engineering/Extension
  - Subject/Graph Node/Engineering/Framework Instance
  - Subject/Graph Node/Domain/Continuant/Project.Framework Settings
  - Subject/Graph Node/Domain/Continuant/Scope Unit//PROJECT_CONFIGURATION
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-832@28
status: Archived
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
