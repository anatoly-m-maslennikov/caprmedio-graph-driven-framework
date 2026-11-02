---
atom_id: CA-R-1991@4
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Entity/Node/Continuant/Atom/Content Role: Operations/Type: Workflow.Enabled Relations.Contains'
  depends_on:
  - Entity/Node/Continuant/Atom.Enabled Relations.Contains
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
relations:
  child_of:
  - CA-R-1945
version: 4
updated_at: 2026-10-23 03:06:32 +0400
---
# Summary

Enable containment for Workflow Atoms

## Scope

Containment capability of Workflow Atoms.

## Claim

`Atom/Content Role: Operations/Type: Workflow.Enabled Relations.Contains` **must** be True. a Workflow Atom **may** contain Step Atoms.

## Details

The Workflow remains an Atom. Its Steps retain their own definitions and Action references. This permission does not copy shared Actions into a Workflow or replace its declared control flow with folder order.
