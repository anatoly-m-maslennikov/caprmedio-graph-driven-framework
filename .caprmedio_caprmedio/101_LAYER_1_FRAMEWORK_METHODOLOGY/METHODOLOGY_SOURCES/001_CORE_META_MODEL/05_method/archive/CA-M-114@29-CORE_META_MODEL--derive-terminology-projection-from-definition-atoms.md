---
subjects:
  governs: Subject/Domain/Node/Continuant/Projection
  depends_on:
  - 'Subject/Domain/Node/Continuant/Projection/Type: Catalog'
  - Generator
  - Definition Atom
  - Subject/Domain/Node/Continuant/Term
  - Subject/Domain/Node/Continuant/Project
  - Subject/Domain/Node/Continuant/Atom.Substance
  - Subject
  - Subject/Domain/Node
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
version: 29
updated_at: 2026-10-24 01:18:03 +0400
relations: {}
atom_id: CA-M-114@29
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
---
# Summary

Derive Terminology Projection from Definition Atoms

## Scope

derivation of a terminology Projection from active Definition Atoms.

## Claim

**to** build a terminology list using the Catalog Type, the Generator **must** derive **every** Governed Term's name **and** Project-specific meaning from its active Definition Atom. read the Term named by the defining Claim **and** verify that the Definition Atom's GOVERNS Subject Relation identifies its defined target under CA-R-1279-CORE_META_MODEL-CORE-REQUIREMENT--govern-every-defined-term. extract Term references from **every** named component of a Subject Path, **not** **only** its terminal component; obtain **every** referenced Term's meaning from that Term's own defining Claim, **not** by treating **all** path components as definitions supplied by the referencing Atom. include an entry **only** **when** the defining Claim establishes a Project-specific meaning; consistent use, capitalization, **or** occurrence **in** a Subject Path alone does **not** supply defining authority. an unresolved named component is a Term-reference gap **to** report, **not** permission **to** invent a definition **or** silently treat that component as ordinary vocabulary. exclude words **and** phrases used **only** with their ordinary English meanings. retain the source reference **without** classifying the direct Subject reference **or** a complete composite Subject Path as a Term **or** creating independent vocabulary authority.

## Details
