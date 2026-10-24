---
subjects:
  governs: Subject/Engineering/Tool//COMMIT_CONTEXT
  depends_on:
  - Subject/Engineering/Tool/Journal Append
  - Subject/Domain/Node/Continuant/History/Journal.Record
  - Subject/Engineering/Carrier
version: 18
updated_at: 2026-10-24 02:14:24 +0400
relations:
  evaluation_for:
  - CA-R-1491
  - CA-R-804
  - CA-R-812
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-187
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Reject incomplete context before Journal append

## Claim checked

the Journal-appending Doer rejects an incomplete sealed event **before** append while preserving the failure **and** pending evidence under CA-R-812 **and** CA-R-1491.

## Test case

remove the singular canonical `result` field from an **otherwise** valid sealed `UPDATE` context **and** invoke `APPEND_CHANGE_RECORDS` apply. capture the pending input, diagnostic, provisional unconsumed lease, runtime state, Journal bytes **and** Git state **before** **and** **after** rejection.

## Acceptance criteria

- return a deterministic missing-`result` diagnostic **before** the first Journal append. do **not** reconstruct the omitted canonical field from the current working tree.
- append no record from the incomplete input **and** change no Git state. release the owned provisional unconsumed lease **without** disturbing another action's state.
- preserve the rejected input **and** failure as inspectable pending **or** blocked runtime evidence under the existing recovery boundary. recording that state is **not** a successful append, Project conformance verdict **or** permission **to** retry with invented data.
- retain accepted Journal history unchanged. loss of the pending evidence is **not** successful cleanup.

## Failure disposition

reject invented fields, an append from incomplete input, lost pending evidence, an abandoned owned unconsumed lease, partial application, hidden runtime failure **or** a generic diagnostic that omits the missing field.
