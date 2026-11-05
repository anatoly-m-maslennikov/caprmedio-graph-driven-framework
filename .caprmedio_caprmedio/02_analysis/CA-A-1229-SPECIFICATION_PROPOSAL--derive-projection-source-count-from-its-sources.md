---
atom_id: CA-A-1229
ref_id: CA-A-1229
role: Analysis & Advisory
form: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
topics:
  main_subject: Subject
version: 3
updated_at: 2026-11-02 15:49:28 +0400
tier: 3
container:
  scope_unit: CA-SU-00
carrier_destination:
  file:
    name: CA-A-1229-CAPRMEDIO-SPECIFICATION_PROPOSAL--derive-projection-source-count-from-its-sources.md
    path: .caprmedio_caprmedio/02_analysis
---
# Summary

Derive Projection source count from its sources

## Question

Should the local generator correct source_count and rebuild the Projection after the accepted corrective Drafts are promoted?

## Operator decision

“okay” to including that correction after the preceding meaning and editorial decisions.

## Correction

C10-I07 / C10-F07: derive source_count from the newly computed unique sources list, then rebuild the Projection from Current sources. The existing local generator replaced sources but inherited the old source_count. Recompute it immediately after constructing sources. Do not hand-edit the derived Projection.

## Scope

One local scratch-generator assignment, normal promotion and predecessor history for the 21 accepted R Drafts, a fresh Current-source inventory and main Subject view rebuild. No production Tool/runtime change, new schema, full property/instance review or new FPF pass.

## Adoption result

All 21 accepted R successors are Current and all 21 predecessors are archived. The local generator recomputes source_count from its freshly constructed sources list. CA-PROJ-009 was rebuilt from 2,273 Current RMEDO sources; source_count and the unique source list both equal 2,273. All 38 defining R references use Current sources. No production Tool or runtime code changed.

[Rebuilt main Subject view](../_projection/CA-PROJ-009-CAPRMEDIO--Subject-Graph--Current-RMEDO.md).
