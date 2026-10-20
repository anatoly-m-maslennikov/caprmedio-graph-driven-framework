---
subjects:
  governs: "Entity/Node/Continuant/Projection/Type: Atom Subjects Graph"
  depends_on:
    ["Entity/Node/Continuant/Projection", "Entity/Node/Continuant/Atom", "Entity/Node/Continuant/Atom.Subjects", "Subject Path", "Entity", "GOVERNS", "DEPENDS_ON", "Entity/Relation", "Relation Kind", "CAPRMEDIO Graph", "Subject", "Entity/Node/Continuant/Term"]
version: 15
updated_at: "2026-10-19 15:52:44 +0400"
relations: {}
atom_id: "CA-R-1281"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1281-CORE_META_MODEL-CORE-REQUIREMENT--define-atom-subjects-graph.md
  source_atom_id: CA-R-1281
  source_atom_revision: 15
  source_sha256: b0e06a0b79ecc512cdf3a0378233b58872c70d7515470e1c272c9cfb017c6e11
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Atom Subjects Graph

## Scope

Atom Subjects Graph Type values under Projection.

## Claim

Atom Subjects Graph **means** the Type value under Projection whose instances are non-authoritative CAPRMEDIO Graphs derived from selected current Atom Subjects, with Atom nodes linked by direct GOVERNS **and** DEPENDS_ON Subject Relations **to** their canonical Entity target nodes. the Subjects are the links, **not** the target nodes **or** intermediate Subject nodes.

## Details

**every** represented link retains the source Atom identity, exact Subject Path, canonical target identity, Relation Kind, direction, **and** source Artifact Revision. its Relation Kinds **and** endpoint constraints remain governed by their existing graph-qualified authority; naming this Projection Type does **not** admit another Relation Kind owner **or** an independently authored relation fact. represented targets retain their Entity identities **without** an intermediate Subject object **or** duplicated target definitions.
