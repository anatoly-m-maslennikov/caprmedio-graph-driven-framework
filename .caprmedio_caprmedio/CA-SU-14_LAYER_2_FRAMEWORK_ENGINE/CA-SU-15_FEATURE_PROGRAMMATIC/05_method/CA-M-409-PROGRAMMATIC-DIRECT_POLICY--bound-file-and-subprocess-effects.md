---
identity:
  atom_id: CA-M-409
  ref_id: CA-M-409
context:
  container:
    scope_unit: CA-SU-15
  role: Method
  form: Direct Policy
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Execution Control
    dependencies:
    - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution
      Control <+ Effect Authorization
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
destination:
  file:
    name: CA-M-409-PROGRAMMATIC-DIRECT_POLICY--bound-file-and-subprocess-effects.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method
current_scope_unit: PROGRAMMATIC
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
---

## Summary

Bound file and subprocess effects

## Claim



### Prose Claim
plan, validate, **and** bound **every** PROGRAMMATIC file mutation **or** subprocess
invocation **before** applying it; make partial failure diagnosable **and** recoverable
**without** guessing.

## Details


### Applicable when

apply **when** a Tool, App backend service, **or** MCP component writes, replaces, **or**
removes a file, **or** invokes a subprocess.

### Procedure

1. validate the target **and** preconditions **before** mutation.
2. write replacement content through a secure temporary carrier on the
   destination filesystem, flush required bytes, **and** use an atomic replacement
   **only** **where** the supported boundary provides that guarantee.
3. invoke a subprocess with an argument array, explicit timeout, checked exit
   status, controlled environment input, **and** shell execution disabled by
   default.
4. return the target, inputs, outcome, **and** partial-failure context needed for
   diagnosis **or** recovery.

### Outcome

**every** applicable effect has a declared precondition, bounded execution
surface, observable result, **and** explicit recovery limit.

### Failure or stop

stop the effect **when** preconditions fail, an atomicity guarantee is unavailable
**and** no weaker recovery boundary is accepted, **or** subprocess completion,
timeout, **and** exit status cannot be observed.

### Sources

- [Python documentation: `tempfile`](https://docs.python.org/3.14/library/tempfile.html)
- [Python documentation: `subprocess`](https://docs.python.org/3.14/library/subprocess.html)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis_and_advisory/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
