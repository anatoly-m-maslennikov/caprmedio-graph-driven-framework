---
subjects:
  active: Atom.Content
  passive:
  - Atom
  - Atom.Content
version: 30
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1417@30
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
tier: 1
role: Requirement
form: Rule
---
## Summary

Give Every Atom Revision One Content

## Claim scope

The Content of each Atom version.

## Claim

Each Atom version **must** have exactly one Content portion.

## Semantics

Content is the Markdown portion whose natural-language meaning generally needs interpretation. Metadata properties use YAML. A complete RMED Content portion has its direct prose Claim; R may add the nested Formal claim defined by CA-R-2500. That formal child remains within the same Markdown Claim rather than in a separate YAML claim. Tools can extract sections or parse the supported formal syntax without proving all prose meaning.

One Content portion is a structured group with zero direct scalar values and independently counted child properties. This introduces no generic Substance field. The retained Summary's word Revision means an Atom version, not a separate Revision entity.
