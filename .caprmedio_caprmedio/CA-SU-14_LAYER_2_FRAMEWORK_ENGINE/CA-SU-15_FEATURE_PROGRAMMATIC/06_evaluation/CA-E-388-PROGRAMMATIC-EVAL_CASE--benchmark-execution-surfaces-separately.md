---
atom_id: CA-E-388
ref_id: CA-E-388
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Dynamic Testing"
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
tier: 1
relations:
  evaluation_for:
  - CA-M-165
  derived_from:
  - CA-A-053
status: Active
version: 19
updated_at: 2026-10-27 19:59:34 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: PROGRAMMATIC
---
# Benchmark execution surfaces separately

## Claim checked

a performance claim is reproducible for one declared execution surface **and** is
**not** generalized **to** another surface.

## Test case

benchmark one bounded batch Tool workload **and** attempt **to** use that result as the
latency baseline for an interactive Hook.

## Acceptance criteria

pass **only** **when** the batch result preserves command, fixture, runtime, platform,
calibration, distribution, baseline, **and** comparison, while the Hook claim is
rejected as unmeasured.

## Failure disposition

reject unstable **or** cross-surface evidence **and** reopen the affected claim.

## Sources

- [pyperf documentation](https://pyperf.readthedocs.io/en/latest/)
- [CA-M-165 — Measure before optimizing PROGRAMMATIC performance](../05_method/CA-M-165-PROGRAMMATIC-CORE-METHOD--measure-before-optimizing-programmatic-performance.md)
