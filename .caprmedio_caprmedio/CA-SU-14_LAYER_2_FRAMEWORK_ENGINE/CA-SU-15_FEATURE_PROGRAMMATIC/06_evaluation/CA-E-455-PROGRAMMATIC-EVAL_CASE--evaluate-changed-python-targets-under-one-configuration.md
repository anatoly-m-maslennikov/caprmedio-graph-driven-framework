---
atom_id: CA-E-455
ref_id: CA-E-455
container:
  scope_unit: CA-SU-15
role: Evaluation
form: Eval Case
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Static Analysis"
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code
tier: 1
relations:
  evaluation_for:
  - CA-M-164
  derived_from:
  - CA-A-053
status: Active
version: 21
updated_at: 2026-10-27 19:59:35 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: PROGRAMMATIC
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
