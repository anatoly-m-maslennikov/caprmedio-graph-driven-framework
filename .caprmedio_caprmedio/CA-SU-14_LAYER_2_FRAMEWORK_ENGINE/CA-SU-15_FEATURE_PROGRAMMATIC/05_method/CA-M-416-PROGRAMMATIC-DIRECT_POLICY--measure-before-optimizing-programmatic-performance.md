---
identity:
  atom_id: CA-M-416
  ref_id: CA-M-416
context:
  container:
    scope_unit: CA-SU-15
  role: Method
  form: Direct Policy
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality
      <+ Performance <+ Measurement and Profiling
  tier: 4
relations:
  child_of:
  - CA-M-415
  DERIVED_FROM:
  - CA-A-053
state:
  status: Active
  version: 14
  updated_at: 2026-11-10 20:47:54 +0400
current_scope_unit: PROGRAMMATIC
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
destination:
  file:
    name: CA-M-416-PROGRAMMATIC-DIRECT_POLICY--measure-before-optimizing-programmatic-performance.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method
---

## Summary

Measure before optimizing PROGRAMMATIC performance

## Claim



### Prose Claim
measure a PROGRAMMATIC performance concern **before** accepting an optimization;
use a representative workload for its Hook, interactive, batch, MCP, App, **or**
background surface rather than treating one surface as universal.

## Details


### Applicable when

apply **when** a Tool, App backend service, **or** MCP component proposes **or** assesses
a performance-sensitive change.

### Procedure

1. profile the applicable surface **to** locate the measured bottleneck, **then**
   select its representative workload.
2. preserve the input, environment, baseline, observed distribution, **and**
   comparison threshold with the measurement.
3. compare the change **to** the recorded baseline **before** accepting the claimed
   improvement.
4. leave numeric budgets **to** a later bounded authority **until** current baselines
   **and** Operator priorities establish them.

### Outcome

an accepted performance claim is tied **to** one reproducible workload **and**
measurement boundary instead of a universal **or** unmeasured optimization claim.

### Failure or stop

stop the performance claim **when** no representative workload, preserved
baseline, **or** comparable observation exists; do **not** invent a numeric budget.

### Sources

- [Python documentation: profilers](https://docs.python.org/3.14/library/profile.html)
- [pyperf documentation](https://pyperf.readthedocs.io/en/latest/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
