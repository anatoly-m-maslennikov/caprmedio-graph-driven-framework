---
atom_id: "CA-R-1990@draft"
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: "Draft"
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Continuant/Node/Atom/Content Role: Plan.Enabled Relations.Contains"
  depends_on:
  - "Entity/Continuant/Node/Atom.Enabled Relations.Contains"
relations:
  child_of:
  - CA-R-1945
version: 2
updated_at: "2026-10-17 23:25:50 +0000"
---
# Summary

Enable containment for Plan Atoms

## Scope

Containment capability of Plan Atoms.

## Claim

`Atom/Content Role: Plan.Enabled Relations.Contains` **must** be True. a Plan Atom **may** contain other Plan Atoms.

## Details

Plan labels such as Epic, Task and Version do not create different containment Types. Containment is optional and can nest. This permission does not implement a Plan projection or replace other typed relations between Plans.
