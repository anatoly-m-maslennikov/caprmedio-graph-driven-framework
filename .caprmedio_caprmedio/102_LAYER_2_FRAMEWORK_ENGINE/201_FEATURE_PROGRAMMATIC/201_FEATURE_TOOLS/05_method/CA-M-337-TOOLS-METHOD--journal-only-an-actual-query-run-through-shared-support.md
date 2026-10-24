---
atom_id: CA-M-337
content_role: Method
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 6
updated_at: 2026-10-24 02:14:24 +0400
subjects:
  governs: Subject/Domain/Node/Occurrent/Execution
  depends_on:
  - Subject/Domain/Node/Occurrent/Execution
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Domain/Node/Continuant/History/Journal.Record
  - Subject/Engineering/Journal Event Query/Actual Invocation Recording
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
