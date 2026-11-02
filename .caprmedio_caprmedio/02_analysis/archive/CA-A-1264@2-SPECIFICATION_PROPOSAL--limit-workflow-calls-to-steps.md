---
atom_id: CA-A-1264@2
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Formal Model
version: 2
updated_at: 2026-10-29 21:51:04 +0400
relations: {}
tier: 3
---
# Summary

Limit Workflow calls to Steps

## Decision

The Operator selected Workflow calls only in Steps. A Substep calls exactly one Action with parameters; it cannot call a Workflow and cannot contain further Substeps. Step and Substep remain distinct kinds. The choice between Action and Workflow targets belongs only to a leaf Step. A containing Step runs its declared Substeps and makes no call of its own.

## State

Definition Draft preparation only. Current sources, Workflow instances and Engine implementation are unchanged.
