---
atom_id: CA-R-1991@12
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow.Enabled Relations.Contains'
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom.Enabled Relations.Contains
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
relations:
  child_of:
  - CA-R-1945
version: 12
updated_at: 2026-10-29 07:45:28 +0400
tier: 3
type: Rule
---
## Summary

Enable containment for Workflow Atoms

## Claim scope

Containment capability of Workflow Atoms.

## Claim

`Atom/Content Role: Operations/Type: Workflow.Enabled Relations.Contains` **must** be True. a Workflow Atom **may** contain Step Atoms.

## Details

The Workflow remains an Atom. Its Steps retain their own definitions and Action references. This permission does not copy shared Actions into a Workflow or replace its declared control flow with folder order.
