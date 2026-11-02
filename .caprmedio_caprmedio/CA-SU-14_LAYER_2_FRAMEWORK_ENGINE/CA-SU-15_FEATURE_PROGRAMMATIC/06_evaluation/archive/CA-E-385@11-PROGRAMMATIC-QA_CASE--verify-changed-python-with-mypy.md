---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Engineering/Python Type Checks
  depends_on:
  - Subject/Engineering/Isolated Python Execution
version: 11
updated_at: 2026-10-22 16:26:49 +0000
relations:
  evaluation_for:
  - CA-M-427
  - CA-E-540
  derived_from:
  - CA-A-053
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-385@11
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Archived
author: Anatoly Maslennikov
---
# Verify changed Python with Mypy

## Claim checked

new Python passes the strict admitted Mypy profile **and** changed Python does **not**
regress below its passing baseline.

## Test case

add one incompatible return type **and** one unexplained broad suppression **to** a
changed target **in** the admitted Mypy set.

## Acceptance criteria

pass **only** **when** both defects are reported **and** the target is rejected.

## Failure disposition

reject the changed target **until** types agree **or** a narrow explained suppression
is accepted.

## Sources

- [Mypy: strict mode](https://mypy.readthedocs.io/en/stable/command_line.html#cmdoption-mypy-strict)
- [CA-M-427 — Use Mypy for static Python type checking](../05_method/CA-M-427-PROGRAMMATIC-STANDARD-IMPLEMENTATION_DECISION--use-mypy-for-static-python-type-checking.md)
