---
subjects:
  governs: "Entity/Node/Continuant/Atom.Governed Subject"
  depends_on:
    ["Entity/Node/Continuant/Atom.Subjects", "GOVERNS", "Subject", "Relation Kind", "Subject Target", "Entity/Node/Continuant/Atom.Substance"]
version: 16
updated_at: "2026-10-21 01:47:52 +0400"
relations:
  child_of:
    - CA-R-1269
    - CA-R-1199
    - CA-R-1201
    - CA-R-1202
atom_id: "CA-R-1363"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1363-CORE_META_MODEL-CORE--define-atom-governed-subject.md
  source_atom_id: CA-R-1363
  source_atom_revision: 16
  source_sha256: 5fdd655a483593f0347ddc8f325188877aaf2b97ebbdfde41d0f2d0ca5ed973a
  original_relations_sha256: cf083fc6909c16047a4a2a96c9a50e03f91fdb6be24a2277a01fa5beff61e7ca
---
# Summary

Define Atom Governed Subject

## Scope

an Atom's governed Subject relation.

## Claim

an Atom Governed Subject **means** the Atom's **`=1`** Subject Relation whose Relation Kind is GOVERNS. its target is the canonical Subject Target governed by the Atom's Claim; the Relation **and** its target are distinct.

## Details
