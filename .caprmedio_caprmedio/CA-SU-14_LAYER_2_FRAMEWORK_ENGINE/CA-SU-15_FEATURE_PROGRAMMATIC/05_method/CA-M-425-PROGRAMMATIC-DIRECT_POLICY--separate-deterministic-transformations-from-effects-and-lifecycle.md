---
identity:
  atom_id: CA-M-425
  ref_id: CA-M-425
context:
  container:
    scope_unit: CA-SU-15
  role: Method
  form: Direct Policy
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Execution Control
    dependencies:
    - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Authoring
      <+ Code Authoring
    - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture
      <+ Component Structure
  tier: 4
relations:
  child_of:
  - CA-M-415
  IS_REPLACEMENT_FOR:
  - CA-M-426
  DERIVED_FROM:
  - CA-A-053
state:
  status: Active
  version: 15
  updated_at: 2026-11-10 20:47:54 +0400
current_scope_unit: PROGRAMMATIC
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
destination:
  file:
    name: CA-M-425-PROGRAMMATIC-DIRECT_POLICY--separate-deterministic-transformations-from-effects-and-lifecycle.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method
---

## Summary

Separate deterministic transformations from effects and lifecycle

## Claim

### Prose Claim

keep PROGRAMMATIC decisions **in** a function-based deterministic core. apply
filesystem, process, clock, environment, network, persistence, **or**
logging-export effects through a specifically named bounded one-shot function
**when** no identity **or** ownership is required, **or** through a specifically named
method on an object that owns state, an invariant, a resource, a lifecycle, **or**
a replaceable adapter.

## Details


### Applicable when

apply **when** a Tool, App backend service, **or** MCP component combines a decision
with an external effect, asynchronous work, **or** lifecycle transition.

### Procedure

1. form the decision, target, ordering, **and** expected outcome with deterministic
   functions from explicit observations **before** applying an effect.
2. pass the resulting plan **to** one bounded effect boundary.
3. use a function for a one-shot effect **only** **when** its complete target,
   dependency, input, outcome, **and** failure boundary are explicit **and** it owns
   no identity across calls, state, invariant, resource, lifecycle, **or** adapter.
4. use a specifically named object method **when** the effect **must** own **any** of those
   responsibilities across calls.
5. return typed observations **or** completion facts **to** the decision boundary;
   do **not** let the effect owner invent, reorder, **or** suppress a decision.

### Outcome

decision logic is locally readable **and** replayable. **every** effect has a visible,
bounded function **or** object owner, ordered input, **and** recoverable result
boundary. objects exist **only** **where** persistent identity **or** ownership requires
them.

### Failure or stop

stop execution **when** the plan is incomplete, an effect owner would make a new
business decision, a one-shot effect hides a dependency **or** exceeds its declared
boundary, an object exists **without** owned identity **or** ownership, **or** the effect
boundary cannot report a typed result.

### Sources

- [Python Functional Programming HOWTO](https://docs.python.org/3.14/howto/functional.html)
- [Python documentation: data classes](https://docs.python.org/3.14/library/dataclasses.html)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis_and_advisory/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)

### Pure computation and execution recording

Keep pure computation independent of persistence and Run or Journal writes. Construct results and diagnostics from bound inputs without hidden writes. Persist an output only through its declared authorized effect boundary. Actual execution recording remains with its declared executor; generated output alone does not establish durable terminal completion.
