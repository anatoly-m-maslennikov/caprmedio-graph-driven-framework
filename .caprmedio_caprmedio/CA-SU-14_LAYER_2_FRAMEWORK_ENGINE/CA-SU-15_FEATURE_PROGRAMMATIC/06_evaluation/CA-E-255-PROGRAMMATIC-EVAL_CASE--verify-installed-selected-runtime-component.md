---
atom_id: CA-E-255
ref_id: CA-E-255
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
tier: 4
relations:
  evaluation_for:
  - CA-M-415
  derived_from:
  - CA-A-053
status: Active
version: 26
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
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

- [CA-M-415 — Implement PROGRAMMATIC components in Python](../05_method/CA-M-415-PROGRAMMATIC-ENG_POLICY--implement-programmatic-components-in-python.md)
