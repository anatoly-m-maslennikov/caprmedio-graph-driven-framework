---
version: 26
updated_at: 2026-10-27 19:59:38 +0400
relations:
  child_of:
  - CA-M-006
  - CA-E-001
  evaluation_for:
  - CA-R-1773
  - CA-R-706
  - CA-R-1551
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
status: Active
atom_id: CA-E-655
type: Policy
tier: 3
---
# Principle-first alignment

## Claim checked

for **every** given scope, the complete active Atom set is aligned with **every** active Project Principle.

## Check

load the complete active Project Principle set first, resolve the scope, collect the complete active Atom set, including Methodology source Atoms within the selected Scope, **and** evaluate **every** Atom against **every** Principle **before** applying lower-tier authority.

## Acceptance

pass **only** **when** no Atom conflicts with a Project Principle **and** no lower-tier interpretation weakens **or** overrides one.

## Failure

report **every** conflicting Atom **and** Principle pair; route **every** conflict between active Project Principles **to** the Operator under `CA-R-1551`.
