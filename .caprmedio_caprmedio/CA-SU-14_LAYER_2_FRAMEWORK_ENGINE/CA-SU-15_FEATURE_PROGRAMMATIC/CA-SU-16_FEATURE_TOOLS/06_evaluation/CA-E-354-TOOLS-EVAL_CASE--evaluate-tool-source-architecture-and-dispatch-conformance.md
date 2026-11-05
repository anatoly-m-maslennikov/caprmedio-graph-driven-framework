---
atom_id: CA-E-354
ref_id: CA-E-354
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Dynamic Testing
tier: 3
relations:
  evaluation_for:
  - CA-M-157
  - CA-M-158
  - CA-M-160
  - CA-M-162
  - CA-M-182
status: Active
version: 23
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Evaluate Tool source architecture and dispatch conformance

## Claim checked

changed Tool source conforms **to** the shared PROGRAMMATIC function, object,
effect, source-boundary, **and** manager-defined execution-graph Methods.

## Test case

apply **to** **every** new **or** materially changed Tool source tree.

## Check

evaluate declared file **and** executable-unit limits, side-effect-free standalone
functions, specifically named bounded one-shot effect functions **or** objects
with owned state, invariant, resource, lifecycle **or** adapter responsibility
under CA-M-158 **and** CA-M-160, one pure decision manager,
atomic non-deciding workers, an acyclic manager-defined execution graph,
mechanical scheduling **or** direct dispatch, canonical manager, worker, **and** asset
placement, **and** externalized large static mappings. inject worker observations
**and** require **every** semantic **and** lifecycle decision **to** remain **in** the manager's
explicit result. require handoffs **and** queued completions **to** follow **only**
manager-declared transitions.

## Acceptance

pass **only** **when** **every** applicable boundary conforms independently **and** the
dispatcher **or** scheduler advances the declared graph **without** changing it.

## Failure and stop

fail **every** violated constraint independently with the exact file, object,
dependency, transition, **or** effect boundary. generated Runtime **or** Delivery
output cannot excuse a violation **in** hand-authored Tool source.

## Sources

- [Ruff: complex-structure rule](https://docs.astral.sh/ruff/rules/complex-structure/)
- [Python FAQ: testing programs and components](https://docs.python.org/3/faq/library.html#how-do-i-test-a-python-program-or-component)
- [Python documentation: `unittest.mock`](https://docs.python.org/3/library/unittest.mock.html)
- [Python documentation: queues](https://docs.python.org/3.14/library/asyncio-queue.html)
