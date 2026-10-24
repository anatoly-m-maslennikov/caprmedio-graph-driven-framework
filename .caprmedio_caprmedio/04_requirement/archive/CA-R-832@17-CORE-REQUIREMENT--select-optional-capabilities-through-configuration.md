---
cce_version: cce_1
cce_form: obligation
version: 17
updated_at: 2026-10-24 01:28:26 +0400
relations:
  child_of:
  - CA-R-1421
  - CA-R-815
  - CA-M-006
  relates_to:
  - CA-R-1207
subjects:
  governs: Configuration
  depends_on:
  - Subject/Domain/Node/Continuant/Project
  - Extension
  - CAPRMEDIO Framework Instance
  - Subject/Domain/Node/Continuant/Project.Framework Settings
  - Project Configuration
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-832@17
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: caprmedio
type: Goal
---
# Select optional capabilities through Configuration

the CAPRMEDIO Framework Instance **must** provide configuration capabilities **to** select, combine, parameterize, **or** disable available optional canonical **and** Extension capabilities **only** within declared configuration boundaries **and** **without** redefining governed meanings.

current Extension activation **and** selected Extension revisions use their authoritative Framework Instance Settings under CA-R-1207; this capability does **not** make Project Configuration Atoms a second owner of those selections.
