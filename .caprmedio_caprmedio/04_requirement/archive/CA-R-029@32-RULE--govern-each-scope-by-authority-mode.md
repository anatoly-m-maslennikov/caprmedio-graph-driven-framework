---
version: 32
updated_at: 2026-10-29 07:45:26 +0400
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
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Authority Modes
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Method'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Evaluation'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Delivery'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations'
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Authority Modes
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Structure
  - Entity/Object/Continuant/Structural Unit/Scope Unit
cce_version: cce_1
cce_form: obligation
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: caprmedio
status: Archived
atom_id: CA-R-029@32
type: Rule
tier: 1
---
## Summary
Govern each scope by authority mode

## Claim

the caprmedio Project **must** use the effective Authority Mode for the Project **and** **every** configured Scope Unit under CA-R-1430:

- Framework Instance Settings selects the Project mode **and** the default Scope Unit mode.
- a Scope Unit's explicit override comes **only** from its authoritative Project Structure declaration; an omitted override uses the effective Framework Instance setting.

mode selection **must not** weaken active-authority consistency.
