---
atom_id: CA-R-1990@6
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan.Enabled Relations.Contains'
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Enabled Relations.Contains
relations:
  child_of:
  - CA-R-1945
version: 6
updated_at: 2026-10-24 01:37:42 +0400
tier: 3
type: Rule
---
# Summary

Enable containment for Plan Atoms

## Scope

Containment capability of Plan Atoms.

## Claim

`Atom/Content Role: Plan.Enabled Relations.Contains` **must** be True. a Plan Atom **may** contain other Plan Atoms.

## Details

Plan labels such as Epic, Task and Version do not create different containment Types. Containment is optional and can nest. This permission does not implement a Plan projection or replace other typed relations between Plans.
