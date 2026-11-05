---
atom_id: CA-A-1224
ref_id: CA-A-1224
role: Analysis & Advisory
form: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Done
author: Anatoly Maslennikov
topics:
  main_subject: Subject
version: 3
updated_at: 2026-11-02 15:49:28 +0400
tier: 3
container:
  scope_unit: CA-SU-00
---
# Summary

Move existing Term Subject paths

## Question

Should the existing Term Subjects move with Candidate #10 while Terms Graph work stays deferred?

## Proposal

Move Subject/Graph Node/Domain/Continuant/Term and its existing suffixes to Subject/CAPRMEDIO/Graph/Node/Project Model/Term. Retain existing Term.Name, Term.Type and named Term Subjects without changing their content or definitions. CA-R-1318 already defines Term.

## Decision

Operator: “Move the existing Term Subject paths; keep Terms Graph work deferred.”

## Scope

The fresh inventory contains 196 such references in 174 Current RMEDO Atoms, including 15 governed targets. This decision moves their Subject paths; it does not implement, review or unfreeze the Terms Graph, or create a new definition layer.

## References

- [Candidate #10](CA-A-1218-SPECIFICATION_PROPOSAL--subject-model-candidate-10.md).
