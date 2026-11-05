---
atom_id: CA-A-1262
ref_id: CA-A-1262
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

Keep Substeps as leaves

## Decision

The Operator answered No to recursive Substeps. A Substep cannot contain further Substeps. Workflow >{1..} Step >{0..} Substep is retained. Every Substep is a leaf rather than another grouping level. This resolves the further-nesting part of review gap G-03; it does not create a Substep Run kind or decide unrelated Type admission.

## State

Definition Draft preparation only. Current sources, Workflow instances and Engine implementation are unchanged.
