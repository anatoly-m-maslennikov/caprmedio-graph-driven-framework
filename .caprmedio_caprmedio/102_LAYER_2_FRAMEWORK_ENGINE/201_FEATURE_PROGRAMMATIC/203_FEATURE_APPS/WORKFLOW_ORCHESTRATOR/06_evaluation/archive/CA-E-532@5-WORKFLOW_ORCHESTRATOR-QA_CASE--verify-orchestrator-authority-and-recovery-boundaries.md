---
atom_id: CA-E-532@5
content_role: Evaluation
type: Eval Case
current_scope_unit: WORKFLOW_ORCHESTRATOR
local_tier: Standard
global_tier: 14
status: Archived
author: Anatoly Maslennikov
version: 5
updated_at: 2026-10-23 03:14:50 +0400
subjects:
  governs: Subject/Domain/Node/Occurrent/Execution/Workflow Run
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Domain/Node/Continuant/Atom
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Continuant/History/Journal
  - Implementation
  - Subject/Engineering/Workflow Orchestration/Authority and Recovery Evaluation
relations:
  relates_to:
  - CA-R-1522
  - CA-R-1523
  - CA-R-1524
  - CA-O-104
---
# Summary

Verify orchestrator authority and recovery boundaries

## Scope

WORKFLOW_ORCHESTRATOR's initial local execution capability.

## Claim

the Evaluation **must** verify rejection of orchestration requests **or** Agent output outside declared authority.

## Details

- reject unsupported Workflows, traversal, symlinks, protected paths, unknown fields, stale input **and** conflicting duplicate Run requests.
- check phases cannot modify source Atoms; allow_fixes=false preserves source bytes.
- reject Agent-assigned successor IDs, undelegated Summary changes, low confidence, incomplete checks **and** invalid report fields.
- **with** allow_replacements=true **and** fix permission, verify the new unreused ID, successor Version **`=1`**, archived predecessor, confirmed lifecycle receipts **and** full report bindings.
- verify recovery **after** partial publication reuses the reserved ID **without** a new Agent dispatch; stale source, changed Scope Unit **or** conflicting destination bytes interrupt rather than overwrite.
- record uncertainty **after** dispatch intent with no accepted output, **without** silently rerunning the Agent.
- verify failure **and** interruption remain observable through status, shared Journal **and** full reports.
