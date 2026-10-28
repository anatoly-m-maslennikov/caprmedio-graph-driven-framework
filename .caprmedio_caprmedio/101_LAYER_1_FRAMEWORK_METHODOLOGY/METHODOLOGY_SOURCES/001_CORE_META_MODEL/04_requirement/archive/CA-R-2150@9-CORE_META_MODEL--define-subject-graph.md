---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Subject Graph'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Subjects
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Domain
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering
  - Subject
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Runtime
  - Subject/CAPRMEDIO/Carrier
version: 9
updated_at: 2026-10-27 23:22:38 +0400
relations: {}
atom_id: CA-R-2150@9
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

Subject Graph means the non-authoritative Projection Type whose instances present a readable hierarchy of canonical Subject Targets from a selected Current RMEDO source frontier. The hierarchy is rooted at Subject and retains the full namespace of every selected target. Within CAPRMEDIO it preserves Graph with Node, Relation and Rule as siblings; Node's Project Model and Aspect branches; and Carrier outside Graph. Project-specific namespaces remain separate from shared framework vocabulary. The view retains the selected Project Model kinds, including existing Project and modeled Execution/Event meanings, and the selected Product, Project, Domain, Engineering, UX, Design and Documentation aspects. It is a target-hierarchy view, not an Atom-to-Subject link graph and not a native graph of another kind.

Source-backed classification-axis Subjects remain visible as topics. In the shared Atom branch, `Atom/Content Role` names such an axis; it is not a separate entity kind. Role-qualified descendants such as `Atom/Content Role: Plan` are narrower Atom kinds and inherit Atom properties. A namespace or classification-axis segment does not become an entity kind merely because it appears in the hierarchy.

## Details

The selected source frontier is the named Current RMEDO selection: current Requirement, Method, Evaluation, Delivery, and Operations Atoms after any approved missing-Status normalization. Concern, Analysis, Plan, Draft, Archived, and derived Projection material are outside this selection. Every represented Subject Target and property remains derived from those selected source Atoms and their canonical Subject paths; a filename, folder, or derived view does not create a target, property, relation, or authority. For a selected Graph Rule Atom, its YAML `claim.*` mapping is its source-backed fully formal Claim; absence of `atom.content.claim` does not mean Claim is absent.

The hierarchy is formed programmatically from canonical Subject paths using the approved /, ., :, and // operators as distinct hierarchy boundaries. The exact canonical path text, namespace and operator distinctions are preserved internally. Concise display labels do not replace full logical target identity. The result is not a term-oriented semantic graph or a construction tree.

A complete view has four sections in this order: primary Subject kinds and source-backed classification-axis topics, with namespace and branch context but without named instances or dependent properties; one detail section per displayed primary Subject with direct or inherited properties, in primary-tree first-appearance order; named instances, including Workflow instances, Relation Type declarations and concrete Graph Rule declarations; and dependency-only Subjects. A value-qualified narrower kind such as `Atom/Content Role: Plan` belongs with kinds, not with named Atom instances. Keep the bare `Atom/Content Role` axis visible as a topic; do not remove its Subject or collapse its identity into Atom. Show its source-backed axis detail without assigning it the bearer Atom's entity properties merely because it is an intermediate path segment.

The fourth section lists exact canonical Subject paths occurring in selected source Atoms' subjects.depends_on but never explicitly in their subjects.governs. Compare complete path strings, including their namespaces, without ancestor or descendant propagation. Show each path once with sorted, deduplicated referring Atom IDs, and sort paths alphabetically. This section reports existing targets without changing their placement in the first three sections; membership does not itself prove a missing definition or create another authority. The instance section is not a graph of actual Atom-to-Atom Relation tuples.

For this derived display, narrower Subject kinds inherit source-backed properties from their broader kinds. Mark each inherited property and allowed value as `[inherited]` in the Markdown display; retain the full originating canonical Subject in internal provenance. Keep role-qualified narrower Atom kinds as separate detail sections where properties are present. Keep direct additions and all source-backed origins; do not silently replace or discard inherited values. An equal-name collision does not authorize an override: retain its origins and report any conflict without choosing a winner. Derived inheritance does not create or rewrite source properties. It does not add per-Atom link lists, intermediate Subject objects, a separate Revision entity, or duplicate target identities. The source Atoms remain authoritative for every represented target and property, while the Projection preserves their Atom IDs and Versions in its source provenance.

The Subject Graph follows source of truth → Workflow → Projection. Changes are made in the selected authoritative sources and the view is rebuilt through its Workflow; the view is not edited directly. Directly edited Implementation that realizes RMED remains distinct from this derived view.

This Definition admits the requested Subject Graph Projection Type only. It does not define a new Domain entity, Tool, MCP route, runtime namespace, renderer, or implementation support gate.


Render the complete four-section Subject Graph by default. Only an explicitly requested bounded main-Subject view may render primary Subjects alone; label it `Bounded main-Subject view — not a complete Subject Graph`. It omits property inventories, instances and dependency-only reporting, retains the same Current RMEDO selection and complete provenance, and must not be presented as satisfying a request for the full Subject Graph.


Show defining Current Requirement Atoms by their bare CA-R IDs beside the Subjects they define. Do not copy definition or Claim text into the view, or add a Definitions table, file citation, hyperlink or inline Atom Version. The YAML sources list retains complete versioned provenance. A source is a defining reference only when it is a Current Requirement of Type Definition governing that Subject; do not label every governing Atom as its definition. A Subject without such a direct defining reference remains visible without an invented ID.
