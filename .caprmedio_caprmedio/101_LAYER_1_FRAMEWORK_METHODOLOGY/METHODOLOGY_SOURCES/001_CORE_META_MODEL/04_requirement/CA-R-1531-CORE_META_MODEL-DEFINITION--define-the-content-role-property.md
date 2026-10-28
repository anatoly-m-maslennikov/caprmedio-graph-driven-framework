---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Property
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
version: 17
updated_at: 2026-10-27 19:59:57 +0400
relations: {}
atom_id: CA-R-1531
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Definition
---
# Summary

Define the Content Role Property

## Scope

The Content Role classification of Atoms.

## Claim

Content Role is the classification parameter of an Atom that identifies the primary contribution of its Claim. The parameter has an allowed value, such as Requirement or Plan; it is not a separate entity kind.

Within `Subject/CAPRMEDIO/Graph/Node/Project Model`, `Atom/Content Role` is a valid Subject naming this classification axis. `Atom/Content Role: Requirement` names the narrower Atom kind selected by that value. That narrower kind inherits the properties of Atom. The full canonical Subject retains the namespace and complete path.

## Semantics

A Subject may name a thing or a topic. Having a Subject does not make the named topic a separate entity kind. Defining Content Role therefore does not introduce a Content Role entity between Atom and its role-qualified kinds, and does not remove the classification-axis Subject.

The stored Content Role value classifies a particular Atom. The Subject notation describes the classification axis or a role-qualified Atom kind; it does not assign a value to a particular Atom instance.

## Details

The allowed values and the requirement for one value per Atom remain governed by CA-R-1283 and CA-R-740. This definition does not change those rules.
