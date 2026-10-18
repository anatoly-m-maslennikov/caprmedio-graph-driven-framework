---
subjects:
  governs: "Subject"
  depends_on:
    ["Entity/Continuant/Object/Atom", "Entity", "Entity/Continuant/Term", "Entity/Continuant/Object/Relation", "GOVERNS", "DEPENDS_ON", "Subject Path"]
version: 15
updated_at: "2026-10-15 18:41:32 +0000"
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
  source_atom_revision: 15
  source_sha256: af0d914d9eaa35592277726ce82427feb916b2e6e5b70a57c48615e74df8421c
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
