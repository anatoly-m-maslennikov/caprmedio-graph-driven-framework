---
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan'
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan'
  - Entity/Object/Continuant/Governing Objects/Atom.Content.Summary
  - Entity/Object/Continuant/Governing Objects/Atom.Content
version: 23
updated_at: 2026-10-29 07:45:27 +0400
relations: {}
atom_id: CA-R-1575@23
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
## Summary

Require work or decomposition in every Plan

## Claim scope

Plan Atoms, their own work, and their direct Plan containment.

## Claim

**every** Plan Atom **must** have **`>=1`** of:

- its own work content;
- **`>0`** outgoing derived `CONTAINS` links **to** directly contained Plan Atoms.

both contributions **may** be present within the same Claim; a Summary alone **without** either contribution is insufficient.

## Details
