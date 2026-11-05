---
subject_scopes:
- runtime
version: 21
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
  - CA-M-261
author: Anatoly Maslennikov
role: Requirement
current_scope_unit: SKILLS
status: Active
atom_id: CA-R-564
ref_id: CA-R-564
form: Rule
tier: 1
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component
    Structure
container:
  scope_unit: CA-SU-23
---
# Use one portable shared Skill runtime

**all** CAPRMEDIO Skills for one agent host invoke one versioned portable shared runtime that deterministically resolves the owning project, project-local governance, routing, **and** required session **or** Journal setup; thin wrappers duplicate no shared mechanics **and** fail closed **when** the runtime boundary cannot be resolved.
