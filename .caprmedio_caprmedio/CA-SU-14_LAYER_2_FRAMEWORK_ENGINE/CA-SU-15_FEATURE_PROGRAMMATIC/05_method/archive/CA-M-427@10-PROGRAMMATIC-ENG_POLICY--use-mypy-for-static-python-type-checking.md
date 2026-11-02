---
atom_id: CA-M-427@10
content_role: Method
type: Eng Policy
current_scope_unit: PROGRAMMATIC
status: Archived
subjects:
  governs: Subject/Graph Node/Engineering/Verification/Static Analysis
  depends_on:
  - Subject/Graph Node/Engineering/Verification/Static Analysis
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

Use Mypy for static Python type checking

use Mypy as the selected static type checker for hand-authored PROGRAMMATIC
Python source. CA-E-540 owns strict-profile, baseline, **and** suppression
acceptance policy.

## Details

Candidate source: [CA-M-283@9](archive/CA-M-283-PROGRAMMATIC-CORE-METHOD--use-mypy-for-static-python-type-checking@9.md)

## Applicable when

apply **to** new **or** materially changed Python source within Tools, App, **or** MCP.

## Procedure

1. materialize one pinned Mypy profile **and** bounded target set **in**
   `pyproject.toml`.
2. run Mypy through the selected uv workflow.
3. provide the current diagnostics **and** recorded baseline **to** CA-E-540.
4. bind suppression rationale **to** the affected line **or** symbol for evaluation
   under CA-E-540.
5. keep static typing evidence distinct from runtime validation **and** behavioral
   evidence.

## Outcome

changed Python interfaces become more explicit **without** making untyped legacy
source an unrelated whole-project blocker.

## Failure or stop

return unavailable configuration **when** the profile **or** target set is absent.
typing acceptance, baseline regression, **and** suppression disposition follow
CA-E-540.

## Sources

- [Mypy documentation](https://mypy.readthedocs.io/en/stable/)
- [Mypy: using Mypy with an existing codebase](https://mypy.readthedocs.io/en/stable/existing_code.html)
- [Mypy: strict mode](https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-strict)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
