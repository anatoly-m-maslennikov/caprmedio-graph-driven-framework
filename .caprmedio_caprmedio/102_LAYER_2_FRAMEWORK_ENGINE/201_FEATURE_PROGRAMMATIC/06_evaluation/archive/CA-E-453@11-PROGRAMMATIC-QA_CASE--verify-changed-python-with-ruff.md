---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Method/Python Style Checks
  depends_on: []
version: 11
updated_at: "2026-10-22 12:45:09 +0400"
relations:
  evaluation_for:
    - CA-M-428
    - CA-E-539
  derived_from:
    - CA-A-053
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-453@11
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Archived
author: Anatoly Maslennikov
---
# Verify changed Python with Ruff

## Claim checked

changed Python passes the one admitted Ruff format, lint, **and** complexity
profile **or** carries one bounded exception.

## Test case

run the pinned Ruff profile against one changed module containing an executable
unit above the configured `C901` maximum.

## Acceptance criteria

pass **only** **when** **all** of the following hold:

- Ruff reports the unit that exceeds the configured maximum.
- the change is rejected **or** an accepted bounded exception records the rule, value, reason, **and** review condition.

## Failure disposition

reject the changed target **until** the diagnostic is resolved **or** bounded.

## Sources

- [Ruff: complex-structure rule](https://docs.astral.sh/ruff/rules/complex-structure/)
- [CA-M-428 — Use Ruff for Python formatting, linting, and complexity](../05_method/CA-M-428-PROGRAMMATIC-STANDARD-IMPLEMENTATION_DECISION--use-ruff-for-python-formatting-linting-and-complexity.md)
