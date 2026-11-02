---
atom_id: CA-P-2687
content_role: Plan
type: Plan
label: Task
current_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Done
subjects:
  governs: Entity
version: 5
updated_at: 2026-10-29 11:24:13 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2683
tier: 4
---
## Summary

Define new Relations and their derived inverses

## Objective

Fill missing Relation Definitions while preserving reusable Type metadata and direct/derived meanings.

## Details

Stage 3 specialist lane under P2691. Adopt/reuse the reviewed Relation structure and named Relation Definitions, then inspect actual admitted relation use for remaining defining gaps. Relation//NAME instances describe reusable Types; real connections have identity (source, Relation Type, target).

Retain canonical meaning, declared direct direction and evidenced derived inverse/transitivity semantics. Store the direct fact once; inverse views are derived. Concrete source/target references belong to a connection, not fixed endpoint values on its reusable Type. Endpoint permissions and structural constraints belong in their appropriate governing Model Definition Claims; do not add a redundant per-Type rules registry.

Use ((RELATION_TYPE)) where no short operator applies. Keep named-relation cardinalities in prose for this scope, preserving exactly-one bindings without inventing counting-direction syntax. Create a missing Definition only when existing Rs cannot supply it. Keep the coverage list shared with P2691 and correct necessary typed consumers as replacements are adopted.

## Definition of Done

All admitted in-scope Relation Types and needed direct/derived meanings have Current R Definitions; real-edge versus Type metadata stays distinct; no duplicate stored inverse or undefined named-relation count suffix remains.

## Progress

Completed 31 named Relation Types through current R/Relation Definition authority, including paired direct and derived names. Literal short notation is declared for /, //, ., :, >; general ((RELATION_TYPE)) is retained. IS_EXECUTION_OF, RECORDS and EXECUTES connect the agreed kinds. Constraints remain in Entity Definitions, not reusable Type metadata. Source review found no lost endpoint constraint.
