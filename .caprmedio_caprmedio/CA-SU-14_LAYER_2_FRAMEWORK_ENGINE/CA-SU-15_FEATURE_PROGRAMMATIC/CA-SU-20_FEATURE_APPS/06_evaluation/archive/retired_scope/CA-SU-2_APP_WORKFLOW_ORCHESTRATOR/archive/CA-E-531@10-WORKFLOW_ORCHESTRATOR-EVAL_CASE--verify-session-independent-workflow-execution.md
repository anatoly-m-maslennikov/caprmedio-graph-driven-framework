---
atom_id: CA-E-531@10
content_role: Evaluation
type: Eval Case
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Archived
author: Anatoly Maslennikov
version: 10
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Continuant/Atom
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - Subject/Graph Node/Engineering/Verification/Dynamic Testing
relations: {}
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
