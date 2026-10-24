---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Engineering/Programming Language Selection
  depends_on: []
version: 19
updated_at: 2026-10-24 02:14:24 +0400
relations:
  evaluation_for:
  - CA-M-415
  derived_from:
  - CA-A-053
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-255
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Active
author: Anatoly Maslennikov
tier: 4
type: Eval Case
---
# Verify installed selected-runtime component

## Claim checked

one delivered installable PROGRAMMATIC component runs under the runtime **and**
dependency selections owned by accepted Methods from the carrier placed **and**
encoded by its Delivery.

## Applicable conditions

apply **only** **when** a lower-Scope Delivery declares the component installable.
this case does **not** establish a platform-support claim.

## Test case

install one delivered component from its Delivery-owned carrier, invoke its
declared entry boundary, **and** compare the observed runtime **and** dependencies with
their Method-owned selections **and** materializations.

## Acceptance criteria

pass **only** **when** the installed carrier reaches its declared entry boundary,
the observed runtime **and** dependencies match their applicable Method-owned
selections **and** materializations, **and** no undeclared runtime **or** dependency is
required. the carrier **must not** claim selection authority.

## Failure disposition

reject the installation claim **and** return the component **to** its Delivery owner.

## Sources

- [CA-M-415 — Implement PROGRAMMATIC components in Python](../05_method/CA-M-415-PROGRAMMATIC-STANDARD-ENG_POLICY--implement-programmatic-components-in-python.md)
