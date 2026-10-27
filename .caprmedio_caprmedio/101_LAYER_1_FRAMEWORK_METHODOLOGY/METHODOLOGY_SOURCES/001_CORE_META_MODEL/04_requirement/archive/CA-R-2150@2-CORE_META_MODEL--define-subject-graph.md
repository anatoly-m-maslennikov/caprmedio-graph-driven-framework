---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Projection/Type: Subject Graph'
  depends_on:
  - Subject/Domain/Node/Continuant/Projection
  - Subject/Domain/Node/Continuant/Projection/Type
  - Subject/Domain/Node/Continuant/Projection/Selection
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Atom.Subjects
  - Subject/Domain
  - Subject/Engineering
  - Subject/Graph
version: 2
updated_at: 2026-10-24 10:48:25 +0400
relations: {}
atom_id: CA-R-2150@2
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

Subject Graph means the non-authoritative Projection Type whose instances present a readable hierarchy of canonical Subject Targets from a selected Current RMEDO source frontier. the hierarchy is rooted at Subject and preserves the selected Domain, Engineering, and global Graph branches. it is a target hierarchy view, not an Atom-to-Subject link graph and not a native graph of another kind.

## Details

The selected source frontier is the named Current RMEDO selection: current Requirement, Method, Evaluation, Delivery, and Operations Atoms after any approved missing-Status normalization. Concern, Analysis, Plan, Draft, Archived, and derived Projection material are outside this selection. Every represented Subject Target and property remains derived from those selected source Atoms and their canonical Subject paths; a filename, folder, or derived view does not create a target, property, relation, or authority.

The hierarchy is formed programmatically from canonical Subject paths using the approved /, ., :, and // operators as distinct hierarchy boundaries. The exact canonical path text and operator distinctions are preserved. The result is not a term-oriented semantic graph or a construction tree.

The view contains primary Subject Targets and per-primary property sections. It does not add per-Atom link lists, intermediate Subject objects, a separate Revision entity, or duplicate target identities. The source Atoms remain authoritative for every represented target and property, while the Projection preserves their Atom IDs and Versions in its source provenance.

This Definition admits the requested Subject Graph Projection Type only. It does not define a new Domain entity, Tool, MCP route, runtime namespace, renderer, or implementation support gate.
