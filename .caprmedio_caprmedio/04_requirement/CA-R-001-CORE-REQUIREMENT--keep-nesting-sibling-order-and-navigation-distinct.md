---
version: 14
updated_at: 2026-10-24 02:14:24 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
  - CA-M-001
  - CA-R-1407
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Project/Scope Unit topology
  depends_on:
  - Project
  - Scope Unit
  - Scope Unit/Local Order
  - Structural Level
  - Navigational Order Number
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: caprmedio
status: Active
atom_id: CA-R-001
type: Rule
tier: 1
---
# Keep nesting, sibling order, and navigation distinct

the Project Scope Unit topology **must** distinguish Structural Level as nesting depth, Local Order as the order of ordered siblings under the same parent, **and** Navigational Order Number as presentation; dependency permission **must** follow its relation-family authority **and** **must not** be created by a filename number, nesting position, **or** the assumption that **every** Scope Unit is a Layer.
