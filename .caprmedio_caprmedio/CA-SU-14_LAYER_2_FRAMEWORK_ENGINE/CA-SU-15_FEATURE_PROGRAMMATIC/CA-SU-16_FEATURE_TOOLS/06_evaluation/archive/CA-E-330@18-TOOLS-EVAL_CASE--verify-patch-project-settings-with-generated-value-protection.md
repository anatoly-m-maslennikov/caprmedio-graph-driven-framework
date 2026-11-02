---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Project.Settings
  depends_on: []
version: 18
updated_at: 2026-10-26 00:46:35 +0400
relations:
  evaluation_for:
  - CA-M-212
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-330@18
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 3
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
