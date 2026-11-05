---
cce_version: cce_1
cce_form: evaluation
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Dynamic
    Testing
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
version: 19
updated_at: 2026-10-27 19:59:34 +0400
relations:
  evaluation_for:
  - CA-M-166
  derived_from:
  - CA-A-053
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-397
ref_id: CA-E-397
status: Archived
role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: PROGRAMMATIC
form: Eval Case
tier: 1
container:
  scope_unit: CA-SU-15
carrier_destination:
  file:
    name: CA-E-397@19-PROGRAMMATIC-EVAL_CASE--verify-machine-contract-compatibility.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation/archive
---
# Verify machine-contract compatibility

## Claim checked

one public machine boundary preserves structural, semantic, version, **and**
adjacent producer-consumer compatibility.

## Test case

pass valid, missing-field, forbidden-field, wrong-type, **and** unsupported-version
fixtures from one producer **to** its supported adjacent consumer.

## Acceptance criteria

pass **only** **when** valid meaning survives, structural **and** semantic failures remain
distinct, unsupported versions are rejected, **and** the declared compatibility
promise is preserved **or** explicitly replaced.

## Failure disposition

reject release **or** the compatibility claim **until** the boundary is restored.

## Sources

- [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12)
- [CA-M-166 — Preserve declared interface compatibility boundaries](../05_method/CA-M-166-PROGRAMMATIC-CORE-METHOD--preserve-declared-interface-compatibility-boundaries.md)
