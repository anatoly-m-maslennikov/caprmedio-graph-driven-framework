---
identity:
  atom_id: CA-M-427
  ref_id: CA-M-427
context:
  container:
    scope_unit: CA-SU-15
  role: Method
  form: Direct Policy
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality
      <+ Verification <+ Static Analysis
    dependencies: []
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
    name: CA-M-427-PROGRAMMATIC-DIRECT_POLICY--use-mypy-for-static-python-type-checking.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method
current_scope_unit: PROGRAMMATIC
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
---

## Summary

Use Mypy for static Python type checking

## Claim



### Prose Claim
use Mypy as the selected static type checker for hand-authored PROGRAMMATIC
Python source. CA-E-540 owns strict-profile, baseline, **and** suppression
acceptance policy.

## Details


### Applicable when

apply **to** new **or** materially changed Python source within Tools, App, **or** MCP.

### Procedure

1. materialize one pinned Mypy profile **and** bounded target set **in**
   `pyproject.toml`.
2. run Mypy through the selected uv workflow.
3. provide the current diagnostics **and** recorded baseline **to** CA-E-540.
4. bind suppression rationale **to** the affected line **or** symbol for evaluation
   under CA-E-540.
5. keep static typing evidence distinct from runtime validation **and** behavioral
   evidence.

### Outcome

changed Python interfaces become more explicit **without** making untyped legacy
source an unrelated whole-project blocker.

### Failure or stop

return unavailable configuration **when** the profile **or** target set is absent.
typing acceptance, baseline regression, **and** suppression disposition follow
CA-E-540.

### Sources

- [Mypy documentation](https://mypy.readthedocs.io/en/stable/)
- [Mypy: using Mypy with an existing codebase](https://mypy.readthedocs.io/en/stable/existing_code.html)
- [Mypy: strict mode](https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-strict)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
