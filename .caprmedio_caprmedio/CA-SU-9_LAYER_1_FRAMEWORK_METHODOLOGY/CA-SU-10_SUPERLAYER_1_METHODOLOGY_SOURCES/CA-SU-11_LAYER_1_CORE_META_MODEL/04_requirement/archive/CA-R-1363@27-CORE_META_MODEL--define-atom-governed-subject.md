---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Subjects.Governs
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom.Subjects
  - Entity/Graph Syntax > Relation//GOVERNS
  - Entity
  - Entity/Graph Syntax > Relation
  - Entity/Object/Continuant/Governing Objects/Atom.Content
version: 27
updated_at: 2026-10-29 09:46:50 +0400
relations:
  child_of:
  - CA-R-1269
  - CA-R-1199
  - CA-R-2100
  - CA-R-1202
atom_id: CA-R-1363@27
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
---
## Summary

Define Atom Governed Subject

## Claim scope

an Atom's governed Subject relation.

## Claim

an Atom Governed Subject **means** the Atom's exactly one GOVERNS Subject Relation for a complete Current Atom; its Relation Kind is GOVERNS. A Draft may omit it while incomplete. This is the link whose target is the canonical Subject Target governed by the Atom's role/Type-specific Content; the Relation **and** its target are distinct.

## Details

### Formal claim

```text
Atom.Subjects.Governs[string]{1}
```
