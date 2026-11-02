---
atom_id: CA-M-337@9
content_role: Method
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Domain/Occurrent/Execution
  depends_on:
  - Subject/Graph Node/Domain/Occurrent/Execution
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - Subject/Graph Node/Domain/Continuant/History/Journal.Record
relations:
  method_for:
  - CA-R-1867
type: Eng Decision
tier: 4
---
# Summary

Journal only an actual query Run through shared support

## Scope

Actual query invocation evidence.

## Claim

To record an actual Journal query invocation, the Tool **must** delegate
preview/execute admission and Run evidence to shared selected-Run support only
after the adapter captured the sealed frontier; that evidence consumes no Event
in the frontier.

## Details

Preview has no Run/Event; execute records only actual Run outcomes and cannot change the already captured result frontier.
