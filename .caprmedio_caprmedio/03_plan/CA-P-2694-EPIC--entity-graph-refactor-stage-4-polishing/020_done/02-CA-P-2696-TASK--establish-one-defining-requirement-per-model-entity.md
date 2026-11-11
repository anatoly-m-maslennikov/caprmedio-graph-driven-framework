---
atom_id: CA-P-2696
ref_id: CA-P-2696
container:
  atom: CA-P-2694
role: Plan
form: Plan
label: Task
topics:
  main_subject: Entity
tier: 4
relations:
  BLOCKS:
  - CA-P-2697
status: Done
version: 7
updated_at: 2026-10-29 17:18:14 +0400
current_scope_unit: caprmedio
author: Anatoly Maslennikov
carrier_destination:
  file:
    name: 02-CA-P-2696-TASK--establish-one-defining-requirement-per-model-entity.md
    path: .caprmedio_caprmedio/03_plan/CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/020_done
---
## Summary

Establish one defining Requirement per model Entity

## Objective

Every declared Object, Carrier and Graph Syntax entity has exactly one global defining R/Entity Definition; scope-specific Rs may constrain but not redefine it. Aspects also retain one canonical Definition; their additional requirements may differ by scope. Other Rs may constrain or refer to the Entity without becoming additional defining Atoms. IS_DEFINED_BY is a derived relation, not another stored link.

## Details

The stronger check is separate from P2695's dependency-only coverage. Actual source readback finds 337 primary-kind/property paths: 180 have one exact-Governs R/Entity Definition, 24 have multiple candidates, and 133 are currently supplied through shared/formal declarations rather than an exact governing Definition. The last count is not automatically 133 missing Definitions.

Review [the thin duplicate table](../definition-ownership-duplicates.tsv). Distinguish an actual Entity Definition from a Rule, a reference, a field constraint or a supporting clause. Preserve useful content and consumers. Reuse/consolidate the defining source before adding new Atoms; avoid duplicate field schemas merely to satisfy a text match. Do not choose ownership by timestamp, Tier, list order or an arbitrary first match.

Derive IS_DEFINED_BY from the qualifying defining Requirement's governing link. Keep source authority in the defining R; do not store a duplicate reverse relation. The Operator confirmed that Relation Definition counts through its specialized Entity Definition template. Keep the current Types; subtype restructuring is deferred. Define the main direction once and retain only a short derived-counterpart reference to it. Also make ownership of entities introduced in shared formal declarations explicit before calling the derived view unambiguous.

Prepare/review Draft corrections and Definition/relation RMED, apply the agreed ownership fixes, rebuild views, and independently verify exactly one owner for every in-scope model Entity. Keep actual Scope Unit/Action instances distinct from definitions of their kinds. Terms Graph implementation and Engine/code migration remain separate.

### Execution sequence

1. Review all 24 multiple-Definition groups and the confirmed shared/formal cohort. The Operator confirmed all 133 shared/formal cases. The starting cohort is all 337 parsed model paths: 180 one-exact-Definition, 24 multiple-candidate groups and 133 shared/formal cases. One canonical R/Entity Definition for every logical model Entity, including Aspects. A scope-specific R can add requirements or constraints but is not a competing Entity Definition. Preserve one coherent Claim per Atom. Do not invent separate entities for every nuance. Report where a dedicated Definition fits badly. The Relation Definition template remains eligible; derived counterparts use short references, not duplicated full meaning. No subtype hierarchy is introduced.
2. Draft and apply the supported ownership corrections so every selected Entity has exactly one defining R. Reuse existing defining sources where they genuinely define the entity; otherwise give the logical entity one dedicated Definition. Inherited / and // Definitions state only distinctions, not copies of the base. Do not create a Definition per runtime occurrence.
3. Hand off the fixed entity list and canonical defining IDs to [CA-P-2697](03-CA-P-2697-TASK--review-combined-entity-definitions-for-coherence-and-conflicts.md). That task reviews the combined 180 original entities plus the repaired groups.
4. Apply the subsequent coherence/conflict fixes through [CA-P-2698](04-CA-P-2698-TASK--fix-definition-review-findings-and-recheck-the-graph.md).

Use Luna for inventories, grouping, mechanical Draft edits and checks. Use Terra for Definition-vs-Rule judgments, meaning preservation and independent review. Parent owns publication, shared Journal and integration; workers use disjoint scopes and thin trackers.

## Definition of Done

The Definition-family and derivation semantics are explicit; each selected logical Entity has one unambiguous defining R; no competing Definition is hidden by projection filtering. Applicable Rules/references remain distinct, required consumers are repaired, and the source-backed graph and derived ownership view pass readback.

## Progress

Done — actual-source readback establishes exactly one canonical Definition for all 336 original logical kind/property entities and all 33 named Relation Types. The complete original 337 raw paths, including all 133 shared cases, were preserved in the audit. Published 75 successors with archives and 145 new Atoms. Definitions inherit through / and // and state only differences; > adds no inheritance.

See [definition polishing result](../definition-polishing-result.md).
