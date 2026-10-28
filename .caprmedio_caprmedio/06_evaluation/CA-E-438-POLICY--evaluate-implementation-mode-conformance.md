---
cce_version: cce_1
cce_form: evaluation
version: 21
updated_at: 2026-10-27 19:59:35 +0400
relations:
  child_of:
  - CA-E-001
  evaluation_for:
  - CA-M-266
  - CA-M-262
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Method'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Delivery'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-438
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: caprmedio
type: Policy
tier: 3
---
# Evaluate implementation mode conformance

the implementation mode Evaluation **must** return `fail` **if**

- execution replaces the Operator-selected mode **without** authorization,
- treats an evaluation-and-fix request as permission for a full rebuild,
- exceeds Task permissions,
- **or** exempts the selected mode from the governing RMED.

authorized rewriting **or** different source-code bytes **must not** by themselves cause failure **when** reconstruction equivalence under CA-M-262 is preserved.
