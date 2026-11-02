---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Engineering/Python Idiom Selection
  depends_on: []
version: 13
updated_at: 2026-10-24 00:38:25 +0400
relations:
  evaluation_for:
  - CA-M-406
  derived_from:
  - CA-A-053
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-451@13
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Archived
author: Anatoly Maslennikov
tier: 3
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
- [CA-M-406 — Adopt current Python idioms only for declared benefit](../05_method/CA-M-406-PROGRAMMATIC-STANDARD-ENG_POLICY--adopt-current-python-idioms-only-for-declared-benefit.md)
