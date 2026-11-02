---
atom_id: CA-R-1987@5
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Graph/Relation.Target Reference
relations:
  child_of:
  - CA-R-1174
version: 5
updated_at: 2026-10-24 00:38:25 +0400
tier: 3
---
# Summary

Define Relation.Target Reference

## Scope

the target endpoint of a Relation.

## Claim

Relation.Target Reference **means** the reference to the endpoint to which the Relation's declared direction points.

## Details

Candidate #5 includes Source Reference and Target Reference as Relation properties. CA-R-1017 gives a concrete directed relation; CA-R-1472 governs endpoint admission and CA-D-268 governs target serialization for authored Atom relations. This definition changes no endpoint eligibility, direction, cardinality or storage syntax.
