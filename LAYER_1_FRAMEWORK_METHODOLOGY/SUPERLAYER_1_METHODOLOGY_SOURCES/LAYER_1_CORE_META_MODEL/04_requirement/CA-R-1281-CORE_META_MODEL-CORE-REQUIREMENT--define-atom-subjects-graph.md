---
subjects:
  governs: "Entity/Node/Continuant/Projection/Type: Atom Subjects Graph"
  depends_on:
    ["Entity/Node/Continuant/Projection", "Entity/Node/Continuant/Atom", "Entity/Node/Continuant/Atom.Subjects", "Subject Path", "Subject Target", "GOVERNS", "DEPENDS_ON", "Entity/Relation", "Relation Kind", "CAPRMEDIO Graph", "Subject", "Entity/Node/Continuant/Term"]
version: 16
updated_at: "2026-10-21 01:47:52 +0400"
relations: {}
atom_id: "CA-R-1281"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Define Atom Subjects Graph

## Scope

Atom Subjects Graph Type values under Projection.

## Claim

Atom Subjects Graph **means** the Type value under Projection whose instances are non-authoritative CAPRMEDIO Graphs derived from selected current Atom Subjects, with Atom nodes linked by direct GOVERNS **and** DEPENDS_ON Subject Relations **to** their canonical Subject Target nodes. the Subjects are the links, **not** the target nodes **or** intermediate Subject nodes.

## Details

**every** represented link retains the source Atom identity, exact Subject Path, canonical target identity, Relation Kind, direction, **and** source Artifact Revision. its Relation Kinds **and** endpoint constraints remain governed by their existing graph-qualified authority; naming this Projection Type does **not** admit another Relation Kind owner **or** an independently authored relation fact. represented targets retain their existing identities **without** an intermediate Subject object **or** duplicated target definitions.

an Atom Subjects Graph may represent both Entity-root and Method-root Subject Targets. this specification does not claim that a particular renderer, tool, or existing Projection already supports either root.
