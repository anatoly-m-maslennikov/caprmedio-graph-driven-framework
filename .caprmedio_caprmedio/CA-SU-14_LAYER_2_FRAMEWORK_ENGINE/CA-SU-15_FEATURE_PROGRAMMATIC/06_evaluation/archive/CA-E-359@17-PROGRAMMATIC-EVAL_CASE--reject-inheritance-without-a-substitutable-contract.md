---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Engineering/State Ownership
  depends_on: []
version: 17
updated_at: 2026-10-24 11:58:20 +0400
relations:
  evaluation_for:
  - CA-M-408
  derived_from:
  - CA-A-053
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-359@17
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Archived
author: Anatoly Maslennikov
tier: 5
type: Eval Case
---
# Reject inheritance without a substitutable contract

## Claim checked

one PROGRAMMATIC inheritance relationship exists **only** for a stable
substitutable subtype contract.

## Test case

evaluate one changed subclass that inherits behavior for code reuse but cannot
replace its base under the base contract.

## Acceptance criteria

pass **only** **when** the inheritance is rejected **and** the behavior is expressed by a
function, module, **or** composed collaborator.

## Failure disposition

reject the subtype boundary **until** substitutability is demonstrated **or**
inheritance is removed.

## Sources

- [CA-M-408 — Allocate owned state and lifecycle to objects](../05_method/CA-M-408-PROGRAMMATIC-ENG_POLICY--allocate-owned-state-and-lifecycle-to-objects.md)
