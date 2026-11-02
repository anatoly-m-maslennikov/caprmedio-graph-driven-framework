---
cce_version: cce_1
cce_form: evaluation
version: 22
updated_at: 2026-10-29 07:17:15 +0400
relations:
  child_of:
  - CA-E-001
  evaluation_for:
  - CA-M-266
  - CA-M-262
subjects:
  governs: Entity/Object/Continuant/Package/Project Implementation
  depends_on:
  - Entity/Object/Continuant/Actor/Operator
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan'
  - Entity/Object/Continuant/Package/Project Implementation
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Evaluation'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Method'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Delivery'
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-438@22
status: Archived
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
