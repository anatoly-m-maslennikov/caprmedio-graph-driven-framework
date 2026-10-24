---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "subtype-contract"
  depends_on:
    - "programmatic software"
version: 9
updated_at: "2026-10-21T23:29:13+00:00"
relations:
  evaluation_for:
    - CA-M-408
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-359
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Active
author: Anatoly Maslennikov
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

- [CA-M-408 — Allocate owned state and lifecycle to objects](../05_method/CA-M-408-PROGRAMMATIC-STANDARD-IMPLEMENTATION_METHOD--allocate-owned-state-and-lifecycle-to-objects.md)
