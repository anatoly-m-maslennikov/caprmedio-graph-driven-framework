---
atom_id: CA-R-1991
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow.Enabled Relations.Contains'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Enabled Relations.Contains
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
relations:
  child_of:
  - CA-R-1945
version: 10
updated_at: 2026-10-27 20:00:07 +0400
tier: 3
type: Rule
---
# Summary

Enable containment for Workflow Atoms

## Scope

Containment capability of Workflow Atoms.

## Claim

`Atom/Content Role: Operations/Type: Workflow.Enabled Relations.Contains` **must** be True. a Workflow Atom **may** contain Step Atoms.

## Details

The Workflow remains an Atom. Its Steps retain their own definitions and Action references. This permission does not copy shared Actions into a Workflow or replace its declared control flow with folder order.
