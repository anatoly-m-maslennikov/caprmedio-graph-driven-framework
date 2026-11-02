---
atom_id: CA-R-2150@13
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Entity/Object/Continuant/Projection/Type: Subject Graph'
  depends_on:
  - Entity/Object/Continuant/Projection
  - Entity/Object/Continuant/Projection/Type
  - Entity/Object/Continuant/Selection
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Object/Continuant/Governing Objects/Atom.Subjects
  - Entity/Aspect/Domain
  - Entity/Aspect/Engineering
  - Entity
  - Entity/Object/Continuant/Package/Project Implementation
  - Entity/Object/Occurrent/Runtime
  - Entity/Carrier
version: 13
relations: {}
tier: 1
updated_at: 2026-10-29 08:06:42 +0400
---
## Summary

Define Subject Graph

## Claim scope

the Entity Graph Projection Type under Projection.

## Claim

Entity Graph is a non-authoritative Projection Type that presents readable
canonical Entity Targets from a selected Current RMEDO frontier. Its root is
Entity, with Object, Aspect, Graph Syntax, and Carrier as sibling branches.
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
Structural Unit, Projection, Selection, and Term retain their reconciled
placements. Actor/AI Agent and Actor/Operator are specializations. Package
contains Modules, and Modules contain Code Units; Project Implementation is
the root Package. Workflow contains Step, and Step contains Sub-step using the
qualified Operations paths and spaced containment tokens.

Source of truth flows through a Workflow to a Projection. The Projection is
rebuilt rather than directly edited. A defined Relation Type is a named
instance under `Entity/Graph Syntax > Relation//NAME`; a direct relation fact
is stored once and any inverse view is derived.

## Details

Use `/`, `//`, `.`, `:`, `>`, `@(...)`, `((RELATION_TYPE))`, basic value
formats, and settled cardinalities exactly as their Definitions specify. Do
not add an organizational operator, functions, formula expressions, or
bracketed conditions. The Projection includes defining R IDs where available,
not copied Definition text.

Selection and Term placement remains provisional under C605. A missing direct
Definition stays visible rather than being hidden or supplied by the view.
