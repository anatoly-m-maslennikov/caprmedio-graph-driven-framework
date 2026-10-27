---
subjects:
  governs: Subject
  depends_on:
  - Subject
  - Subject/Graph Relation
  - Subject/Graph Node/Domain/Continuant/Term
version: 25
updated_at: 2026-10-25 17:32:27 +0400
relations: {}
atom_id: CA-R-1194
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Definition
---
# Summary

Define Subject Path

## Scope

a Subject Path.

## Claim

A Subject Path means a full canonical Subject Expression used by a Subject Relation to identify exactly one canonical Subject Target through its named Term components and registered qualifications. Bare Subject is a valid umbrella; every more-specific path starts at Subject and its next component is exactly Graph Node, Graph Relation, or Graph Rule. Within Graph Node, both Domain and Engineering can contain Continuant and Occurrent target-hierarchy components; those components do not create an extra Entity or target identity. A qualification retains its registered endpoint constraints; the path identifies the target without creating another target identity or becoming the Subject Relation itself.

## Details
