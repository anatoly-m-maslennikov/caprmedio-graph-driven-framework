---
atom_id: CA-R-1986@8
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Graph Relation.Source Reference
relations:
  child_of:
  - CA-R-1174
version: 8
updated_at: 2026-10-25 17:32:27 +0400
tier: 3
type: Definition
---
# Summary

Define Relation.Source Reference

## Scope

the source endpoint of a Relation.

## Claim

Relation.Source Reference **means** the reference to the endpoint from which the Relation's declared direction starts.

## Details

Candidate #5 includes Source Reference and Target Reference as Relation properties. CA-R-1017 gives a concrete directed relation; CA-R-118 and CA-D-268 establish directional ownership and serialized target references for authored Atom relations. Source Reference identifies an endpoint, not the evidence or authority supporting the relation. No reference encoding is prescribed here.
