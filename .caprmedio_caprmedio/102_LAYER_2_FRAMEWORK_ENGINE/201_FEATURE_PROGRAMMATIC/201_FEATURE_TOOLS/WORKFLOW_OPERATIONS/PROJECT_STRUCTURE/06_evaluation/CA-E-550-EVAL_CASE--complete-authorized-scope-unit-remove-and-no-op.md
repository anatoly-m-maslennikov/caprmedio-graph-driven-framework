---
atom_id: CA-E-550
content_role: Evaluation
type: Eval Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 10
updated_at: 2026-10-27 19:59:37 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
  - Subject/CAPRMEDIO/Carrier
relations: {}
tier: 3
---
# Summary

Complete authorized Scope Unit Remove and no-op

## Scope

Golden remove and no-op cases for one declared unit with affected references and observed Carrier content.

## Claim

The Evaluation **must** prove Remove preserves or reports all affected material and a true no-op performs no mutation.

## Details

- Remove only a declaration whose exact preservation/breakage disposition is authorized; assert every affected Atom, definition, reference, and Carrier is preserved or explicitly returned as breakage.
- Verify neither recursive directory deletion nor implicit Carrier deletion occurs.
- Repeat the already-satisfied request and assert `no_op`, unchanged TOML revision, empty actual effect set, and no fictitious mutation or success evidence.
