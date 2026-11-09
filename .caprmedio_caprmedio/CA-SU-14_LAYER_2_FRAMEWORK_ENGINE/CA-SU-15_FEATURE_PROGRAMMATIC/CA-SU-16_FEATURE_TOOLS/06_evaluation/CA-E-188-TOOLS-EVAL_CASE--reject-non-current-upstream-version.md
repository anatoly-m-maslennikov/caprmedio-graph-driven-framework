---
atom_id: CA-E-188
ref_id: CA-E-188
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Data Validation"
tier: 2
relations:
  evaluation_for:
  - CA-R-804
  - CA-R-805
status: Active
version: 24
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Reject non-current upstream version

## Claim checked

the commit flow cannot seal **or** apply a typed upstream relation whose target version is **not** current immediately **before** the file change.

## Test case

prepare one `UPDATE` fixture whose direct upstream target is at version 3, **then** supply a candidate context that names version 2 for that same target.

## Acceptance criteria

the flow returns a deterministic non-current-upstream-version diagnostic, names both versions, **and** creates no governed **or** Git state change.

## Failure disposition

reject the flow **if** it accepts, silently rewrites, **or** omits the stale target reference.
