---
subjects:
  governs: Subject
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Entity
  - Subject Target
  - Entity/Node/Continuant/Term
  - Subject/Graph/Relation
  - 'Subject/Graph/Relation/Type: GOVERNS'
  - 'Subject/Graph/Relation/Type: DEPENDS_ON'
  - Subject Path
version: 19
updated_at: 2026-10-24 00:38:25 +0400
relations: {}
atom_id: CA-R-1275@19
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
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
