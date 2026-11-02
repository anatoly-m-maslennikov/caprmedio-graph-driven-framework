---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Content
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Evaluation'
  - Entity/Object/Continuant/Structural Unit/Scope Unit
  - Entity/Object/Continuant/Governing Objects/Atom.Target Scope Unit
version: 27
updated_at: 2026-10-29 10:13:50 +0400
relations: {}
atom_id: CA-E-461@27
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Eval Policy
tier: 2
---
## Summary

Warn About Selected-sibling Claim Boundaries

## Claim scope

an Atom Claim concerning **only** selected sibling Scope Units.

## Claim

**when** **`=1`** Atom Claim concerns **only** **`>=2`** selected sibling Scope Units **and** does **not** apply **to** their containing Scope Unit as a whole, the Evaluation **must** report a non-blocking boundary warning for review; that restriction alone **must not** make the Atom invalid **or** trigger automatic rejection, splitting, **or** retargeting **to** their parent.
