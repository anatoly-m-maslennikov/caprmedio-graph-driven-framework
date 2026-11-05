---
atom_id: CA-A-1252
ref_id: CA-A-1252
role: Analysis & Advisory
form: Specification Proposal
status: Done
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
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

Require Code Units inside Modules

## Decision

Module is a file-level Code component. Code Unit is declared inside Module, with Class and Function as narrower kinds. A Code Unit has no independent declaration directly under Code. Continuant classification can reference the same kind without permitting independent existence.

## State

This resolves the earlier unnecessary Module-versus-direct-Code question. It does not settle the separate alternatives for a Module contained by Code or Package. Draft refinement only.
