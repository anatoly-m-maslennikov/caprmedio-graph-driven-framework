---
subjects:
  governs: 'Subject/Graph/Relation/Type: GOVERNS'
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Semantics
  - Subject
  - Subject/Domain/Node/Continuant/Term
  - Subject/Domain/Node/Continuant/Atom.Content
version: 25
updated_at: 2026-10-25 03:12:46 +0400
relations: {}
atom_id: CA-R-1279@25
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Govern Every Defined Term

## Scope

defined Terms and their canonical direct GOVERNS Subject Relation.

## Claim

when an Atom's Claim explicitly defines a Term, it **must** use its **`=1`** direct GOVERNS Subject Relation **to** identify the canonical target defined by that Claim, with the defined Term as the terminal name **in** that target's Subject Path. the defining Claim, source use, **and** applicable Atom.Semantics establish that Term's meaning; the other Term components **in** the path are references **to** their own meanings, **not** additional meanings supplied by this Atom.

## Details
