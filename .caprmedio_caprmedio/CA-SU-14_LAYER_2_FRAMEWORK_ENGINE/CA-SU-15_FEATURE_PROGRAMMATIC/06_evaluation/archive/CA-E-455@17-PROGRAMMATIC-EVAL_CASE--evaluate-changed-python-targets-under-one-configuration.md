---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Engineering/Evaluation
  depends_on:
  - Subject/Engineering/programmatic software
version: 17
updated_at: 2026-10-24 22:06:39 +0400
relations:
  evaluation_for:
  - CA-M-164
  derived_from:
  - CA-A-053
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-455@17
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: PROGRAMMATIC
type: Eval Case
tier: 1
---
# Evaluate changed Python targets under one configuration

## Claim checked

**every** changed Python target receives distinct syntax, Ruff, Mypy, **and** relevant
behavioral evidence under one declared interpreter **and** configuration.

## Test case

evaluate one changed target for which Ruff passes, Mypy fails, **and** its focused
behavioral case passes.

## Acceptance criteria

pass **only** **when** the three results remain separate **and** the aggregate changed-code
gate fails with the target, diagnostic, boundary, **and** replay command.

## Failure disposition

reject masking one mechanism with another **and** return the failed evidence **to** its
owner.

## Sources

- [Ruff documentation](https://docs.astral.sh/ruff/)
- [Mypy documentation](https://mypy.readthedocs.io/en/stable/)
- [CA-M-164 — Ratchet typing and automation adoption](../05_method/CA-M-164-PROGRAMMATIC-CORE-METHOD--ratchet-typing-and-automation-adoption.md)
