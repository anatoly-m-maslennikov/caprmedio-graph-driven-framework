---
atom_id: CA-R-1990@11
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Enabled Relations.Contains'
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom.Enabled Relations.Contains
relations:
  child_of:
  - CA-R-1945
version: 11
updated_at: 2026-10-29 07:45:28 +0400
tier: 3
type: Rule
---
## Summary

Enable containment for Plan Atoms

## Claim scope

Containment capability of Plan Atoms.

## Claim

`Atom/Content Role: Plan.Enabled Relations.Contains` **must** be True. a Plan Atom **may** contain other Plan Atoms.

## Details

Plan labels such as Epic, Task and Version do not create different containment Types. Containment is optional and can nest. This permission does not implement a Plan projection or replace other typed relations between Plans.
