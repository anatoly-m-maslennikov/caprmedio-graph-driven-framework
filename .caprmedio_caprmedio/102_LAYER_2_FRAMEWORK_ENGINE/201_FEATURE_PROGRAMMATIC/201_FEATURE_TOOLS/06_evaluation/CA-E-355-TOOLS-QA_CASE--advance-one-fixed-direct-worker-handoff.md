---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Engineering/Tool.Orchestration
  depends_on: []
version: 13
updated_at: 2026-10-24 02:14:24 +0400
relations:
  evaluation_for:
  - CA-M-182
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-355
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 3
---
# Advance one fixed direct worker handoff

## Claim checked

a fixed direct worker handoff advances **only** the transition already declared by
the manager.

## Test case

given a manager-produced two-step execution graph whose second step depends on
the first, execute the first worker **and** its synchronous handoff.

## Acceptance criteria

the exact typed result reaches **only** the declared second worker, the manager is
**not** re-entered for a new decision, **and** neither worker can select **or** alter the
downstream transition.

## Failure disposition

reject the handoff **when** a result reaches an undeclared worker, a worker changes
the transition, the manager is re-entered for an already declared decision, **or**
the handoff loops.

## Sources

- [Python documentation: unittest.mock](https://docs.python.org/3/library/unittest.mock.html)
- [PEP 544 — Protocols](https://peps.python.org/pep-0544/)
