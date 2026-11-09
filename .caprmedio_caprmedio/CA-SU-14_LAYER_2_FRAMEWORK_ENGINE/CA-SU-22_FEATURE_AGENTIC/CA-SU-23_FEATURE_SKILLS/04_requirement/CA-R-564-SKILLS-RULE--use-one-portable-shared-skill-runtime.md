---
atom_id: CA-R-564
ref_id: CA-R-564
container:
  scope_unit: CA-SU-23
role: Requirement
form: Rule
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Component Structure"
tier: 1
relations:
  child_of:
  - CA-M-261
status: Active
version: 21
updated_at: 2026-11-02 19:44:26 +0400
subject_scopes:
- runtime
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: SKILLS
---
## Summary

Use one portable shared Skill runtime

## Claim

### Prose Claim

**all** CAPRMEDIO Skills for one agent host invoke one versioned portable shared runtime that deterministically resolves the owning project, project-local governance, routing, **and** required session **or** Journal setup; thin wrappers duplicate no shared mechanics **and** fail closed **when** the runtime boundary cannot be resolved.
