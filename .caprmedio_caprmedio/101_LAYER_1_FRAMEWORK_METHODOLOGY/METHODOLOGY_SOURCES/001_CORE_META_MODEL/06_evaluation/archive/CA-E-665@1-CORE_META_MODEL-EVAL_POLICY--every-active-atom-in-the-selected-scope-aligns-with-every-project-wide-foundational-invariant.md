---
version: 1
updated_at: 2026-10-29 23:57:07 +0400
relations:
  child_of:
  - CA-M-006
  - CA-E-001
  evaluation_for:
  - CA-R-2426
  - CA-R-706
  - CA-R-2425
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
  - Entity/Object/Continuant/Actor/Operator
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
status: Archived
atom_id: CA-E-665@1
type: Eval Policy
tier: 3
---
## Summary

Every active Atom in the selected scope aligns with every Project-wide foundational invariant

## Claim

for **every** given scope, the complete active Atom set is aligned with **every** active Project-wide foundational invariant.

## Check

perform **all** of the following in order:

1. load the complete active Project-wide foundational invariant set.
2. resolve the scope.
3. collect the complete active Atom set, including Methodology source Atoms within the selected Scope.
4. evaluate **every** collected Atom against **every** Project-wide foundational invariant **before** applying lower-tier authority.

## Acceptance

pass **only** **when** **all** of the following hold:

- no Atom conflicts with a Project-wide foundational invariant.
- no lower-tier interpretation weakens **or** overrides a Project-wide foundational invariant.

## Failure

report **every** conflicting Atom **and** Project-wide foundational invariant pair. route **every** conflict between active Project-wide foundational invariants **to** the Operator under `CA-R-2425-CORE_META_MODEL-RULE--reserve-project-wide-invariant-conflict-resolution-to-the-operator`.
