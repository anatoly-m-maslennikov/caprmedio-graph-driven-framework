---
atom_id: CA-R-1990
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Continuant/Node/Atom/Content Role: Plan.Enabled Relations.Contains"
  depends_on:
  - "Entity/Continuant/Node/Atom.Enabled Relations.Contains"
relations:
  child_of:
  - CA-R-1945
version: 2
updated_at: "2026-10-18 03:34:07 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1990-CORE_META_MODEL--enable-containment-for-plan-atoms.md
  source_atom_id: CA-R-1990
  source_atom_revision: 2
  source_sha256: bba6f33649b39b90902347b6ae0050838411851187d718ec329d76d20e0a0dc1
  original_relations_sha256: 2fc855d77171d79c5f946e04ce0f770d15c7c80d8f7c81f058e114045a6a5f49
---
# Summary

Enable containment for Plan Atoms

## Scope

Containment capability of Plan Atoms.

## Claim

`Atom/Content Role: Plan.Enabled Relations.Contains` **must** be True. a Plan Atom **may** contain other Plan Atoms.

## Details

Plan labels such as Epic, Task and Version do not create different containment Types. Containment is optional and can nest. This permission does not implement a Plan projection or replace other typed relations between Plans.
