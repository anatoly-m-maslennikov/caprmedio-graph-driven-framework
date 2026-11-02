---
subjects:
  governs: Entity/Aspect/Engineering/Authoring/Controlled English
  depends_on:
  - Entity/Aspect/Engineering/Authoring/Controlled English
  - Entity/Object/Continuant/Governing Objects/Atom
version: 1
updated_at: 2026-10-29 20:32:25 +0400
relations:
  child_of:
  - CA-M-122
atom_id: CA-M-draft
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
author: Anatoly Maslennikov
tier: 6
type: Implementation Method
---
## Summary

Evaluate membership and nonmembership in a set-valued property

## Claim scope

evaluation of **in** **or** **not in** for one set-valued governed property.

## Claim

**to** evaluate **in** **or** **not in** for one set-valued governed property, the Resolver **must** evaluate **in** as true exactly **when** **`>=1`** property member **`=`** one listed value **and** **must** evaluate **not in** as true exactly **when** no property member **`=`** **any** listed value.
