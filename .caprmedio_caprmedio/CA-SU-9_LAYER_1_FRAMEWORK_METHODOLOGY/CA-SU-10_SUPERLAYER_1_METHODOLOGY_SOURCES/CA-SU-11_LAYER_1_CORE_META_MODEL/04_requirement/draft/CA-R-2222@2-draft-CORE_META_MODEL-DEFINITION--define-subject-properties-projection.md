---
atom_id: CA-R-2222@2-draft
ref_id: CA-R-2222@2-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Definition
topics:
  main_subject: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Subject Graph Properties'
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection
tier: 2
relations:
  depends_on:
  - CA-R-2150
status: Draft
version: 2
updated_at: 2026-10-28 16:27:23 +0400
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
---
# Summary

Define Subject Properties Projection

## Claim

A Subject Graph Properties Projection **means** a flat list of the selected primary Subjects that have at least one direct or source-backed inherited property, with each Subject's property hierarchy beneath it. Include inherited properties and allowed values with the mark [inherited]. A classification axis does not acquire its bearer's properties merely by being an intermediate path segment; qualified narrower kinds inherit from their actual broader kind. Do not include a separate primary hierarchy, named-instance inventory or copied definition text.

Organizational membership, displayed as `::`, and structural containment through CONTAINS, displayed as `>`, do not establish specialization or property inheritance. `Project Model::Actor` supplies no Project Model or Scope Unit properties to Actor. Actual specializations such as `Actor/Operator` retain applicable Actor properties. Organizational display ancestry alone supplies no inheritance route. A role-qualified kind such as `Atom/Content Role: Plan` inherits from Atom; its intermediate Content Role axis does not thereby acquire Atom properties.

### Existing-target reference marker

An `@` reference does not change the operator's inheritance behavior. An admitted `/@` specialization preserves applicable properties of its actual broader kind; `::@` membership and `>@` containment supply no inheritance. Referencing a target elsewhere does not create a second property-bearing kind.
