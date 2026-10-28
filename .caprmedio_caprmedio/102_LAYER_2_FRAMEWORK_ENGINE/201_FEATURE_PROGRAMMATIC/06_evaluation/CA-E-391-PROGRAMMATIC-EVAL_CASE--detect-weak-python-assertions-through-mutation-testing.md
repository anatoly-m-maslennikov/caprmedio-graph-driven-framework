---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Dynamic Testing
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
version: 21
updated_at: 2026-10-27 19:59:34 +0400
relations:
  evaluation_for:
  - CA-M-285
  derived_from:
  - CA-A-053
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-391
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: PROGRAMMATIC
type: Eval Case
tier: 1
---
# Detect weak Python assertions through mutation testing

## Claim checked

decision-dense changed Python has assertions strong enough **to** distinguish its
relevant alternative behavior.

## Test case

run a pinned mutation profile **after** normal cases pass **and** preserve one
surviving relevant mutant **in** a manager **or** validator.

## Acceptance criteria

pass **only** **when** the mutant is classified as missing assertion, unreachable,
equivalent, **or** intentionally uncovered, **and** the frontier **and** replay command are
preserved.

## Failure disposition

reject unexplained survivors; keep this expensive campaign outside synchronous
Hooks.

## Sources

- [Mutmut documentation](https://mutmut.readthedocs.io/en/latest/)
- [CA-M-285 — Select software Evaluation techniques by failure mode](../05_method/CA-M-285-PROGRAMMATIC--select-software-evaluation-techniques-by-failure-mode.md)
