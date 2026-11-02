---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom
  depends_on:
  - Entity
version: 38
updated_at: 2026-10-29 09:34:45 +0400
relations: {}
atom_id: CA-R-655@38
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Entity Definition
---
## Summary
Define Atom Artifact Form

## Claim scope
Atoms.

## Claim

an Atom **means** the smallest independently governed Artifact.

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

Authored relation endpoint permissions are separate from reusable Relation Type meaning:

- rationale_for is owned by a Rationale Analysis Atom and targets one RMED Atom it explains.
- method_for is owned by a Method Atom and targets one Requirement it serves.
- delivery_for is owned by a Delivery Atom and targets one Requirement or Method it realizes.
- concern_about is owned by a Concern Atom and targets the directly affected governed entity.

Each entry represents one directed source-Type-target tuple, not a restriction that an owner can store only one entry of that Type. An Atom target must resolve to its canonical Current version; Draft and Archived targets are not admitted merely because an ID-like string is present.

## Details
