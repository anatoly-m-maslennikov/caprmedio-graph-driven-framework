---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: generated-boundary-evaluation
  depends_on:
  - programmatic software
version: 14
updated_at: 2026-10-24 10:48:25 +0400
relations:
  evaluation_for:
  - CA-M-285
  derived_from:
  - CA-A-053
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-395@14
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: PROGRAMMATIC
type: Eval Case
tier: 1
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
