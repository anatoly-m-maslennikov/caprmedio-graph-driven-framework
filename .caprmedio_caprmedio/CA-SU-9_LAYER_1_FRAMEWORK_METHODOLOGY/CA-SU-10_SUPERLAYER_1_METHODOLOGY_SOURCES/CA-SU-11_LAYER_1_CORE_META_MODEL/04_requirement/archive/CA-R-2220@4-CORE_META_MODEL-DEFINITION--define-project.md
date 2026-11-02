---
atom_id: CA-R-2220@4
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit/Project
version: 4
updated_at: 2026-10-29 09:06:21 +0400
relations: {}
tier: 1
---
## Summary

Define Project

## Claim scope

The Project as a whole in the primary Subject structure.

## Claim

Project means the whole project as one entity, distinct from any particular part such as an Atom or Implementation.

### Formal claim

```text
Scope Unit/Project.Parent{0}
```

## Semantics

This Subject addresses claims about the project as a whole. Atoms, Implementation, governing configurations and other project parts retain their own Subjects.

Project Model groups the vocabulary for Project and its parts. Project is the whole entity addressed by a Subject; Project Model is the vocabulary grouping.

The root Scope Unit organizes the project's Atoms and child Scope Units. Implementation and the repository Carrier are distinct project parts or representations; none replaces the whole-project Subject.
