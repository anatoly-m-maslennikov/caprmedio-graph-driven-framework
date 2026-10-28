---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Atom Subjects Graph'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Subjects
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Atom Subjects Graph'
  - 'Subject/CAPRMEDIO/Graph/Relation/Type: GOVERNS'
  - 'Subject/CAPRMEDIO/Graph/Relation/Type: DEPENDS_ON'
  - Subject/CAPRMEDIO/Graph/Relation
  - Subject/CAPRMEDIO/Graph/Relation/Type
  - Subject
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term
version: 29
updated_at: 2026-10-27 19:59:52 +0400
relations: {}
atom_id: CA-R-1281
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Definition
---
# Summary

Define Atom Subjects Graph

## Scope

Atom Subjects Graph Type values under Projection.

## Claim

Atom Subjects Graph **means** the Type value under Projection whose instances are non-authoritative CAPRMEDIO Graphs derived from selected current Atom Subjects, with Atom nodes linked by direct GOVERNS **and** DEPENDS_ON Subject Relations **to** their canonical Subject Target nodes. A Subject names the thing or topic an Atom governs or depends on; GOVERNS and DEPENDS_ON are the links from the Atom to that Subject, not the Subject itself. The Subject target is not an intermediate Subject object or a duplicated target definition.

## Details

**every** represented link retains the source Atom identity, exact Subject Path, canonical target identity, Relation Kind, direction, **and** source Atom ID and Version. its Relation Types and endpoint constraints remain governed by applicable Graph Rules and other existing authority for their use; Relation Types use shared project-unique names and meanings, have no owning graph or Type Status, and this Projection Type does **not** create a mandatory per-Type admission record or default, nor an independently authored relation fact. represented targets retain their existing identities **without** an intermediate Subject object **or** duplicated target definitions.

an Atom Subjects Graph may represent canonical Subject Targets under one Subject-rooted hierarchy. this Projection Type remains the bipartite Atom-to-Subject link view; this specification does not claim that a particular renderer, tool, or existing Projection already supports that hierarchy.