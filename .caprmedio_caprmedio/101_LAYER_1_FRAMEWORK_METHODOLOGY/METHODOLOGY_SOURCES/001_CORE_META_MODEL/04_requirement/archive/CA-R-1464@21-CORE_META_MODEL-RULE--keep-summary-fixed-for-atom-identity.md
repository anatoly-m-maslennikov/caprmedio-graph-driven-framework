---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Content.Summary
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Object/Continuant/Governing Objects/Atom.ID
  - Entity/Object/Continuant/Governing Objects/Atom.Content
version: 21
updated_at: 2026-10-29 10:13:48 +0400
relations: {}
atom_id: CA-R-1464@21
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Rule
---
## Summary

Keep Summary fixed for Atom identity

## Claim scope

the Summary of an Atom across its Revisions.

## Claim

an Atom **must** keep the Summary created with it across **all** of its Revisions. **if** its Summary needs a change, **then** it **must** be replaced by a new Atom with a new Atom ID, even **if** its Claim is unchanged.
