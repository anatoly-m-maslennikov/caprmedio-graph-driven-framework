---
atom_id: CA-E-531
content_role: Evaluation
type: Eval Case
current_scope_unit: WORKFLOW_ORCHESTRATOR
status: Active
author: Anatoly Maslennikov
version: 11
updated_at: 2026-10-27 19:59:37 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Dynamic Testing
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
