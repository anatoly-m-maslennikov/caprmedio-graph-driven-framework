---
atom_id: CA-A-1305@1
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
tier: 3
version: 1
updated_at: 2026-10-29 07:12:41 +0400
subjects:
  governs: Entity
relations: {}
---
## Summary

Track Entity candidate implementation Questions

## Latest candidate

[CA-A-1302 — Entity graph candidate with four root branches](draft/CA-A-1302@1-draft-SPECIFICATION_PROPOSAL--entity-graph-candidate-with-four-root-branches.md), with A1303/A1304 refinements. The Operator’s latest words override older decisions; implementation evidence uses only the last 48 hours. This proposal tracks every Question created while implementing CA-P-2683.

## Questions and chosen continuation

- [CA-C-605 — Where should Term and Selection belong under Entity?](../01_concern/CA-C-605-QUESTION--where-should-term-and-selection-belong-under-entity.md): Keep the existing persistent Term and Selection classifications under Object/Continuant for this migration. This preserves the latest explicit lower-level tree instead of adding a fifth root. The four-root candidate left their exact placement open; this choice is provisional and does not implement the Terms Graph.

- [CA-C-606 — Does a zero-direct-value property need a value Format?](../01_concern/CA-C-606-QUESTION--does-a-zero-direct-value-property-need-a-value-format.md): For a grouping property with cardinality {0}, state that a direct-value Format is not applicable; define the Formats of its children independently. Do not invent void/list/map as Formats. This reconciles the required property coverage with the approved direct-value semantics.

## Boundaries

The six legacy Graph Rule Subject paths are held for source-specific preservation/retirement during the Definition pass. Missing-ID legacy RMED carriers without Subjects are explicitly unchanged in the Subject-only pass. Neither creates a new entity or requires Engine changes. The Current frontier is 1,100 RMED carriers; 17 legacy records have no explicit Atom ID or Subjects. Existing archived/draft carriers and Engine sources are excluded.
