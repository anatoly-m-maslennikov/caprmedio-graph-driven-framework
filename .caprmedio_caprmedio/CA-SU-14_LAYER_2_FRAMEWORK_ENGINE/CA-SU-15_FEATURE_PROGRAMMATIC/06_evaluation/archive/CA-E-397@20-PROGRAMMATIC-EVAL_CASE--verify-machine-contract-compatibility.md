---
atom_id: CA-E-397
ref_id: CA-E-397@20
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Dynamic
    Testing
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
tier: 1
relations:
  evaluation_for:
  - CA-M-166
  derived_from:
  - CA-A-053
status: Archived
version: 20
updated_at: 2026-11-05 23:05:59 +0400
carrier_destination:
  file:
    name: CA-E-397@20-PROGRAMMATIC-EVAL_CASE--verify-machine-contract-compatibility.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation/archive
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: PROGRAMMATIC
---
## Summary

Verify machine-contract compatibility

## Claim

### Prose Claim

#### Claim checked

one public machine boundary preserves structural, semantic, version, **and**
adjacent producer-consumer compatibility.

#### Test case

pass valid, missing-field, forbidden-field, wrong-type, **and** unsupported-version
fixtures from one producer **to** its supported adjacent consumer. Include
invalid arguments that must be rejected before effects, and where the boundary
supports shared paged state, delayed or reordered acknowledgements from two
clients and a snapshot larger than one page with null, Unicode and hidden values.
Use paired failures with similar human text but different structured error type,
code or state. When both restart-required and unavailable categories are
declared, include ordinary “restart required” text versus true unavailable
state.

#### Acceptance criteria

pass **only** **when** valid meaning survives, structural **and** semantic failures remain
distinct, unsupported versions are rejected, **and** the declared compatibility
promise is preserved **or** explicitly replaced. Failure classification comes
from structured type, code and state, not an arbitrary message substring; invalid
arguments have no effect before rejection. A shared page boundary keeps rows,
global counts and all value forms on one snapshot, and delayed or reordered
acknowledgements from two clients cannot mix or overwrite it.

#### Failure disposition

reject release **or** the compatibility claim **until** the boundary is restored.

#### Sources

- [JSON Schema Draft 2020-12](https://json-schema.org/draft/2020-12)
- [CA-M-166 — Preserve declared interface compatibility boundaries](../05_method/CA-M-166-PROGRAMMATIC-CORE-METHOD--preserve-declared-interface-compatibility-boundaries.md)
