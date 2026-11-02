---
subjects:
  active: CFEL <+ Relation
  passive:
  - Entity
  - Projection/(.Form:=Applicable Methodology)
  - Projection
version: 34
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-R-1246
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Keep relation vocabularies graph-specific

## Claim scope

Relation Types, their shared Project identities, and any applicable Entity Definition constraints in CAPRMEDIO Graphs.

## Claim

Relation Type names are shared across CAPRMEDIO Graphs and unique within the Project. A Relation Type is not owned by a graph kind. Existing Entity Definition constraints, where applicable, supply graph-specific endpoint classes, endpoint graph contexts, cardinality, permissions, and prohibitions for that shared Type. They do not create graph-owned Type copies or impose a new per-Type/per-graph admission registry; this contract chooses neither default allow nor default deny.

instances of the same graph kind governed by the same Applicable Methodology **must** reuse the same defining Relation Type authority and any applicable Entity Definition constraints. Matching names identify the shared Type; they do not create interchangeable copies or erase graph-specific constraints.

where an Entity Definition constraint applies, it determines graph-specific endpoint constraints, **not** a requirement that all endpoints occupy the same graph. admitted cross-graph endpoints and source references under CA-R-1472 retain their endpoint identity and source traceability. another graph **may** represent a source-traceable reference **or** view of the Relation **without** creating a graph-specific Type copy.
