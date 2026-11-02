---
atom_id: CA-P-2694@10
content_role: Plan
type: Plan
label: Epic
current_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
tier: 3
version: 10
updated_at: 2026-10-29 17:07:33 +0400
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

The boundary is Current Methodology and direct project-local RMED, currently 1,111 sources in CA-PROJ-014/015/016. Engine RMED/code/runtime, Terms Graph implementation and advanced formulas remain separate. No additional polishing work is silently included; add concrete Tasks as it is identified.

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

### Remaining ordered work

1. [P2696 — Review competing/shared Definitions and establish exactly one owner](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/02-CA-P-2696-TASK--establish-one-defining-requirement-per-model-entity.md). Start with the 24 multiple-candidate groups and the confirmed shared/formal cohort. The Operator confirmed all 133 shared/formal cases. The starting cohort is all 337 parsed model paths: 180 one-exact-Definition, 24 multiple-candidate groups and 133 shared/formal cases. One canonical R/Entity Definition for every logical model Entity, including Aspects. A scope-specific R can add requirements or constraints but is not a competing Entity Definition. Preserve one coherent Claim per Atom. Do not invent separate entities for every nuance. Report where a dedicated Definition fits badly. The Relation Definition template remains eligible; derived counterparts use short references, not duplicated full meaning. No subtype hierarchy is introduced.
2. [CA-P-2697 — Review the combined Entity Definitions for coherence and conflicts](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/03-CA-P-2697-TASK--review-combined-entity-definitions-for-coherence-and-conflicts.md). Review all 180 original one-Definition entities together with the fixed 24 groups and fixed shared/formal cohort. Check meanings, scopes, formal/prose agreement, properties, inheritance and relations as one model.
3. [CA-P-2698 — Fix findings, rebuild and recheck](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/04-CA-P-2698-TASK--fix-definition-review-findings-and-recheck-the-graph.md). Apply reviewed Draft corrections and verify the combined model again. Do not automatically close this Epic.

### Accepted definition rules and delegation

Every logical Entity has one canonical defining R, including Objects, Carriers, Graph Syntax, Aspects and their properties. Scoped additional Rs are constraints, not additional Definitions. Scope-specific Rs may constrain an Object but not redefine its meaning. Report where the dedicated-Definition trial fits badly; do not create new entities for every nuance. Relation Definition counts through its specialized template. Define the main relation once and keep its derived counterpart as a short reference, following DRY. IS_DEFINED_BY is derived. Subtype restructuring remains deferred.

Use Luna for deterministic inventories, grouping, mechanical changes and checks; use Terra for semantic analysis, ambiguous Definition ownership, coherence review and independent verification. Keep work in bounded disjoint groups. Parent owns Current publication, shared Journal and integration. Use thin tracking files and immediate Drafts, not large copied-Claim mapping documents.

## Definition of Done

All adopted polishing Tasks are Done or Canceled. Every dependency-only starting row has an explicit source-backed disposition; required Definition/consumer fixes are adopted, and affected Entity views are rebuilt and reviewed. Draft preparation alone is not completion.

## Progress

P2695 dependency-only coverage is complete: 21 Current source successors, 3 new Definitions and rebuilt views over 1,111 sources. All original 29 paths have recorded coverage/correction dispositions. Twenty exact dependency-only paths remain legitimately covered/registered. P2696 is Active for exact-one ownership. The combined coherence review and subsequent repair Tasks are Backlog, in that order; all 133 shared/formal cases are included; global uniqueness is strict for Objects, Carriers and Graph Syntax, and Aspects have canonical Definitions with scoped additional requirements. The Epic stays Active as requested. See [coverage result](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/dependency-coverage-result.md).

### Final execution clarification

One canonical R/Entity Definition for every logical model Entity, including Aspects. A scope-specific R can add requirements or constraints but is not a competing Entity Definition. Preserve one coherent Claim per Atom. Do not invent separate entities for every nuance. Report where a dedicated Definition fits badly. The Relation Definition template remains eligible; derived counterparts use short references, not duplicated full meaning. No subtype hierarchy is introduced.

[CA-A-1311](../02_analysis/CA-A-1311-SPEC_PROPOSAL--one-canonical-entity-definition-with-additional-scoped-requirements.md) records the latest decision. The Epic remains Active.

### Inherited Definitions

Definitions inherit through / specialization and // instantiation. A narrower kind reuses the broader Definition and states only its differences. An instance follows its kind Definition and states only instance facts. Common meaning, properties and constraints are reused, not copied. Containment > adds no inheritance. Atom/Content Role: Method is an Atom with Content Role Method; it does not repeat the Atom Definition.

[CA-A-1312](../02_analysis/CA-A-1312-SPEC_PROPOSAL--inherit-base-definitions-and-state-only-differences.md) records this clarification.
