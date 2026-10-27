---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom.Content
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Atom.Content
version: 24
updated_at: 2026-10-26 05:29:36 +0400
relations: {}
atom_id: CA-R-1417
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Give Every Atom Revision One Content

## Scope

The Content of each Atom version.

## Claim

Each Atom version **must** have exactly one Content portion.

## Semantics

Content is the natural-language portion whose meaning generally requires
interpretation, represented by Markdown under the applicable D rules. Tools
can extract sections and check structure; that does not prove their meaning.
Structured YAML properties and operative formal rules are separate. A formal
Graph Rule can have only Summary in its Markdown Content, with optional
Semantics and Details; its fully formal Claim stays in its YAML `claim.*`
mapping. That does not require a duplicate `atom.content.claim`. Content does
not introduce another generic Substance field. The retained Summary's word
Revision refers to an Atom version, not a separate Revision entity.

## Details
