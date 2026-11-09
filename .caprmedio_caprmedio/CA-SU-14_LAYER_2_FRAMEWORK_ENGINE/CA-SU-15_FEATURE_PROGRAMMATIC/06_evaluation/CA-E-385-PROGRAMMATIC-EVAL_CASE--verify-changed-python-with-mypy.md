---
atom_id: CA-E-385
ref_id: CA-E-385
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Static Analysis"
  dependencies:
  - "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Static Analysis"
tier: 6
relations:
  evaluation_for:
  - CA-M-427
  - CA-E-540
  derived_from:
  - CA-A-053
status: Active
version: 21
updated_at: 2026-10-27 19:59:34 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Verify changed Python with Mypy

## Claim checked

new Python passes the strict admitted Mypy profile **and** changed Python does **not**
regress below its passing baseline.

## Test case

add one incompatible return type **and** one unexplained broad suppression **to** a
changed target **in** the admitted Mypy set.

## Acceptance criteria

pass **only** **when** both defects are reported **and** the target is rejected.

## Failure disposition

reject the changed target **until** types agree **or** a narrow explained suppression
is accepted.

## Sources

- [Mypy: strict mode](https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-strict)
- [CA-M-427 — Use Mypy for static Python type checking](../05_method/CA-M-427-PROGRAMMATIC-ENG_POLICY--use-mypy-for-static-python-type-checking.md)
