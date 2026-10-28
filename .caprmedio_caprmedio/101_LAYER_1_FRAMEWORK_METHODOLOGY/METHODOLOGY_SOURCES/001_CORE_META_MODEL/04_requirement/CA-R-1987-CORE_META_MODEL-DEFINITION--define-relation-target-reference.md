---
atom_id: CA-R-1987
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject/CAPRMEDIO/Graph/Relation.Target Reference
relations:
  child_of:
  - CA-R-1174
version: 9
updated_at: 2026-10-27 20:00:07 +0400
tier: 3
type: Definition
---
# Summary

Define Relation.Target Reference

## Scope

the target endpoint of a Relation.

## Claim

Relation.Target Reference **means** the reference to the endpoint to which the Relation's declared direction points.

## Details

Candidate #5 includes Source Reference and Target Reference as Relation properties. CA-R-1017 gives a concrete directed relation; CA-R-1472 governs endpoint admission and CA-D-268 governs target serialization for authored Atom relations. This definition changes no endpoint eligibility, direction, cardinality or storage syntax.
