---
atom_id: CA-M-428
ref_id: CA-M-428
container:
  scope_unit: CA-SU-15
role: Method
form: Eng Policy
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Static Analysis
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Static Analysis
tier: 4
relations:
  derived_from:
  - CA-A-053
  child_of:
  - CA-M-415
status: Active
version: 11
updated_at: 2026-10-27 19:59:43 +0400
carrier_destination:
  file:
    name: CA-M-428-PROGRAMMATIC-ENG_POLICY--use-ruff-for-python-formatting-linting-and-complexity-use-ruff-as-the-selected-formatter-and-linter-for-hand-authored-programmatic-python-source-including-cyclomatic-complexity-lint-for-changed-executable-units.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/05_method
current_scope_unit: PROGRAMMATIC
cce_version: cce_1
cce_form: method
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
---
# Summary

Use Ruff for Python formatting, linting, and complexity

use Ruff as the selected formatter **and** linter for hand-authored PROGRAMMATIC
Python source, including cyclomatic-complexity lint for changed executable
units.

## Details

Candidate source: [CA-M-282@9](archive/CA-M-282-PROGRAMMATIC-CORE-METHOD--use-ruff-for-python-formatting-linting-and-complexity@9.md)

## Applicable when

apply **to** new **or** materially changed Python source within Tools, App, **or** MCP.

## Procedure

1. materialize one pinned Ruff profile **in** `pyproject.toml`.
2. run Ruff formatting **and** linting through the selected uv workflow.
3. enable the Ruff `C901` rule **and** materialize the applicable Evaluation-owned
   complexity maximum under CA-E-539.
4. provide rule diagnostics, measured values, **and** exception rationale **to**
   CA-E-539 for its acceptance **and** disposition decision.
5. keep Ruff evidence distinct from typing **and** behavioral evidence.

## Outcome

mechanical style, lint, **and** cyclomatic-complexity checks use one reproducible
Method-owned selection **and** one materialized profile.

## Failure or stop

return unavailable configuration **when** Ruff is unpinned **or** the current profile
is absent. changed-source acceptance **and** exception admission follow CA-E-539.

## Sources

- [Ruff documentation](https://docs.astral.sh/ruff/)
- [Ruff: configuration](https://docs.astral.sh/ruff/configuration/)
- [Ruff: complex-structure rule](https://docs.astral.sh/ruff/rules/complex-structure/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
