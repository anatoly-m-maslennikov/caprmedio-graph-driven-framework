---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Projection/Type: Subject Graph'
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Projection
  - Subject/Graph Node/Domain/Continuant/Projection/Type
  - Subject/Graph Node/Domain/Continuant/Projection/Selection
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Atom.Subjects
  - Subject/Graph Node/Domain
  - Subject/Graph Node/Engineering
  - Subject
  - Subject/Graph Node/Implementation
  - Subject/Graph Node/Runtime
  - Subject/Graph Node/Carrier
version: 7
updated_at: 2026-10-27 06:29:27 +0400
relations: {}
atom_id: CA-R-2150@7
content_role: Requirement
type: Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 1
status: Archived
author: Anatoly Maslennikov
---
# Summary

Define Subject Graph

## Scope

the Subject Graph Projection Type under Projection.

## Claim

Subject Graph means the non-authoritative Projection Type whose instances present a readable hierarchy of canonical Subject Targets from a selected Current RMEDO source frontier. The hierarchy is rooted at Subject and preserves the selected Graph Node, Graph Relation, and Graph Rule branches. Under Graph Node it preserves the selected Domain Continuant/Occurrent descendants, Engineering aspects, logical Implementation, technical Runtime, Carrier representations, and Documentation, Product, and UX branches. It is a target-hierarchy view, not an Atom-to-Subject link graph and not a native graph of another kind.

## Details

The selected source frontier is the named Current RMEDO selection: current Requirement, Method, Evaluation, Delivery, and Operations Atoms after any approved missing-Status normalization. Concern, Analysis, Plan, Draft, Archived, and derived Projection material are outside this selection. Every represented Subject Target and property remains derived from those selected source Atoms and their canonical Subject paths; a filename, folder, or derived view does not create a target, property, relation, or authority. For a selected Graph Rule Atom, its YAML `claim.*` mapping is its source-backed fully formal Claim; absence of `atom.content.claim` does not mean Claim is absent.

The hierarchy is formed programmatically from canonical Subject paths using the approved /, ., :, and // operators as distinct hierarchy boundaries. The exact canonical path text and operator distinctions are preserved. The result is not a term-oriented semantic graph or a construction tree.

The view has four sections in this order: primary Subject kinds without instances or dependent properties; one detail section per primary Subject with direct or inherited properties, in primary-tree first-appearance order; named instances, including Workflow instances, Relation Type declarations and concrete Graph Rule declarations; and dependency-only Subjects. The fourth section lists exact canonical Subject paths occurring in selected source Atoms' subjects.depends_on but never explicitly in their subjects.governs. Compare complete path strings without ancestor or descendant propagation. Show each path once with sorted, deduplicated referring Atom IDs, and sort paths alphabetically. This section reports existing targets without changing their placement in the first three sections; membership does not itself prove a missing definition or create another authority. The instance section is not a graph of actual Atom-to-Atom Relation tuples. For this derived display, narrower Subject kinds inherit source-backed properties from their broader kinds. Mark each inherited property and allowed value with its originating canonical Subject. Keep direct additions and all source-backed origins; do not silently replace or discard inherited values. An equal-name collision does not authorize an override: retain its origins and report any conflict without choosing a winner. Derived inheritance does not create or rewrite source properties. It does not add per-Atom link lists, intermediate Subject objects, a separate Revision entity, or duplicate target identities. The source Atoms remain authoritative for every represented target and property, while the Projection preserves their Atom IDs and Versions in its source provenance.

This Definition admits the requested Subject Graph Projection Type only. It does not define a new Domain entity, Tool, MCP route, runtime namespace, renderer, or implementation support gate.
