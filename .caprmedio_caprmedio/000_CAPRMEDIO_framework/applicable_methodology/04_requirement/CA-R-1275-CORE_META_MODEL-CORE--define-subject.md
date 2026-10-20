---
subjects:
  governs: "Subject"
  depends_on:
    ["Entity/Node/Continuant/Atom", "Entity", "Entity/Node/Continuant/Term", "Entity/Relation", "GOVERNS", "DEPENDS_ON", "Subject Path"]
version: 16
updated_at: "2026-10-19 15:52:43 +0400"
relations: {}
atom_id: "CA-R-1275"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1275-CORE_META_MODEL-CORE--define-subject.md
  source_atom_id: CA-R-1275
  source_atom_revision: 16
  source_sha256: 0d91f79c84e07820c2e6fb20eda4aaf48131d914fe97c1d16cda1cf6a8f39a3a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Subject

## Scope

Subjects relating an Atom and an Entity.

## Claim

a Subject **means** a direct Relation between an Atom **and** an Entity, typed as GOVERNS **or** DEPENDS_ON.

## Details

- the Atom is the source; the Entity is the target identified by its full canonical Subject Path.
- the Subject is the Relation, **not** its target, its target's path, **or** a Term used **in** that path.
- the Relation creates no intermediate Subject object **and** no additional target identity; it does **not** make the target bearer-dependent on the source Atom.
