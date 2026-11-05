---
cce_version: cce_1
cce_form: evaluation
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
version: 23
updated_at: 2026-11-02 19:44:26 +0400
relations:
  evaluation_for:
  - CA-M-087
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-400
ref_id: CA-E-400
status: Active
role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
form: Eval Case
tier: 3
container:
  scope_unit: CA-SU-16
---
# Reconcile one missed external project change

## Claim checked

repository reconciliation recovers one Git-admitted project change that has no
Codex Hook event **without** inventing session provenance **or** duplicating work.

## Test case

create one admitted project change outside Codex Hook delivery, **then** run one
low-frequency reconciliation cycle twice against the resulting frontier.

## Acceptance criteria

pass **only** **when** the first cycle creates one governed action, identifies
repository reconciliation as its observation source, advances the normal commit
pipeline once, **and** the second cycle produces no duplicate action.

## Failure disposition

reject the reconciliation boundary **when** the change remains invisible, receives
invented Codex provenance, bypasses the normal pipeline, **or** is processed twice.

## Sources

- [Git documentation: porcelain v2](https://git-scm.com/docs/git-status#_porcelain_format_version_2)
- [CA-M-087 — Process one file change](../05_method/CA-M-087-TOOLS-ENG_DECISION--process-one-project-path-action.md)
