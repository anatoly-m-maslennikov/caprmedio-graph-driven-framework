---
atom_id: CA-E-378
ref_id: CA-E-378
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
tier: 5
relations:
  evaluation_for:
  - CA-M-429
  derived_from:
  - CA-A-053
status: Active
version: 22
updated_at: 2026-10-27 19:59:34 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Run an installed Tool without uv

## Claim checked

one installed CAPRMEDIO Tool executes from `.caprmedio_runtime/tools` **without** uv, a
project virtual environment, **or** another dependency outside the selected
runtime release.

## Test case

invoke one installed Tool **in** a clean process **where** uv **and** the project virtual
environment are unavailable.

## Acceptance criteria

pass **only** **when** the Tool reaches its declared entry boundary using solely its
installed carrier **and** admitted host prerequisites.

## Failure disposition

reject the installed-runtime claim **until** the external workflow dependency is
removed.

## Sources

- [CA-M-429 — Use uv as the default Python workflow frontend](../05_method/CA-M-429-PROGRAMMATIC-ENG_POLICY--use-uv-as-the-default-python-workflow-frontend.md)
