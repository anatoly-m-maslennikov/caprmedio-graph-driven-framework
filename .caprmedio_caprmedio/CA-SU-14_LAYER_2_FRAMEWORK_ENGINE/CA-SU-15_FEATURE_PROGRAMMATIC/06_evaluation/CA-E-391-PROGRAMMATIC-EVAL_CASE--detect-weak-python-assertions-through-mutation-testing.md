---
atom_id: CA-E-391
ref_id: CA-E-391
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality
    <+ Verification <+ Dynamic Testing
  dependencies:
  - MODEL//CAPRMEDIO <+ Package/Project Package
tier: 5
relations:
  evaluation_for:
  - CA-M-424
  DERIVED_FROM:
  - CA-A-053
status: Active
version: 22
updated_at: 2026-11-10 20:47:54 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: PROGRAMMATIC
destination:
  file:
    name: CA-E-391-PROGRAMMATIC-EVAL_CASE--detect-weak-python-assertions-through-mutation-testing.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
---
## Summary

Detect weak Python assertions through mutation testing

## Claim

### Prose Claim

#### Claim checked

decision-dense changed Python has assertions strong enough **to** distinguish its
relevant alternative behavior.

#### Test case

run a pinned mutation profile **after** normal cases pass **and** preserve one
surviving relevant mutant **in** a manager **or** validator.

#### Acceptance criteria

pass **only** **when** the mutant is classified as missing assertion, unreachable,
equivalent, **or** intentionally uncovered, **and** the frontier **and** replay command are
preserved.

#### Failure disposition

reject unexplained survivors; keep this expensive campaign outside synchronous
Hooks.

#### Sources

- [Mutmut documentation](https://mutmut.readthedocs.io/en/latest/)
- [CA-M-285 — Select software Evaluation techniques by failure mode](../05_method/CA-M-285-PROGRAMMATIC--select-software-evaluation-techniques-by-failure-mode.md)
