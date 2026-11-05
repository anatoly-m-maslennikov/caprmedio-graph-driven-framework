---
cce_version: cce_1
cce_form: evaluation
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Dynamic Testing
  dependencies:
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
atom_id: CA-E-395
ref_id: CA-E-395
status: Active
role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: PROGRAMMATIC
form: Eval Case
tier: 1
container:
  scope_unit: CA-SU-15
---
# Fuzz parsers and stateful boundaries

## Claim checked

broad input **or** transition spaces preserve accepted invariants under generated
valid, invalid, **and** ordered cases.

## Test case

run a bounded property **or** state-machine campaign against one parser **or**
lifecycle **and** inject an invariant-breaking generated sequence.

## Acceptance criteria

pass **only** **when** the minimal failing input **or** sequence **and** seed are preserved,
the defect is accepted **or** rejected explicitly, **and** an accepted defect gains a
deterministic regression case.

## Failure disposition

reject unreplayable generated evidence **and** keep expensive campaigns outside
synchronous Hooks.

## Sources

- [Hypothesis stateful testing](https://hypothesis.readthedocs.io/en/latest/stateful.html)
- [CA-M-285 — Select software Evaluation techniques by failure mode](../05_method/CA-M-285-PROGRAMMATIC--select-software-evaluation-techniques-by-failure-mode.md)
