---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Graph Node/Engineering/Effect Boundary
  depends_on:
  - Subject/Graph Node/Engineering/State Ownership
version: 18
updated_at: 2026-10-25 17:32:27 +0400
relations:
  evaluation_for:
  - CA-M-425
  derived_from:
  - CA-A-053
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-360@18
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Archived
author: Anatoly Maslennikov
tier: 5
type: Eval Case
---
# Admit a bounded one-shot effect function

## Claim checked

one bounded one-shot effect **may** be a function **when** **every** dependency **and**
boundary is explicit **and** no identity **or** ownership persists across calls.

## Test case

evaluate one specifically named function that applies one file effect from an
explicit target **and** dependency **and** returns a typed outcome **without** retained
state.

## Acceptance criteria

pass **only** **when** the function's target, dependency, input, outcome, **and** failure
boundary are explicit **and** it owns no state, invariant, resource, lifecycle, **or**
adapter across calls.

## Failure disposition

reject the function **or** allocate an object **when** **any** persistent ownership is
required.

## Sources

- [CA-M-425 — Separate deterministic transformations from effects and lifecycle](../05_method/CA-M-425-PROGRAMMATIC-ENG_POLICY--separate-deterministic-transformations-from-effects-and-lifecycle.md)
