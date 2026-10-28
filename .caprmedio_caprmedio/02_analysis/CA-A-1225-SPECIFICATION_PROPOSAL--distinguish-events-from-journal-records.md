---
atom_id: CA-A-1225
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

Distinguish Events from Journal records

## Question

How do Event, Occurrent, Event Record and Journal relate?

## Operator decision

- An Event happening in a Runtime is an Occurrent.
- A record about that Event in a Journal is a Continuant.
- A Journal contains Event Records: Journal > Event Record.

The occurrence and its record are different things. The containment statement concerns Journal records, not the actual Events.

## Interpretation boundary

Keep Event as an actual occurrence under the existing Occurrent classification. Do not infer an instantaneous-only Event criterion or a new lifecycle from this answer. The answer establishes the occurrence/record distinction and Journal containment; it does not require a new Subject path for Event Record or merging Event and Occurrent definitions.

## Review disposition

This addresses C10-I04 / C10-G03 with the Operator's intended distinction. Existing Continuant/Occurrent meanings stay settled. C10-I06 / C10-G04 (Runtime boundary), optional Prompts/Documentation clarification, general stale drafting language and Projection source-count correction remain separate items.

## Adoption result

Current R1968@9 and R1745@32 now state the accepted Event/record distinction and Journal containment. R1972 already classified actual Events as Occurrents; its separate editorial correction is recorded in A1228. No narrower Event discriminator or new Subject path was introduced.

[Rebuilt main Subject view](../_projection/CA-PROJ-009-CAPRMEDIO--Subject-Graph--Current-RMEDO.md).
