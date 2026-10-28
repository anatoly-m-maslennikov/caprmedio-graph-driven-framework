---
atom_id: CA-M-416@10
content_role: Method
type: Eng Policy
current_scope_unit: PROGRAMMATIC
status: Archived
subjects:
  governs: Subject/Graph Node/Engineering/Verification/Dynamic Testing
version: 10
updated_at: 2026-10-27 06:04:45 +0400
cce_version: cce_1
cce_form: method
relations:
  derived_from:
  - CA-A-053
  child_of:
  - CA-M-415
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
tier: 4
author: Anatoly Maslennikov
---
# Summary

Measure before optimizing PROGRAMMATIC performance

measure a PROGRAMMATIC performance concern **before** accepting an optimization;
use a representative workload for its Hook, interactive, batch, MCP, App, **or**
background surface rather than treating one surface as universal.

## Details

Candidate source: [CA-M-165@9](archive/CA-M-165-PROGRAMMATIC-CORE-METHOD--measure-before-optimizing-programmatic-performance@9.md)

## Applicable when

apply **when** a Tool, App backend service, **or** MCP component proposes **or** assesses
a performance-sensitive change.

## Procedure

1. profile the applicable surface **to** locate the measured bottleneck, **then**
   select its representative workload.
2. preserve the input, environment, baseline, observed distribution, **and**
   comparison threshold with the measurement.
3. compare the change **to** the recorded baseline **before** accepting the claimed
   improvement.
4. leave numeric budgets **to** a later bounded authority **until** current baselines
   **and** Operator priorities establish them.

## Outcome

an accepted performance claim is tied **to** one reproducible workload **and**
measurement boundary instead of a universal **or** unmeasured optimization claim.

## Failure or stop

stop the performance claim **when** no representative workload, preserved
baseline, **or** comparable observation exists; do **not** invent a numeric budget.

## Sources

- [Python documentation: profilers](https://docs.python.org/3.14/library/profile.html)
- [pyperf documentation](https://pyperf.readthedocs.io/en/latest/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
