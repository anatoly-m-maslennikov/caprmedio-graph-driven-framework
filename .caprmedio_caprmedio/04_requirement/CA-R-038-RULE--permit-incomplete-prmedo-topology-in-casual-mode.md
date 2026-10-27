---
subject_scopes:
- requirement-topology
version: 12
updated_at: 2026-10-25 17:32:27 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
  - CA-R-029
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: caprmedio
status: Active
atom_id: CA-R-038
type: Rule
tier: 2
subjects:
  governs: Subject/Graph Rule
  depends_on: []
---
# Permit incomplete PRMEDO topology in casual mode

a scope **in** casual authority mode **may** contain active PRMEDO Core **and** Standard Atoms **without** permitted active parents **and** **may** omit permitted active children.
