---
atom_id: CA-A-1264
ref_id: CA-A-1264
container:
  scope_unit: CA-SU-00
role: Analysis & Advisory
form: Specification Proposal
topics:
  main_subject: Formal Model
tier: 3
status: Done
version: 3
updated_at: 2026-11-02 15:49:28 +0400
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Limit Workflow calls to Steps

## Decision

The Operator selected Workflow calls only in Steps. A Substep calls exactly one Action with parameters; it cannot call a Workflow and cannot contain further Substeps. Step and Substep remain distinct kinds. The choice between Action and Workflow targets belongs only to a leaf Step. A containing Step runs its declared Substeps and makes no call of its own.

## State

Definition Draft preparation only. Current sources, Workflow instances and Engine implementation are unchanged.
