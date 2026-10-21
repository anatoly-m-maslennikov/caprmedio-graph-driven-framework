---
subjects:
  governs: "Subject"
  depends_on:
    ["Entity/Node/Continuant/Atom", "Entity", "Subject Target", "Entity/Node/Continuant/Term", "Entity/Relation", "GOVERNS", "DEPENDS_ON", "Subject Path"]
version: 17
updated_at: "2026-10-21 01:47:52 +0400"
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
  source_atom_revision: 17
  source_sha256: c36446b966447d9fbe61127e89eb3b35bfc9be508c1b8a93aef83973077b2e40
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Define Subject

## Scope

Subjects relating an Atom and a canonical Subject Target.

## Claim

a Subject **means** a direct Relation between an Atom **and** a canonical Subject Target, typed as GOVERNS **or** DEPENDS_ON.

## Details

- the Atom is the source; the Subject Target is the target identified by its full canonical Subject Path.
- the Subject is the Relation, **not** its target, its target's path, **or** a Term used **in** that path.
- the Relation creates no intermediate Subject object **and** no additional target identity; it does **not** make the target bearer-dependent on the source Atom.
