---
subjects:
  governs: "Entity/Continuant/Projection/Type: Atom Subjects Graph"
  depends_on:
    ["Entity/Continuant/Projection", "Entity/Continuant/Object/Atom", "Entity/Continuant/Object/Atom.Subjects", "Subject Path", "Entity", "GOVERNS", "DEPENDS_ON", "Entity/Continuant/Object/Relation", "Relation Kind", "CAPRMEDIO Graph", "Subject", "Entity/Continuant/Term"]
version: 14
updated_at: "2026-10-15 18:13:35 +0000"
relations: {}
atom_id: "CA-R-1281@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Define Atom Subjects Graph

## Scope

Atom Subjects Graph Type values under Projection.

## Claim

Atom Subjects Graph **means** the Type value under Projection whose instances are non-authoritative CAPRMEDIO Graphs derived from selected current Atom Subjects, with Atom nodes linked by direct GOVERNS **and** DEPENDS_ON Subject Relations **to** their canonical Entity target nodes. the Subjects are the links, **not** the target nodes **or** intermediate Subject nodes.

## Details

**every** represented link retains the source Atom identity, exact Subject Path, canonical target identity, Relation Kind, direction, **and** source Artifact Revision. its Relation Kinds **and** endpoint constraints remain governed by their existing graph-qualified authority; naming this Projection Type does **not** admit another Relation Kind owner **or** an independently authored relation fact. represented targets retain their Entity identities **without** an intermediate Subject object **or** duplicated target definitions.
