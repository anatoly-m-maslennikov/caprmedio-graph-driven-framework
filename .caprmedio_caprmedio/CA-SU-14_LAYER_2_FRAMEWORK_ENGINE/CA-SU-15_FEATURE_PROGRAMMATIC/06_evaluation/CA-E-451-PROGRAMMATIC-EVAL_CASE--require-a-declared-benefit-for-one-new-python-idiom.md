---
atom_id: CA-E-451
ref_id: CA-E-451
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Authoring/Code Authoring/Python Code"
tier: 5
relations:
  evaluation_for:
  - CA-M-406
  derived_from:
  - CA-A-053
status: Active
version: 22
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Require a declared benefit for one new Python idiom

## Claim checked

a runtime-dependent Python idiom is admitted **only** for a named benefit inside
the supported boundary.

## Test case

replace an immediate trusted f-string with a t-string while providing no
interpolation processor **or** other correctness, clarity, safety, **or** measured
performance benefit.

## Acceptance criteria

pass **only** **when** the change is rejected **and** the simpler supported idiom remains.

## Failure disposition

reject novelty alone as a benefit **and** return the selection **to** CA-M-406.

## Sources

- [PEP 750 — Template Strings](https://peps.python.org/pep-0750/)
- [CA-M-406 — Adopt current Python idioms only for declared benefit](../05_method/CA-M-406-PROGRAMMATIC-ENG_POLICY--adopt-current-python-idioms-only-for-declared-benefit.md)
