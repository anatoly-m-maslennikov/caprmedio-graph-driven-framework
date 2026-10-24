---
version: 15
updated_at: 2026-10-24 01:33:47 +0400
relations:
  child_of:
  - CA-M-006
  - CA-E-001
  evaluation_for:
  - CAPRMEDIO-REQU-026
  - CAPRMEDIO-REQU-706
  - CA-R-1551
subjects:
  governs: Project/Principle alignment
  depends_on:
  - Structural Level
  - Atom
  - Project
  - 'Atom/Local Tier: Principle'
  - Operator
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
content_role: Evaluation
current_scope_unit: caprmedio
status: Archived
atom_id: CA-E-655@15
---
# Principle-first alignment

## Claim checked

for **every** selected Structural Level **and** given scope, the complete active Atom set is aligned with **every** active Project Principle.

## Check

load the complete active Project Principle set first, resolve the Structural Level **and** scope, collect the complete active Atom set, including Methodology source Atoms within the selected Scope, **and** evaluate **every** Atom against **every** Principle **before** applying lower-tier authority.

## Acceptance

pass **only** **when** no Atom conflicts with a Project Principle **and** no lower-tier interpretation weakens **or** overrides one.

## Failure

report **every** conflicting Atom **and** Principle pair; route **every** conflict between active Project Principles **to** the Operator under `CA-R-1551`.
