---
atom_id: CA-R-1824@4
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 4
updated_at: 2026-10-23 03:14:50 +0400
subjects:
  governs: WORKFLOW_OPERATIONS/RUN_SUPPORT/journal recovery
  depends_on:
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Initiative
  - Implementation
relations:
  relates_to:
  - CA-R-812
  - CA-R-1644
  - CA-R-1720
---
# Summary

Recover selected Run Journal evidence without replaying effects

## Scope

Durable append and recovery of selected-Run evidence through the existing
Project Work Journal. It excludes a second execution log or Journal.

## Claim

RUN_SUPPORT may independently append selected-Run observations, retain an append
diagnostic, and, when supported, retry only the identical pending observation
without replaying its Action effect. Journal append/receipt is never Run admission
or terminal-success evidence; actual same-session Run state may have no Event ID.

## Details

- An independent append attempt may use an Event identity and append context.
  Its unavailable, failed, or incomplete result is a recording diagnostic; no
  Journal read, receipt, baseline, or retained Journal history is required to
  admit, complete, or describe the actual Run. Actual same-session Run/parent,
  terminal, result, and effect evidence remain available with Event ID absent.
- When a recording retry is supported and pending observation bytes exist, it
  uses those same bytes and any existing Event identity/context. It may detect
  a byte conflict and retain the diagnostic, but it neither requires a
  canonical-once Journal lookup nor changes an actual Run outcome. A later
  `Recovered` observation remains separately admissible only for independently
  established facts under CA-R-1644.
- A recording retry cannot invoke an Action executor, dispatch a Step, create a
  Run, reset authorization, or change an effect. It never replays a completed
  or uncertain mutation; a new execution attempt needs a separately admitted
  request under CA-R-1821.
- Artifact Change Log and Process Log are reconstructed views of independently
  supplied observations. A failed append or incomplete view coverage is visible;
  no caller may manufacture a view record, receipt, time, outcome, or effect to
  claim recovery.
