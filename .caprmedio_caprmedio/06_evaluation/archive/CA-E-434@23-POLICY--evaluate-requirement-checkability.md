---
cce_version: cce_1
cce_form: evaluation
version: 23
updated_at: 2026-10-31 15:50:06 +0400
relations:
  child_of:
  - CA-E-001
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement'
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Evaluation'
  - Entity/Object/Continuant/Governing Objects/Atom
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-434@23
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: caprmedio
type: Eval Policy
tier: 1
---
# Evaluate Requirement checkability

**when** an accepted Requirement is used **to** govern work **or** evaluate a result, its checkability Evaluation **must** return `pass` **if** the available evidence identifies **all** of the following:

- recoverable inputs for checking the Requirement;
- a recoverable check procedure;
- a recoverable interpretation that yields **=1** result **in** (`pass`, `fail`).

**if** **any** of these conditions is missing, the checkability Evaluation **must** return `fail`. satisfying them does **not** require a separate Evaluation Atom **unless** applicable authority requires that Atom for the particular case under CAPRMEDIO-META-REQU-124; an independently governed Evaluation Claim still follows the Atom boundary rules.
