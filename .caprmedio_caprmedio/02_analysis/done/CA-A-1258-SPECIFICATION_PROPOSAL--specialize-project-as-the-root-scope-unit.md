---
atom_id: CA-A-1258
ref_id: CA-A-1258
role: Analysis & Advisory
form: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Done
author: Anatoly Maslennikov
topics:
  main_subject: Formal Model
version: 3
updated_at: 2026-11-02 15:49:28 +0400
tier: 3
container:
  scope_unit: CA-SU-00
---
# Summary

Specialize Project as the root Scope Unit

## Decision

Scope Unit/Project is specialization. Project is the single root Scope Unit, without a parent Scope Unit. Project >@(Scope Unit); Scope Unit >@(Scope Unit), >@(Atom), >@(Projection) are structural containment. Project is not a separate sibling kind which merely contains all Scope Units. Scope Unit properties therefore apply to Project through specialization, with the explicit root-parent exception. Project Goal Operator ownership remains unchanged.

## State

Refine proposal and Definition Drafts only. Current source migration remains separate.
