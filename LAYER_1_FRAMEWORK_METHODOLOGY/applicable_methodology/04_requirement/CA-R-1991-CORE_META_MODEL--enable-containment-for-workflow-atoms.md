---
atom_id: CA-R-1991
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Workflow.Enabled Relations.Contains"
  depends_on:
  - "Entity/Node/Continuant/Atom.Enabled Relations.Contains"
  - "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step"
relations:
  child_of:
  - CA-R-1945
version: 3
updated_at: "2026-10-19 15:54:17 +0400"
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1991-CORE_META_MODEL--enable-containment-for-workflow-atoms.md
  source_atom_id: CA-R-1991
  source_atom_revision: 3
  source_sha256: cc10bf6cd5e3a5804290cf2537b49ca4449099bbb0bf0357e726834e79b3df2a
  original_relations_sha256: 2fc855d77171d79c5f946e04ce0f770d15c7c80d8f7c81f058e114045a6a5f49
---
# Summary

Enable containment for Workflow Atoms

## Scope

Containment capability of Workflow Atoms.

## Claim

`Atom/Content Role: Operations/Type: Workflow.Enabled Relations.Contains` **must** be True. a Workflow Atom **may** contain Step Atoms.

## Details

The Workflow remains an Atom. Its Steps retain their own definitions and Action references. This permission does not copy shared Actions into a Workflow or replace its declared control flow with folder order.
