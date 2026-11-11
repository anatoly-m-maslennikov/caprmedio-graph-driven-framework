---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Subjects
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity
  - Entity/Graph Syntax > Relation//GOVERNS
  - Entity/Graph Syntax > Relation//DEPENDS_ON
  - Entity/Object/Continuant/Term//Property
  - Entity/Object/Continuant/Governing Objects/Atom.Subjects
version: 28
updated_at: 2026-10-29 09:46:50 +0400
relations: {}
atom_id: CA-R-1198
content_role: Requirement
type: Entity Definition
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
---
## Summary

Define Atom Subjects

## Claim scope

the Atom Subjects Property.

## Claim

Subjects is the structured Atom property that links the Atom to its governed Subject and contextual dependencies. A complete Current Atom has exactly one direct GOVERNS target and zero or more direct DEPENDS_ON targets. The grouping has no direct scalar value; each child is counted independently. Drafts can remain incomplete until promotion.

The links preserve their target identities without copying the target or creating a separate Subject object for each link. A governing Atom may introduce its governed target; that target need not pre-exist as a separate artifact.

### Formal claim

```text
Atom.Subjects{0}
Atom.Subjects.Governs[string]{1}
Atom.Subjects.Depends On[string]{0+}
```
