---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom/(.Role := Plan)
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Plan)
  - CAPRMEDIO <+ MODEL <+ Atom.Content.Summary
  - CAPRMEDIO <+ MODEL <+ Atom.Content
version: 25
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1575
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
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
