---
subject_scopes:
- runtime
version: 15
updated_at: 2026-10-24 10:48:25 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
  - CA-M-261
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: SKILLS
status: Archived
atom_id: CA-R-564@15
type: Rule
tier: 1
subjects:
  governs: Subject/Engineering/Runtime
  depends_on: []
---
# Use one portable shared Skill runtime

**all** CAPRMEDIO Skills for one agent host invoke one versioned portable shared runtime that deterministically resolves the owning project, project-local governance, routing, **and** required session **or** Journal setup; thin wrappers duplicate no shared mechanics **and** fail closed **when** the runtime boundary cannot be resolved.
