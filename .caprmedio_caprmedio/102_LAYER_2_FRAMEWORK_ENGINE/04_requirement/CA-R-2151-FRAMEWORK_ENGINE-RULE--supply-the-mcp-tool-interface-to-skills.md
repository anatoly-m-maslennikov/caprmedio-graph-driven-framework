---
subject_scopes:
- scope-topology
semantic_shape: relational
version: 16
updated_at: 2026-10-27 06:04:45 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relational_endpoints:
  controller:
    scope_unit: ./AGENTIC/SKILLS
    content_role: requirement
  followers:
  - scope_unit: ./PROGRAMMATIC/MCP
    content_roles:
    - delivery
relations:
  child_of:
  - CA-R-881
  realization_input:
  - ./PROGRAMMATIC/MCP
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: FRAMEWORK_ENGINE
status: Active
atom_id: CA-R-2151
tier: 1
type: Rule
subjects:
  governs: Subject/Graph Node/Engineering/Architecture/Communication
  depends_on:
  - Subject/Graph Node/UX/CAPRMEDIO Skill and MCP Entry Interface
---
# Supply the MCP Tool interface to SKILLS

MCP supplies SKILLS with the current generated discovery **and** invocation interface for active Tools. Skills select **and** use that interface **without** redefining Tool behavior, while MCP preserves each Tool's identity, accepted inputs, structured outputs, **and** failure meaning.
