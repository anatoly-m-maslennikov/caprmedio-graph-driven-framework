---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Summary
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
version: 21
updated_at: 2026-10-27 19:59:58 +0400
relations: {}
atom_id: CA-R-1575
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Require work or decomposition in every Plan

## Scope

Plan Atoms, their own work, and their direct Plan containment.

## Claim

**every** Plan Atom **must** have **`>=1`** of:

- its own work content;
- **`>0`** outgoing derived `CONTAINS` links **to** directly contained Plan Atoms.

both contributions **may** be present within the same Claim; a Summary alone **without** either contribution is insufficient.

## Details
