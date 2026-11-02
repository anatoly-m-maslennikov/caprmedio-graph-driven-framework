---
current_scope_unit: caprmedio
status: Done
author: Anatoly Maslennikov
version: 5
updated_at: 2026-11-02 15:49:28 +0400
subjects:
  governs: Entity
atom_id: CA-A-1307
content_role: Analysis & Advisory
type: Spec Proposal
tier: 3
relations: {}
---
## Summary

Derive IS_DEFINED_BY from Definition governance

## Proposal

IS_DEFINED_BY is a derived relation. The defining Requirement remains authoritative; its reverse ownership view is computed rather than stored a second time.

## Context

Approved by the Operator on 2026-10-29 14:40:00 +0400. [CA-P-2696](../../03_plan/CA-P-2694-EPIC--entity-graph-refactor-stage-4-polishing/02-CA-P-2696-TASK--establish-one-defining-requirement-per-model-entity.md) owns adoption and correction. The Current graph is not yet asserted to satisfy uniqueness: 24 exact-Governs groups have multiple Definition candidates. The Definition-family question is resolved: Relation Definition counts through its specialized template. The main Relation is defined once; the derived counterpart reuses it through a short reference. Subtype restructuring is deferred. Drafts remain unadopted while shared-declaration and competing ownership are reviewed.

## Drafts

- [CA-R-2278 Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-P-2696-definition-ownership/CA-R-2278@1-draft-CORE_META_MODEL-RULE--require-exactly-one-defining-requirement-per-model-entity.md)
- [CA-R-2279 Draft](../../101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/draft/CA-P-2696-definition-ownership/CA-R-2279@1-draft-CORE_META_MODEL-RELATION_DEFINITION--define-derived-is-defined-by-relation.md)

## Accepted clarification

- [CA-A-1308](CA-A-1308-SPEC_PROPOSAL--relation-definition-template-counts-as-entity-definition.md)
- [CA-A-1309](CA-A-1309-SPEC_PROPOSAL--define-main-relation-once-and-reference-derived-counterpart.md)
