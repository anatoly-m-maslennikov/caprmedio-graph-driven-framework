---
atom_id: CA-E-184
ref_id: CA-E-184
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Relation/Type
tier: 1
relations:
  evaluation_for:
  - CA-R-806
status: Active
version: 20
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Reject incomplete relation-kind metadata

## Claim checked

deterministic Tools cannot use a relation kind whose canonical registry entry is incomplete.

## Test case

compile a fixture registry containing one **otherwise** valid direct relation whose derived inverse name, declaration carrier, **or** upstream endpoint is absent, **then** gather commit context for a file using that relation.

## Acceptance criteria

registry compilation fails with the exact missing field, context gathering returns no sealed envelope, **and** no governed **or** Git state changes.

## Failure disposition

reject the registry compiler **and** Finder **if** either infers the missing field **or** continues with a partial relation entry.
