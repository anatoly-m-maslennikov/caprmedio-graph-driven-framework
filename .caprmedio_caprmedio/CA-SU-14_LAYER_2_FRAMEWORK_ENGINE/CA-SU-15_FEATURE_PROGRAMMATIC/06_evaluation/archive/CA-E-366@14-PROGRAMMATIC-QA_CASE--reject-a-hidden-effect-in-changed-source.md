---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Engineering/Effect Boundary
  depends_on:
  - Subject/Engineering/State Ownership
version: 14
updated_at: 2026-10-24 00:38:25 +0400
relations:
  evaluation_for:
  - CA-M-425
  derived_from:
  - CA-A-053
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-366@14
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Archived
author: Anatoly Maslennikov
tier: 3
---
# Reject a hidden effect in changed source

## Claim checked

one changed effect function declares its complete effect boundary **or** allocates
persistent ownership **to** an object.

## Test case

evaluate one changed function that reads the process environment implicitly
**before** writing its declared target.

## Acceptance criteria

pass **only** **when** the function is rejected **until** the environment observation is
an explicit input **or** an owned adapter boundary.

## Failure disposition

block the changed unit **until** the hidden observation is removed.

## Sources

- [CA-M-425 — Separate deterministic transformations from effects and lifecycle](../05_method/CA-M-425-PROGRAMMATIC-STANDARD-ENG_POLICY--separate-deterministic-transformations-from-effects-and-lifecycle.md)
