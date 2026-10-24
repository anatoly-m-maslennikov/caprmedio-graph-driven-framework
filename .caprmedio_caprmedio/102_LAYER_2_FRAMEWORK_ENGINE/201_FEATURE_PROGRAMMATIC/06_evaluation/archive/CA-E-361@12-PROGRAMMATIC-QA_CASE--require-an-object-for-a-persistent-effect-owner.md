---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Engineering/Effect Boundary
  depends_on:
  - Subject/Engineering/State Ownership
version: 12
updated_at: 2026-10-23 23:58:37 +0400
relations:
  evaluation_for:
  - CA-M-425
  derived_from:
  - CA-A-053
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-361@12
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Archived
author: Anatoly Maslennikov
---
# Require an object for a persistent effect owner

## Claim checked

one effect that owns identity, state, an invariant, a resource, a lifecycle, **or**
a replaceable adapter across calls is applied through a specifically named
object method.

## Test case

evaluate one standalone function that acquires a resource **and** retains its
lifecycle state for a later call.

## Acceptance criteria

pass **only** **when** the function is rejected **and** the persistent responsibility is
allocated **to** one object with explicit acquisition, use, **and** release boundaries.

## Failure disposition

reject the effect boundary **until** its persistent owner is explicit.

## Sources

- [CA-M-425 — Separate deterministic transformations from effects and lifecycle](../05_method/CA-M-425-PROGRAMMATIC-STANDARD-ENG_POLICY--separate-deterministic-transformations-from-effects-and-lifecycle.md)
