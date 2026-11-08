---
identity:
  atom_id: CA-M-406
  ref_id: CA-M-406
context:
  container:
    scope_unit: CA-SU-15
  role: Method
  form: Direct Policy
  topics:
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Code Authoring/Python
      Code
    dependencies:
    - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Code Authoring/Python
      Code
  tier: 4
relations:
  derived_from:
  - CA-A-053
  child_of:
  - CA-M-415
state:
  status: Active
  version: 12
  updated_at: 2026-11-09 00:09:26 +0400
current_scope_unit: PROGRAMMATIC
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
destination:
  file:
    name: CA-M-406-PROGRAMMATIC-DIRECT_POLICY--adopt-current-python-idioms-only-for-declared-benefit.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method
---
# Summary

Adopt current Python idioms only for declared benefit

adopt a stable idiom available **in** the selected Python boundary **only** **when** it
improves a named project quality such as correctness, understandability,
safety, **or** measured performance. preserve the simpler supported idiom **when** a
newer construct adds no useful distinction.

## Details

Candidate source: [CA-M-280@8](archive/CA-M-280-PROGRAMMATIC-CORE-METHOD--adopt-current-python-idioms-only-for-declared-benefit@8.md)

## Applicable when

apply **when** new **or** materially changed PROGRAMMATIC Python source proposes a
runtime-specific language construct **or** concurrency model.

## Procedure

1. state the quality improved **and** the supported Python boundary that admits
   the idiom.
2. prefer the simplest current construct that expresses the required meaning.
3. use f-strings for immediate trusted string construction; use t-strings **only**
   **when** a processor needs structured interpolation data.
4. keep synchronous work synchronous **unless** related concurrent operations
   create a demonstrated need for structured concurrency.
5. record a compatibility exception **when** an admitted host boundary cannot use
   the selected idiom.

## Outcome

current Python capabilities improve the code for an explicit reason **without**
turning novelty into a requirement **or** obscuring the supported boundary.

## Failure or stop

stop adoption **when** the benefit is unnamed, the simpler idiom is equally clear,
**or** the construct exceeds the selected runtime **or** compatibility boundary.

## Sources

- [PEP 750 — Template Strings](https://peps.python.org/pep-0750/)
- [Python documentation: task groups](https://docs.python.org/3.14/library/asyncio-task.html#task-groups)
- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
