---
subjects:
  governs: 'Subject/Graph Relation/Type: CONTAINS'
  depends_on:
  - 'Subject/Graph Relation/Type: IS_DERIVED_RELATION_OF'
  - Subject/Graph Node/Domain/Continuant/Atom.Enabled Relations.Contains
  - Subject/Graph Node/Domain/Continuant/Scope Unit
version: 21
updated_at: 2026-10-26 05:27:27 +0400
relations: {}
atom_id: CA-R-1368@21
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Definition
---
# Summary

Define Containment Relation Pair

## Scope

The `CONTAINS` and `IS_CONTAINED_BY` Relation Type instances, and direct
containment links that use that pair.

## Claim

`CONTAINS` **IS_DERIVED_RELATION_OF** `IS_CONTAINED_BY` between Relation Type
instances.

the Containment Relation Pair **means** direct relation `IS_CONTAINED_BY` from a
contained entity to its containing entity **and** inverse-derived relation
`CONTAINS` from the containing entity to the contained entity.

## Details

IS_CONTAINED_BY is the direct child-to-parent direction; CONTAINS is its derived
inverse and is not independently authored. For this pair, the derived CONTAINS
link reverses the endpoints of the stored IS_CONTAINED_BY link.

Endpoint permissions are separate constraints, not part of this definition. Existing Scope Unit capability is described by CA-R-1757; CA-R-1656, CA-R-1756 and CA-R-1660 govern parent cardinality, immediate ownership and structural-parent direction. Atom containment capability and its default are governed by CA-R-1945, with the existing Plan, Workflow and Step permissions in CA-R-1990, CA-R-1991 and CA-R-1992. Their formal Graph Rule migration remains separate. Containment does not make a contained Atom part of the containing Atom's Substance or change its owning Scope Unit. This definition does not implement or require a construction graph projection.

