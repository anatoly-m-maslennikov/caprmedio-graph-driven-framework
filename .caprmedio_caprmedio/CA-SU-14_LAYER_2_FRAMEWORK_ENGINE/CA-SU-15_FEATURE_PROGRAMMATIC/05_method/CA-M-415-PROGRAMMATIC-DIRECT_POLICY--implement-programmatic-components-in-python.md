---
identity:
  atom_id: CA-M-415
  ref_id: CA-M-415
context:
  container:
    scope_unit: CA-SU-15
  role: Method
  form: Direct Policy
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Authoring/Code
      Authoring/Python Code
    dependencies:
    - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Resources/Configuration
    - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
    - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations'
  tier: 3
relations:
  derived_from:
  - CA-A-053
  child_of:
  - CA-M-261
state:
  status: Active
  version: 13
  updated_at: 2026-11-09 07:45:14 +0400
destination:
  file:
    name: CA-M-415-PROGRAMMATIC-DIRECT_POLICY--implement-programmatic-components-in-python.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---

## Summary

Implement PROGRAMMATIC components in Python

## Claim

### Prose Claim

use Python for applicable PROGRAMMATIC Tools, App backend services, **and** MCP
components. this Method owns the Python technology selection for that bounded
scope. Configuration **and** Implementation materialize the selected runtime,
dependencies, **and** exceptions; Delivery governs their carrier placement **and**
encoding; Operations defines reusable workflow behavior, **and** Journal Records carry the evidence required by the existing business-lifecycle contract. this Method
does **not** govern Skills **or** make Python a discipline-independent CAPRMEDIO
meaning.

## Details

### Scope

apply **when** a Tool, App backend service, **or** MCP component is added **or** materially
changed, **or** **when** its Python realization, runtime dependency, **or** non-Python
exception is proposed.

Candidate source: [CA-M-110@21](archive/CA-M-110-PROGRAMMATIC-GENERAL-IMPLEMENTATION_METHOD--implement-programmatic-components-in-python@21.md)

#### Procedure
1. apply the Python selection established by this Method **and** read its current
   materialization **before** realizing a component.
2. use the standard library **when** it provides the required behavior with
   comparable clarity **and** reliability.
3. add **or** change a runtime, library, workflow tool, **or** non-Python exception
   **only** through an accepted Method that selects it for a bounded scope.
4. materialize **every** accepted selection **in** canonical configuration **and**
   Implementation **without** making either carrier a second authority.
5. place **and** encode **every** materialization through its Delivery, **and** preserve
   actual execution evidence through its declared owner. Journal writes remain limited
   to the existing business-lifecycle contract; technical execution does not add hidden Journal effects.

#### Outcome

**every** applicable component follows one Method-owned technology selection.
Configuration **and** Implementation reproduce it, Delivery locates its carriers,
**and** the Journal records required business-lifecycle evidence **without** taking over selection authority.

#### Failure or stop

stop admission **or** release **when** no accepted Method owns a required selection,
its materialization disagrees with that Method, **or** the Delivery **or** Operations boundary
is absent. do **not** infer a platform-support claim from local execution.

#### Sources

- [Python 3.14 documentation](https://docs.python.org/3.14/)
- [Python Packaging User Guide: `pyproject.toml`](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
