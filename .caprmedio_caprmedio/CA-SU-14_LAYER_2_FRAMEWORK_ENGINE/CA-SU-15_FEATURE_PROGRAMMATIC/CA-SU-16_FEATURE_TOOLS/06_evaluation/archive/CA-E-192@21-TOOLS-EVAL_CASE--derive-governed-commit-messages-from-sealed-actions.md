---
subjects:
  governs: Subject/Engineering/Git/Commit
  depends_on:
  - Initiative
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Work Journal/Journal Batch
version: 21
updated_at: 2026-10-24 22:06:39 +0400
relations:
  evaluation_for:
  - CA-D-334
  - CA-R-805
  - CA-R-812
  - CA-D-417
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-192@21
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Derive Governed Commit Messages from Sealed Actions

## Claim checked

the canonical Git commit message is a deterministic Projection of **=1** sealed Git-effect action: an Initiative-based real-change action **or** a distinct Journal-only batch action.

## Test case

prepare one sealed real-change action whose Initiative comes from human input **and** one sealed Journal-only batch action. independently render `<initiative-summary> | <CHANGE_CLASS> | <affected-subject>` **and** `JOURNAL BATCH | APPEND | <journal-batch-id>`, **then** compare both renderings with the corresponding Git commit subjects.

## Acceptance criteria

**every** Git commit subject is byte-identical **to** its independently rendered Projection, **contains** no added prefix, suffix, quoting, normalization, line wrapping, **or** technical-parent substitution, **and** neither action accepts the other message class.

## Failure disposition

reject the flow at the first rendering mismatch, technical-parent substitution, **or** cross-class impersonation **and** report the sealed action **and** divergent output.
