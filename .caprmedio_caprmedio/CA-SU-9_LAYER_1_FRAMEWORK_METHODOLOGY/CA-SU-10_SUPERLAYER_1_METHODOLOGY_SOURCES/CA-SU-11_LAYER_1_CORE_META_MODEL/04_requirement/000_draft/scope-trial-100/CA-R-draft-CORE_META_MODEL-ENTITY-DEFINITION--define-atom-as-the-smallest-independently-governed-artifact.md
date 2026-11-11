---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom
  depends_on:
  - Entity
version: 1
updated_at: 2026-10-29 20:32:25 +0400
relations: {}
atom_id: CA-R-draft
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
tier: 1
type: Entity Definition
---
## Summary

Define Atom as the smallest independently governed Artifact

## Claim scope

Atoms.

## Claim

an Atom **means** the smallest independently governed Artifact. Its independently governed contribution is coherent when its whole meaning can be faithfully covered by one concise Summary. One Claim may contain several related statements and conditions; smallest does not require one logical predicate per Atom.

### Formal claim

```text
Atom.Content Role[string]{1}
Atom.Type[string]{1}
Atom.ID[string]{1}
Atom.Status[string]{1}
Atom.Updated At[datetime]{1}
Atom.Version Number[int]{1}
Atom.Author[string]{1}
Atom.Tier[int]{1}
Atom.Label[string]{0..1}
Atom.Content.Summary[string]{1}
Atom.Local Scope Unit[string]{0..1}
Atom.Target Scope Unit[string]{0..1}
Atom.Subjects{0}
Atom.Subjects.Governs[string]{1}
Atom.Subjects.Depends On[string]{0+}
Atom.Relations{0}
Atom.Content{0}
```
