---
atom_id: CA-P-2694@1
content_role: Plan
type: Plan
label: Epic
current_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
tier: 3
version: 1
updated_at: 2026-10-29 13:34:35 +0400
subjects:
  governs: Entity
relations: {}
---
## Summary

Entity graph refactor stage 4 — polishing

## Objective

Polish the adopted Entity graph: close real dependency-only coverage gaps, correct obsolete Subject paths, and rebuild the affected views from actual Current sources.

## Details

Follow the completed [formal-model migration](CA-P-2683-EPIC--migrate-formal-model-syntax-and-claims.md). Stage 3 is [Subject refinement stage 3](CA-P-2673-EPIC--subject-refinement-stage-3.md); this is the next numbered refinement stage.

The starting boundary is Current Methodology and direct project-local RMED, matching the 1,108 sources of CA-PROJ-014/015/016. Engine RMED/code/runtime, Terms Graph implementation and advanced formulas remain separate. No additional polishing work is silently included; add concrete Tasks as it is identified.

### First Task

- [CA-P-2695 — Fill dependency-only Subject coverage](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/01-CA-P-2695-TASK--fill-dependency-only-subject-coverage.md). Starting observation: 29 exact Subject paths, used in 63 Atom dependencies, have no exact Governs occurrence within the selected sources.

### Accepted Tier clarification

Tier is numeric. `Atom.Tier.Label` is an optional readable label:

| Tier | Label |
| --- | --- |
| 0 | Principle |
| 1 | Core |
| 2 | General |
| 3 | Standard |
| 4 | Detail |

Labels are not required, including for these five numbers. Tiers can continue as 5, 6 and higher without a predefined label. Principle is a Tier Label, not a nonnumeric Tier value: `Atom.Tier: Principle` becomes `Atom.Tier.Label: Principle`. Draft the property Definition and its representation rule as part of the first Task before promoting source corrections.

## Definition of Done

All adopted polishing Tasks are Done or Canceled. Every dependency-only starting row has an explicit source-backed disposition; required Definition/consumer fixes are adopted, and affected Entity views are rebuilt and reviewed. Draft preparation alone is not completion.

## Progress

Planned. No RMED source or projection has been changed by creating this Epic.
