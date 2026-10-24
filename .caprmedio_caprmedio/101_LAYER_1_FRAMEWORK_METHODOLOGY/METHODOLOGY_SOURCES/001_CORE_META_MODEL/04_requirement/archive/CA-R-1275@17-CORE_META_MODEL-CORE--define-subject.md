---
subjects:
  governs: "Subject"
  depends_on:
    ["Entity/Node/Continuant/Atom", "Entity", "Subject Target", "Entity/Node/Continuant/Term", "Entity/Relation", "GOVERNS", "DEPENDS_ON", "Subject Path"]
version: 17
updated_at: "2026-10-21 01:47:52 +0400"
relations: {}
atom_id: CA-R-1275@17
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: Archived
author: "Anatoly Maslennikov"
global_tier: 9
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
