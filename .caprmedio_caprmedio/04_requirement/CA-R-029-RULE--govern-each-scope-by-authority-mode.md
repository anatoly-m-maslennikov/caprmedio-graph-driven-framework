---
version: 30
updated_at: 2026-10-27 19:59:49 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  depends_on:
  - CA-R-1430
  child_of:
  - CA-R-1421
  - CA-M-005
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings.Authority Modes
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Method'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Delivery'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings.Authority Modes
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
cce_version: cce_1
cce_form: obligation
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: caprmedio
status: Active
atom_id: CA-R-029
type: Rule
tier: 1
---
# Govern each scope by authority mode

the caprmedio Project **must** use the effective Authority Mode for the Project **and** **every** configured Scope Unit under CA-R-1430:

- Framework Instance Settings selects the Project mode **and** the default Scope Unit mode.
- a Scope Unit's explicit override comes **only** from its authoritative Project Structure declaration; an omitted override uses the effective Framework Instance setting.

mode selection **must not** weaken active-authority consistency.
