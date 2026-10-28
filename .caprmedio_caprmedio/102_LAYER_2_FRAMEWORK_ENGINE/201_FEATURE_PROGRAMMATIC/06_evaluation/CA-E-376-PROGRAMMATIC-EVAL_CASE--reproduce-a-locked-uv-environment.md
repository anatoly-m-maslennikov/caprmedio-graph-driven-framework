---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Code Authoring/Python Code
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Resources/Configuration
version: 23
updated_at: 2026-10-27 19:59:34 +0400
relations:
  evaluation_for:
  - CA-M-423
  - CA-M-429
  derived_from:
  - CA-A-053
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-376
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Active
author: Anatoly Maslennikov
tier: 5
type: Eval Case
---
# Reproduce a locked uv environment

## Claim checked

one admitted PROGRAMMATIC Python environment **and** governed command are
reproduced from the selected Python boundary, `pyproject.toml`, **and**
`uv.lock` **without** implicit dependency changes.

## Test case

from an empty project environment, run `uv sync --locked` **and** **then** one declared
command through `uv run --locked`.

## Acceptance criteria

pass **only** **when** the locked sync **and** command complete **without** changing
`pyproject.toml` **or** `uv.lock`, the observed interpreter satisfies the
Method-selected Python boundary, **and** the command uses **only** Method-selected
dependencies.

## Failure disposition

reject the reproducibility claim **when** the lock is stale, resolution changes
implicitly, **or** a dependency lacks Method authority.

## Sources

- [CA-M-429 — Use uv as the default Python workflow frontend](../05_method/CA-M-429-PROGRAMMATIC-ENG_POLICY--use-uv-as-the-default-python-workflow-frontend.md)
