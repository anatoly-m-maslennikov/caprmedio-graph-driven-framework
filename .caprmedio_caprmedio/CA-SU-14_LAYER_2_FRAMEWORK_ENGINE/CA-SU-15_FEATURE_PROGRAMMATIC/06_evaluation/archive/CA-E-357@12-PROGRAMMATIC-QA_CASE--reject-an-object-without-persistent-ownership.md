---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Engineering/State Ownership
  depends_on: []
version: 12
updated_at: 2026-10-23 23:58:37 +0400
relations:
  evaluation_for:
  - CA-M-408
  derived_from:
  - CA-A-053
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-357@12
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Archived
author: Anatoly Maslennikov
---
# Reject an object without persistent ownership

## Claim checked

one PROGRAMMATIC object is admitted **only** **when** it requires identity across calls
**and** owns state, an invariant, a resource, a lifecycle, **or** a replaceable
adapter.

## Test case

evaluate one changed object that **only** wraps a bounded one-shot effect **and** owns
no responsibility across calls.

## Acceptance criteria

pass **only** **when** the object is rejected **and** the effect is allocated **to** a
specifically named bounded function.

## Failure disposition

reject the object **until** persistent ownership is demonstrated **or** the wrapper is
replaced by a function.

## Sources

- [CA-M-408 — Allocate owned state and lifecycle to objects](../05_method/CA-M-408-PROGRAMMATIC-STANDARD-ENG_POLICY--allocate-owned-state-and-lifecycle-to-objects.md)
