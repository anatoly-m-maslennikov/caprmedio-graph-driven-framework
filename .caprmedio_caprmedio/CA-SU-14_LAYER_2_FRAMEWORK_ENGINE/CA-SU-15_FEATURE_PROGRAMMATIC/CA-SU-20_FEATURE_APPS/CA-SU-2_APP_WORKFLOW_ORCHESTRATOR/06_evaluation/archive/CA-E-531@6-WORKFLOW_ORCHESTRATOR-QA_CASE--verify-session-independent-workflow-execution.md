---
atom_id: CA-E-531@6
content_role: Evaluation
type: Eval Case
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Archived
author: Anatoly Maslennikov
version: 6
updated_at: 2026-10-24 00:51:05 +0400
subjects:
  governs: Subject/Domain/Node/Occurrent/Execution/Workflow Run
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Domain/Node/Continuant/Atom
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Engineering/Workflow Orchestration/Session-Independent Execution Evaluation
relations:
  relates_to:
  - CA-R-1522
  - CA-R-1523
  - CA-R-1524
  - CA-O-104
tier: 3
---
# Summary

Verify session-independent Workflow execution

## Scope

WORKFLOW_ORCHESTRATOR's initial local execution capability.

## Claim

the Evaluation **must** verify independent execution through mock Agent end-to-end cases **and** the real DBOS queue.

## Details

- queue a Run from a short-lived client, disconnect it, start a separate worker **and** verify recorded gather/check/fix results.
- verify clean checks, admitted fixes, blocked reports, Agent failure, timeout, duplicate requests **and** mismatched identities.
- verify worker restart acknowledges a previously applied after hash rather than repeating the edit.
- verify no recheck phase is introduced **and** initial findings remain **in** the saved report.
- distinguish mock execution from a live Codex model Run; mock passes prove integration boundaries, **not** semantic review quality.
