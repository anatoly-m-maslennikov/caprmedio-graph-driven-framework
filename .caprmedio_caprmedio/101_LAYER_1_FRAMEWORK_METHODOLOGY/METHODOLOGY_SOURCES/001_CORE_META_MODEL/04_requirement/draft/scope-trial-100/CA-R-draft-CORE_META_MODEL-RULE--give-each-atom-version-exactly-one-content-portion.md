---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Content
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Object/Continuant/Governing Objects/Atom.Content
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
type: Rule
---
## Summary

Give each Atom version exactly one Content portion

## Claim scope

The Content of each Atom version.

## Claim

Each Atom version **must** have exactly one Content portion.

## Semantics

Content is the Markdown portion whose natural-language meaning generally needs interpretation. Metadata properties use YAML. A complete RMED Content portion has its direct prose Claim; R may add the nested Formal claim defined by CA-R-1269. That formal child remains within the same Markdown Claim rather than in a separate YAML claim. Tools can extract sections or parse the supported formal syntax without proving all prose meaning.

One Content portion is a structured group with zero direct scalar values and independently counted child properties. This introduces no generic Substance field. The retained Summary's word Revision means an Atom version, not a separate Revision entity.
