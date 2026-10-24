---
atom_id: CA-E-550@3
content_role: Evaluation
type: Eval Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 3
updated_at: 2026-10-23 03:14:50 +0400
subjects:
  governs: Subject/Domain/Node/Continuant/Scope Unit
  depends_on:
  - Subject/Engineering/Project Structure
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Project.Structure
  - Subject/Engineering/Carrier
relations:
  relates_to:
  - CA-R-1662
  - CA-R-1829
  - CA-R-1831
  - CA-R-1832
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
