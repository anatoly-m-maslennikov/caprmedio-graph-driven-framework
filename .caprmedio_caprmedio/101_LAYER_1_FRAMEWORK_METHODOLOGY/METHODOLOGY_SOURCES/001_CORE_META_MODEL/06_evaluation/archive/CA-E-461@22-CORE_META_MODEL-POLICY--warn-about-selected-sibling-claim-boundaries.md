---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom.Content
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Evaluation'
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Domain/Continuant/Atom.Target Scope Unit
version: 22
updated_at: 2026-10-25 17:32:27 +0400
relations: {}
atom_id: CA-E-461@22
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Policy
tier: 2
---
# Summary

Warn About Selected-sibling Claim Boundaries

## Scope

an Atom Claim concerning **only** selected sibling Scope Units.

## Claim

**when** **`=1`** Atom Claim concerns **only** **`>=2`** selected sibling Scope Units **and** does **not** apply **to** their containing Scope Unit as a whole, the Evaluation **must** report a non-blocking boundary warning for review; that restriction alone **must not** make the Atom invalid **or** trigger automatic rejection, splitting, **or** retargeting **to** their parent.

## Details
