---
cce_version: cce_1
cce_form: method
version: 20
updated_at: 2026-10-27 19:59:41 +0400
relations:
  child_of:
  - CA-M-261
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect Authorization
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Method'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Delivery'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-M-266
status: Active
content_role: Method
author: Anatoly Maslennikov
current_scope_unit: caprmedio
type: Implementation Method
tier: 2
---
# Follow the Operator-selected implementation mode

**to** implement within a Task, follow the Operator-selected mode: evaluate **and** fix, full rebuild, refactoring, **or** another authorized approach. keep the selected mode within the Task permissions **and** governing RMED; permission for a full rebuild **must not** be inferred from an evaluation-and-fix request. the reconstruction equivalence governed by CA-M-262 applies regardless of mode **and** does **not** require identical code **or** a no-change rerun.
