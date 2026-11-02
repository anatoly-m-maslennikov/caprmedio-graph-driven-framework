---
atom_id: CA-A-1252@1
content_role: Analysis
type: Specification Proposal
status: Archived
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
subjects:
  governs: Formal Model
version: 1
updated_at: 2026-10-28 20:51:13 +0400
relations: {}
tier: 3
---
# Summary

Require Code Units inside Modules

## Decision

Module is a file-level Code component. Code Unit is declared inside Module, with Class and Function as narrower kinds. A Code Unit has no independent declaration directly under Code. Continuant classification can reference the same kind without permitting independent existence.

## State

This resolves the earlier unnecessary Module-versus-direct-Code question. It does not settle the separate alternatives for a Module contained by Code or Package. Draft refinement only.
