---
atom_id: CA-E-193
ref_id: CA-E-193
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 3
relations:
  evaluation_for:
  - CA-M-087
  - CA-R-805
  - CA-R-812
status: Active
version: 27
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Append all related Journal records independently of commit timing

## Claim checked

the Journal Doer completes **every** related append independently of real-change commit timing **and** **without** using the repository Git gate for the append itself.

## Test case

start two valid actions for the same repository whose related records span disjoint **and** shared Journal carriers. **in** separate runs, complete Journal append **before**, during, **and** **after** the corresponding real-change commit; **then** commit the completed records **in** a later Journal-only batch.

## Acceptance criteria

disjoint Journal partitions **may** append concurrently. **every** shared carrier has one canonical writer **or** batcher, **every** accepted record is durable **and** idempotent, **and** no Journal append acquires the repository Git gate. real-change commits do **not** wait for Journal receipts. the later Journal-only commit **contains** **all** **and** **only** its selected Journal Carriers **and** shares the single fenced commit gate.

## Failure disposition

reject the flow **if** Journal timing gates the real-change commit, an append is lost **or** duplicated, writers race on one shared carrier, Journal append uses the Git gate, **or** either commit class **contains** the other's files.
