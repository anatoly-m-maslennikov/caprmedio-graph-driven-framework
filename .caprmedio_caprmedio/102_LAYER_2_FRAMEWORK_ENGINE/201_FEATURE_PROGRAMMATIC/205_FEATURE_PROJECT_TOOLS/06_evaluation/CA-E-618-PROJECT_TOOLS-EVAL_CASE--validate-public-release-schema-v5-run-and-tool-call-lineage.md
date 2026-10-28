---
atom_id: CA-E-618
content_role: Evaluation
type: Eval Case
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
version: 10
updated_at: 2026-10-27 19:59:38 +0400
relations:
  evaluation_for:
  - CA-R-1928
tier: 4
---
# Summary

Validate public-release schema-v5 Run and Tool-call lineage

## Scope

the Journal output of one public-release fixture.

## Claim

**the Operator** **must** verify schema-v5 actual Workflow, Step, and Action Run parentage, started and terminal records, and Tool-call evidence references parented to their Step and Action without any Tool Run kind.

## Details

The check rejects source claims of success without durable Run evidence.
