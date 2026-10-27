---
subjects:
  governs: Subject/Graph Relation/Type
  depends_on:
  - Subject
  - 'Subject/Graph Node/Domain/Continuant/Projection/Type: Applicable Methodology'
  - Subject/Graph Node/Domain/Continuant/Projection
version: 25
updated_at: 2026-10-26 17:20:40 +0400
relations: {}
atom_id: CA-R-1246
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Keep relation vocabularies graph-specific

## Scope

Relation Types, their shared Project identities, and any applicable Graph Rule constraints in CAPRMEDIO Graphs.

## Claim

Relation Type names are shared across CAPRMEDIO Graphs and unique within the Project. A Relation Type is not owned by a graph kind. Existing Graph Rules, where applicable, supply graph-specific endpoint classes, endpoint graph contexts, cardinality, permissions, and prohibitions for that shared Type. They do not create graph-owned Type copies or impose a new per-Type/per-graph admission registry; this contract chooses neither default allow nor default deny.

instances of the same graph kind governed by the same Applicable Methodology **must** reuse the same defining Relation Type authority and any applicable Graph Rules. Matching names identify the shared Type; they do not create interchangeable copies or erase graph-specific constraints.

where a Graph Rule applies, it determines graph-specific endpoint constraints, **not** a requirement that all endpoints occupy the same graph. admitted cross-graph endpoints and source references under CA-R-1472 retain their endpoint identity and source traceability. another graph **may** represent a source-traceable reference **or** view of the Relation **without** creating a graph-specific Type copy.
## Details
