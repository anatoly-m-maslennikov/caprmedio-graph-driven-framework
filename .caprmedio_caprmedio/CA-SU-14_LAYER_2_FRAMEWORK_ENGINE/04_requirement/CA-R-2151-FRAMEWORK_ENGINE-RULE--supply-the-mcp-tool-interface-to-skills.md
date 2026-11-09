---
atom_id: CA-R-2151
ref_id: CA-R-2151
container:
  scope_unit: CA-SU-14
role: Requirement
form: Rule
topics:
  {"main_subject": "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication <+ Interface Contracts", "dependencies": ["Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Interaction"]}
tier: 1
relations:
  child_of:
  - CA-R-881
  realization_input:
  - ./PROGRAMMATIC/MCP
status: Active
version: 17
updated_at: 2026-10-27 20:00:08 +0400
subject_scopes:
- scope-topology
semantic_shape: relational
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
author: Anatoly Maslennikov
current_scope_unit: FRAMEWORK_ENGINE
---
## Summary

Supply the MCP Tool interface to SKILLS

## Claim

### Prose Claim

MCP supplies SKILLS with the current generated discovery **and** invocation interface for active Tools. Skills select **and** use that interface **without** redefining Tool behavior, while MCP preserves each Tool's identity, accepted inputs, structured outputs, **and** failure meaning.
