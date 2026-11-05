---
atom_id: CA-E-330
ref_id: CA-E-330
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
tier: 3
relations:
  evaluation_for:
  - CA-M-212
status: Active
version: 20
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Verify patch project settings with generated-value protection

## Claim checked

CA-M-212 changes **only** schema-editable Project Settings keys **and** rejects generated, unknown, **or** stale targets.

## Applicable when

apply whenever the Project Settings schema, ownership classification, **or** patch mechanics change.

## Test case

seal one settings carrier **and** request changes **to** one schema-editable key, one generated key, **and** one unknown key. observe rejection, **then** apply **only** the editable change **and** compare **every** key **and** byte-level diff.

## Acceptance criteria

the mixed patch changes nothing **and** identifies both prohibited keys; the valid patch changes exactly the editable key, preserves **all** unrelated **and** generated values, remains schema-valid, **and** has no undeclared diff.

## Failure disposition

reject the realization **and** preserve schema, key classifications, requested operations, dry-run diff, final carrier, **and** undeclared-change comparison.
