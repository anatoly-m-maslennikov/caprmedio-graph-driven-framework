---
cce_version: cce_1
cce_form: serialization
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery/Git Commits
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan'
version: 21
updated_at: 2026-10-27 19:59:23 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
content_role: Delivery
current_scope_unit: CORE_EXTENSIONS
status: Active
author: Anatoly Maslennikov
atom_id: CA-D-334
type: Eng Decision
tier: 1
---
# Serialize Governed Change Commit Messages

**every** Git Commit message created by a CAPRMEDIO Tool **must** be the deterministic one-line Projection of exactly one sealed Git-effect action: a real-change action uses `<initiative-summary> | <CHANGE_CLASS> | <affected-subject>`, **where** the Initiative summary is derived from the governing human Plan, Task, **or** ephemeral session task; a Journal-only batch uses `JOURNAL BATCH | APPEND | <journal-batch-id>`. A real-change message **must not** use a technical parent **in** place of the Initiative summary, **and** neither message class **may** impersonate **or** be combined with the other.
