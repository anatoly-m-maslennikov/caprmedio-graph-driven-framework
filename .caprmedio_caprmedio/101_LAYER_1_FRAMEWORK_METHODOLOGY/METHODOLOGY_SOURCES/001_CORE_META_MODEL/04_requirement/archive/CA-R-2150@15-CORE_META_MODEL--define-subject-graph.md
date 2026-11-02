---
atom_id: CA-R-2150@15
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Entity/Object/Continuant/Projection/(.Type: Subject Graph)'
  depends_on:
  - Entity/Object/Continuant/Projection
  - Entity/Object/Continuant/Projection.Type
  - Entity/Object/Continuant/Selection
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Object/Continuant/Governing Objects/Atom.Subjects
  - Entity/Aspect/Domain
  - Entity/Aspect/Engineering
  - Entity
  - Entity/Object/Continuant/Package/Project Implementation
  - Entity/Object/Occurrent/Runtime
  - Entity/Carrier
version: 15
relations: {}
tier: 1
updated_at: 2026-10-30 17:14:59 +0400
---
## Summary

Define Subject Graph

## Claim scope

the Subject Graph Projection Type under Projection.

## Claim

Subject Graph is a non-authoritative Projection Type that presents readable
canonical Entity Targets from a selected Current RMEDO frontier. Its root is
Entity; its direct branches follow the governing Entity Definition in CA-R-1248, including the proposed Term and Property branches.
Continuant and Occurrent specialize Object; Graph Syntax structurally contains
Relation, Format, and Cardinality. The view is a target hierarchy, not an
Atom-to-Entity link graph or a native graph.

The Projection preserves each selected target's full canonical path and source
provenance. It shows source-backed primary kinds and classification-axis
topics, then their direct or inherited properties. Named instances—including
Relation Types—are shown only when the requested Projection scope includes
them. The view does not implement the Terms Graph, create targets, or alter
the selected source frontier.

## Semantics

Within the Object branch, Actor, Governing Objects, History, Package,
Structural Unit, Projection and Selection retain their reconciled
placements. Term and Property are direct Entity branches in the proposed root
Definition, not additions under Object. Actor/AI Agent and Actor/Operator are specializations. Package
contains Modules, and Modules contain Code Units; Project Implementation is
the root Package. Workflow contains Step, and Step contains Sub-step using the
qualified Operations paths and spaced containment tokens.

Source of truth flows through a Workflow to a Projection. The Projection is
rebuilt rather than directly edited. A defined Relation Type is a named
instance under `Entity/Graph Syntax <+ Relation//NAME`; a direct relation fact
is stored once and any inverse view is derived. IS_PROPERTY_OF is directed
from Property to its immediate bearer; HAS_PROPERTY is the derived inverse.

## Details

Use `/`, `//`, `.`, `:`, `+>`, `<+`, `>|`, `|<`, calls with `@` to already
declared Entities, logical grouping `()`, named Relations `((RELATION_TYPE))`,
direct-value Formats, and two-sided Relation cardinalities exactly as their
Definitions specify. Do
not add an organizational operator, functions, formula expressions, or
bracketed conditions. The Projection includes defining R IDs where available,
not copied Definition text.

Selection and Term placement remains provisional under C605. A missing direct
Definition stays visible rather than being hidden or supplied by the view.

### Current source pin and pending adoption

Proposed N+1 successor of `.caprmedio_caprmedio/101_LAYER_1_FRAMEWORK_METHODOLOGY/METHODOLOGY_SOURCES/001_CORE_META_MODEL/04_requirement/CA-R-2150-CORE_META_MODEL--define-subject-graph.md`, Version 14, SHA-256 `d423d501d2733a3f8412da9670b2b075d82f8d0d2a0d335a2a376d92ff97edf9`. Current bytes remain unchanged. The new Relation names depend on the pending IS_PROPERTY_OF / HAS_PROPERTY Relation Definition Drafts; this source does not admit them through a renamed token alone. This preparation performs no runtime change, generated-view refresh or promotion.
