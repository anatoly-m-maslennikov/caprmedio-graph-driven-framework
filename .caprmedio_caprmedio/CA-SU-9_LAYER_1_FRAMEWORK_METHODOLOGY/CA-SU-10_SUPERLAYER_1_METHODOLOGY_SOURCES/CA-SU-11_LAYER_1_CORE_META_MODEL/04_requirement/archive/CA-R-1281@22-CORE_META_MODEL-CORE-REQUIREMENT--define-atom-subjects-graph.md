---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Projection/Type: Atom Subjects Graph'
  depends_on:
  - Subject/Domain/Node/Continuant/Projection
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Atom.Subjects
  - 'Subject/Domain/Node/Continuant/Projection/Type: Atom Subjects Graph'
  - 'Subject/Graph/Relation/Type: GOVERNS'
  - 'Subject/Graph/Relation/Type: DEPENDS_ON'
  - Subject/Graph/Relation
  - Subject/Graph/Relation/Type
  - CAPRMEDIO Graph
  - Subject
  - Subject/Domain/Node/Continuant/Term
version: 22
updated_at: 2026-10-24 01:18:03 +0400
relations: {}
atom_id: CA-R-1281@22
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
---
# Summary

Define Atom Subjects Graph

## Scope

Atom Subjects Graph Type values under Projection.

## Claim

Atom Subjects Graph **means** the Type value under Projection whose instances are non-authoritative CAPRMEDIO Graphs derived from selected current Atom Subjects, with Atom nodes linked by direct GOVERNS **and** DEPENDS_ON Subject Relations **to** their canonical Subject Target nodes. the Subjects are the links, **not** the target nodes **or** intermediate Subject nodes.

## Details

**every** represented link retains the source Atom identity, exact Subject Path, canonical target identity, Relation Kind, direction, **and** source Atom ID and Version. its Relation Kinds **and** endpoint constraints remain governed by their existing graph-qualified authority; naming this Projection Type does **not** admit another Relation Kind owner **or** an independently authored relation fact. represented targets retain their existing identities **without** an intermediate Subject object **or** duplicated target definitions.

an Atom Subjects Graph may represent canonical Subject Targets under one Subject-rooted hierarchy. this Projection Type remains the bipartite Atom-to-Subject link view; this specification does not claim that a particular renderer, tool, or existing Projection already supports that hierarchy.
