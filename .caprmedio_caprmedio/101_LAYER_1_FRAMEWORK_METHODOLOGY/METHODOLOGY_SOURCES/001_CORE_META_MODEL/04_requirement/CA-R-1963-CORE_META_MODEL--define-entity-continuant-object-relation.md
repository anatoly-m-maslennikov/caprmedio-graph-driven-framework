---
atom_id: CA-R-1963
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject/CAPRMEDIO/Graph/Relation
relations:
  child_of:
  - CA-R-1174
version: 10
updated_at: 2026-10-27 20:00:06 +0400
tier: 1
type: Definition
---
# Summary

Define Entity/Continuant/Object/Relation

## Scope

typed connections between identified endpoints.

## Claim

a Relation **means** a typed connection between identified endpoints. its shared Relation Type and defining authority determine the connection's meaning and declared direction; any applicable Graph Rules supply endpoint, graph-context, **and** cardinality constraints.

## Details

CA-R-806 and CA-R-1246 govern shared Relation Type naming and meaning and any applicable Graph Rule constraints; CA-R-1437 governs source authority; CA-R-1472 governs endpoint identity and contexts. This definition adds no Relation Type, inferred connection or endpoint permission.
