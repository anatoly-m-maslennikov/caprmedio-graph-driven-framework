---
atom_id: CA-A-1229
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject
version: 2
updated_at: 2026-10-27 22:47:33 +0400
relations: {}
tier: 3
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
