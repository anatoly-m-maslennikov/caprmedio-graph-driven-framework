---
atom_id: CA-E-532
ref_id: CA-E-532
container:
  scope_unit: CA-SU-20
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Quality/Verification/Dynamic Testing
tier: 3
status: Archived
version: 13
updated_at: 2026-11-09 07:45:14 +0400
carrier_destination:
  file:
    name: CA-E-532@13-APPS-EVAL_CASE--verify-orchestrator-authority-and-recovery-boundaries.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/06_evaluation/archive
current_scope_unit: APPS
author: Anatoly Maslennikov
---

## Summary

Verify orchestrator authority and recovery boundaries

## Claim

### Prose Claim

This retained contract applies only when AI-Agent execution is separately admitted. It does not enable that execution or claim that its runtime implementation is present.

the Evaluation **must** verify rejection of orchestration requests **or** Agent output outside declared authority.

## Details

### Scope

WORKFLOW_ORCHESTRATOR's initial local execution capability.

- reject unsupported Workflows, traversal, symlinks, protected paths, unknown fields, stale input **and** conflicting duplicate Run requests.
- check phases cannot modify source Atoms; allow_fixes=false preserves source bytes.
- reject Agent-assigned successor IDs, undelegated Summary changes, low confidence, incomplete checks **and** invalid report fields.
- **with** allow_replacements=true **and** fix permission, verify the new unreused ID, successor Version **`=1`**, archived predecessor, confirmed lifecycle receipts **and** full report bindings.
- verify recovery **after** partial publication reuses the reserved ID **without** a new Agent dispatch; stale source, changed Scope Unit **or** conflicting destination bytes interrupt rather than overwrite.
- record uncertainty **after** dispatch intent with no accepted output, **without** silently rerunning the Agent.
- verify failure **and** interruption remain observable through status, shared Journal **and** full reports.
