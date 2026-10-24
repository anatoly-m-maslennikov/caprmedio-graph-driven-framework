---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Engineering/Source Check Adoption
  depends_on:
  - Subject/Domain/Node/Continuant/History/Journal.Record
version: 20
updated_at: 2026-10-24 02:14:24 +0400
relations:
  evaluation_for:
  - CA-M-420
  - CA-E-539
  - CA-E-540
  derived_from:
  - CA-A-053
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-270
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Active
author: Anatoly Maslennikov
tier: 6
type: Eval Case
---
# Verify changed-code adoption ratchet

## Claim checked

one changed **or** new PROGRAMMATIC target within an admitted automation **or** typing
capability does **not** regress below its current passing boundary.

## Applicable conditions

apply **when** a component changes source within an admitted typing, formatting,
linting, **or** behavioral-check capability. unadmitted capability selection is
**not** applicable.

## Test case

evaluate one changed target against its current admitted passing boundary.

## Acceptance criteria

pass **only** **when** the target meets the current Method-owned boundary **or** has one
accepted Method-owned bounded exception. Configuration **and** Implementation **must**
materialize that selection, Delivery **must** govern its carrier, **and** Journal Records
**must** carry evidence of the actual result **without** becoming another selection authority.

## Failure disposition

reject the ratchet claim **and** return the target **to** its change owner.

## Sources

- [CA-M-420 — Ratchet typing and automation adoption](../05_method/CA-M-420-PROGRAMMATIC-STANDARD-ENG_POLICY--ratchet-typing-and-automation-adoption.md)
