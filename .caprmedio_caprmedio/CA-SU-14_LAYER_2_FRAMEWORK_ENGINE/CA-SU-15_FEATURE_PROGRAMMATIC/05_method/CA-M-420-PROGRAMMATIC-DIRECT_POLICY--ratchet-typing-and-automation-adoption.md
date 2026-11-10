---
identity:
  atom_id: CA-M-420
  ref_id: CA-M-420
context:
  container:
    scope_unit: CA-SU-15
  role: Method
  form: Direct Policy
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality
      <+ Verification <+ Static Analysis
    dependencies:
    - MODEL//CAPRMEDIO <+ Event Record
  tier: 4
relations:
  child_of:
  - CA-M-415
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
    name: CA-M-420-PROGRAMMATIC-DIRECT_POLICY--ratchet-typing-and-automation-adoption.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method
---

## Summary

Ratchet typing and automation adoption

## Claim



### Prose Claim
advance PROGRAMMATIC typing **and** automation through bounded target selection,
explicit tool configuration, **and** deliberate expansion. Evaluation authority
owns acceptance profiles **and** regression policy under CA-E-539, CA-E-540,
**and** the applicable behavioral Evaluation.

## Details


### Applicable when

apply **when** a Tool, App backend service, **or** MCP component adds **or** materially
changes source that falls within an admitted typing, formatting, linting, **or**
behavioral-check capability.

### Procedure

1. resolve **every** selected typing, formatting, linting, **or** behavioral-check
   capability from its accepted Method owner.
2. read its current tool, version, profile, **and** bounded target materialization
   from canonical configuration **or** Implementation; read carrier placement **and**
   encoding from Delivery.
3. keep formatting, linting, typing, **and** behavioral evidence distinct.
4. provide changed **or** new target evidence **and** its current admitted baseline
   **to** the applicable Evaluation for its regression decision.
5. expand **or** replace a selected capability **only** through a Method change;
   materialize that change separately **and** preserve actual run evidence through its
   declared owner. Journal writes remain limited to the existing business-lifecycle
   contract; technical checks do not add hidden Journal effects.

### Outcome

automation **and** typing improve monotonically at an admitted surface **without**
turning an unselected tool, version, **or** strictness level into shared authority.

### Failure or stop

return unresolved selection **when** no accepted Method owns the tool choice **or**
the bounded materialization is unavailable. Evaluation authority determines
whether the supplied baseline **and** execution evidence admit the claimed ratchet.

### Sources

- [Ruff documentation](https://docs.astral.sh/ruff/)
- [Mypy: using Mypy with an existing codebase](https://mypy.readthedocs.io/en/stable/existing_code.html)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
