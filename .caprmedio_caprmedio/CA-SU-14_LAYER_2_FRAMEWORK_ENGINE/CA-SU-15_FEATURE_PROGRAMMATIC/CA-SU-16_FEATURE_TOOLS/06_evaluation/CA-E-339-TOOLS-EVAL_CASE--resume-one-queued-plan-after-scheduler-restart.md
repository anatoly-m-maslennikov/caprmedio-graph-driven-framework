---
atom_id: CA-E-339
ref_id: CA-E-339
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
tier: 3
relations:
  evaluation_for:
  - CA-M-182
status: Active
version: 19
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Resume one queued plan after Scheduler restart

## Claim checked

a durable manager-defined plan survives Scheduler **and** service termination.

## Test case

persist one plan with a completed step **and** one newly ready step, terminate the Scheduler **and** manager, restart from the selected installed release, **and** dispatch once.

## Acceptance criteria

the completed step is **not** replayed, exactly the persisted ready step is claimed, its identities **and** digests are preserved, **and** no new transition is inferred.

## Failure disposition

reject recovery **if** work is lost, duplicated, reordered, **or** reconstructed from process memory.
