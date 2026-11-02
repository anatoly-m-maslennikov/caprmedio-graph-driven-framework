---
atom_id: CA-P-2694@23
content_role: Plan
type: Plan
label: Epic
current_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
tier: 3
version: 23
updated_at: 2026-10-29 21:35:28 +0400
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

The boundary is Current Methodology and direct project-local RMED, now 1,256 sources in CA-PROJ-014/015/016. Engine RMED/code/runtime, Terms Graph implementation and advanced formulas remain separate. No additional polishing work is silently included; add concrete Tasks as it is identified.

### First Task

- [CA-P-2695 — Fill dependency-only Subject coverage](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/01-CA-P-2695-TASK--fill-dependency-only-subject-coverage.md). Starting observation: 29 exact Subject paths, used in 63 Atom dependencies, have no exact Governs occurrence within the selected sources.

### Accepted Tier clarification

Tier is numeric. `Atom.Tier.Label` is an optional readable label:

| Tier | Label |
| --- | --- |
| 0 | Scope Contract |
| 1 | Core |
| 2 | General |
| 3 | Standard |
| 4 | Detail |

Labels are not required, including for these five numbers. Tiers can continue as 5, 6 and higher without a predefined label. Scope Contract is the accepted Tier-0 label, replacing Principle. Store `tier: 0` and carry `SCOPE_CONTRACT` in the filename; do not add a Scope Contract Type or repurpose Atom.Label. Draft the property Definition and its representation rule as part of the first Task before promoting source corrections.

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

P2695–P2698 are Done. Current-source readback gives one canonical Definition for each of 336 logical kind/property entities and 33 named Relation Types. The three projections were rebuilt from 1,256 Current sources. [Result and weak fits](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/definition-polishing-result.md) records changes, reviews and limits. The Epic remains Active as requested.

### Final execution clarification

One canonical R/Entity Definition for every logical model Entity, including Aspects. A scope-specific R can add requirements or constraints but is not a competing Entity Definition. Preserve one coherent Claim per Atom. Do not invent separate entities for every nuance. Report where a dedicated Definition fits badly. The Relation Definition template remains eligible; derived counterparts use short references, not duplicated full meaning. No subtype hierarchy is introduced.

[CA-A-1311](../02_analysis/CA-A-1311-SPEC_PROPOSAL--one-canonical-entity-definition-with-additional-scoped-requirements.md) records the latest decision. The Epic remains Active.

### Inherited Definitions

Definitions inherit through / specialization and // instantiation. A narrower kind reuses the broader Definition and states only its differences. An instance follows its kind Definition and states only instance facts. Common meaning, properties and constraints are reused, not copied. Containment > adds no inheritance. Atom/Content Role: Method is an Atom with Content Role Method; it does not repeat the Atom Definition.

[CA-A-1312](../02_analysis/CA-A-1312-SPEC_PROPOSAL--inherit-base-definitions-and-state-only-differences.md) records this clarification.

### Current placement review

[CA-P-2699](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/05-CA-P-2699-TASK--review-current-atom-placement-between-methodology-and-engine.md) is Active. Review all Current authoritative source Atoms cheaply with Luna for Methodology/Engine placement and an existing Engine Scope Unit. This is a review-only scope expansion: it does not authorize live moves, content rewrites, Engine implementation, or Draft/archive migration. All Content Roles are included in the census; genuinely project-local/control and mixed cases remain explicit rather than being forced into the wrong group.

### Placement review focus correction

The Operator deferred the cross-cutting Plan question and confirmed RMEDO as the focus. P2699 now reviews 2,443 Current RMEDO sources. C/A/P results and legacy Implementation carriers are parked; no move or content migration is authorized. The broader census remains acquisition evidence only.

### RMEDO placement review completed

P2699 is Done: 2,443 Current RMEDO sources reviewed with Luna; 418 move candidates and 49 uncertain/split cases are recorded in the [placement result](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/rmedo-placement-review.md). Engine destinations use the existing registered Scope Units. C/A/P placement and the cross-cutting Plan question are deferred. This completes review only: no RMEDO moves or content rewrites were performed, and the nine new Drafts remain unpromoted. The Epic stays Active.

### Workflow placement correction

Latest Operator decision: general Workflows for operating Atoms, Projections, Journal and implementation belong to CORE_META_MODEL. Local/Public Release are project-specific, so their definitions belong to project-level configuration. Runtime/code implementing Workflows remains Engine. P2699 is reopened to correct the review and counts; the blanket all-O-to-Project-Configuration proposal is superseded. No actual sources have moved.

### Scope Definition and Summary trial

[P2700](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/06-CA-P-2700-TASK--trial-scope-definitions-and-summary-coherence-on-one-hundred-atoms.md) tests exactly 100 Current sources, including all 47 Goals, with Terra at high effort. Candidate Scope Definitions absorb standing responsibilities and related outcomes; specific constraints can remain additional Rs. Atom coherence is tested by a Summary that covers the whole meaning, not a one-predicate-per-file rule. Compare 70 and 100 characters before adopting a limit. Current Atoms remain unchanged.

### Corrected Workflow placement review completed

P2699 is Done after rechecking 187 O definitions and 186 related RMED contracts. The latest rule is Core business meaning, Engine technical realization and Project-specific Release orchestration with cross-scope Step calls. The [updated review](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/rmedo-placement-review.md) replaces prior move counts. The census now also includes the Operator-owned Project Goal outside role folders: 2,444 Current RMEDO sources. Actual moves remain zero; P2700 separately trials Scope Definitions and Summary coherence.

### Scope Definition trial completed — adoption undecided

P2700 is Done for trial review and Draft preparation: 100 Current sources including all 47 Goals produced 103 candidate units and one supporting Definition Draft. The Goal conversion yields 22 Scope Definitions plus 26 supplementary Requirements, not a mechanical relabel. All candidate Summaries fit the experimental 100-character ceiling; 42 have an established equally faithful ≤70-character alternative. See the [result](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/scope-trial-100-result.md) and its thin Draft index. Current RMEDO remains unchanged; no promotion or Goal retirement is authorized by this trial. The Epic remains Active pending the adoption decision and other open Draft work.

### Scope Contracts replace the separate Principle concept

[A1313](../02_analysis/CA-A-1313-SPEC_PROPOSAL--goals-outside-and-scope-contracts-at-tier-zero.md) records the latest decision: Goal outside; RMEDO Scope Contracts inside at Tier 0; Tier 1+ specialization. Project Principles become the same local contract pattern, not an exception. [P2701](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/07-CA-P-2701-TASK--adopt-goals-outside-and-tier-zero-scope-contracts.md) handles the concrete Goal/Core classifications, model/template Drafts, retirement, review, adoption and rebuild. This supersedes the R-only Scope Definition / Goal-retirement direction and the earlier Principle Tier label. P2700 remains completed trial evidence; its Drafts are not automatically adopted. The Epic remains Active.

### Scope Contract naming simplification

Latest Operator correction: Scope Contract is the readable label for numeric Tier 0, not a new RMEDO Atom Type or Atom.Label. Existing Types remain; an O Atom can remain Workflow, Action or Step. Tiers 1–4 keep Core, General, Standard and Detail, with no mandatory names for 5+. A1313 and P2701 are updated; the short-lived five-Type proposal is superseded before any Type Draft was created. Goal/Core classifications and model Draft preparation continue under the simpler label model.

### Final Scope Contract representation and serving relations

P2701 uses `tier: 0` and the filename token `SCOPE_CONTRACT`; Content Role, Type and Atom.Label remain separate. The Operator also admits appropriate typed same-Scope MEDO Tier-0 → R Tier-0 serving relations. This exception does not allow arbitrary equal-Tier edges or reverse R→MEDO / R→R / MEDO→MEDO equal-Tier governance. Review Core promotion links and update governing methodology and Evaluations together. A1313 records the accepted decisions.

### Scope Contract Draft package prepared

P2701 has 81 actual Drafts under the final Tier-0/SCOPE_CONTRACT filename model, preserving existing Types including O/Workflow. The [adoption package](CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/scope-contract-adoption.md) records review corrections, Goal/Core decisions, eight new-identity/rebinding prerequisites and holds. Current Principle retirement, source promotion/moves and graph rebuild remain pending a coherent publication packet. No Current RMEDO or Engine code/runtime changed. The Epic stays Active.
