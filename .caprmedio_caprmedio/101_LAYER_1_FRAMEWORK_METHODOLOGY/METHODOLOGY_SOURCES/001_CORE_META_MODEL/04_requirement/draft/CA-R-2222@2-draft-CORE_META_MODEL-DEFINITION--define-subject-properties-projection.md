---
atom_id: CA-R-2222@2-draft
content_role: Requirement
type: Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Subject Graph Properties'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection
relations:
  depends_on:
  - CA-R-2150
tier: 2
version: 2
updated_at: 2026-10-28 02:55:02 +0400
---
# Summary

Define Subject Properties Projection

## Claim

A Subject Graph Properties Projection **means** a flat list of the selected primary Subjects that have at least one direct or source-backed inherited property, with each Subject's property hierarchy beneath it. Include inherited properties and allowed values with the mark [inherited]. A classification axis does not acquire its bearer's properties merely by being an intermediate path segment; qualified narrower kinds inherit from their actual broader kind. Do not include a separate primary hierarchy, named-instance inventory or copied definition text.

Containment through `CONTAINS`, displayed as `>`, does not establish specialization or property inheritance. In particular, Project Model contains Actor; Actor does not inherit Project Model properties through that link. Organizational display ancestry alone supplies no inheritance route.
