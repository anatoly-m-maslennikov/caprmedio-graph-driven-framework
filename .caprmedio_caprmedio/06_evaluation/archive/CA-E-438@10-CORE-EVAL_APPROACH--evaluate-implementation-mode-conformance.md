---
cce_version: cce_1
cce_form: evaluation
version: 10
updated_at: 2026-10-24 00:51:05 +0400
relations:
  child_of:
  - CA-E-001
  evaluation_for:
  - CA-M-266
  - CA-M-262
subjects:
  governs: Project/Implementation/mode selection
  depends_on:
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Spec
  - 'Atom/Content Role: Plan/Type: Task'
  - 'Atom/Content Role: Implementation'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Method'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery'
  - Subject/Domain/Node/Continuant/Project
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-438@10
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: caprmedio
---
# Evaluate implementation mode conformance

the implementation mode Evaluation **must** return `fail` **if**

- execution replaces the Operator-selected mode **without** authorization,
- treats an evaluation-and-fix request as permission for a full rebuild,
- exceeds Task permissions,
- **or** exempts the selected mode from the governing RMED.

authorized rewriting **or** different source-code bytes **must not** by themselves cause failure **when** reconstruction equivalence under CA-M-262 is preserved.
