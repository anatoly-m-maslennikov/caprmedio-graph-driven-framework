---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Content
  passive:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Content
version: 32
updated_at: 2026-11-02 00:55:09 +0400
relations: {}
atom_id: CA-R-1417
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
tier: 1
role: Requirement
form: Rule
---
## Summary

Give Every Atom Revision One Content

## Claim

### Prose Claim

Applicability: The Content of each Atom version.

Each Atom version **must** have exactly one Content portion.

## Semantics

Content is the Markdown portion whose natural-language meaning generally needs interpretation. Header properties use YAML. A complete ordinary RMED Content portion has a Claim grouping with no direct value and one or both declared Formal Claim and Prose Claim children. Formal Claim contains a CFEL-labelled code fence; Prose Claim contains ordinary Markdown. Tools can extract declared Properties or parse supported formal syntax without proving all prose meaning.

One Content portion is a structured group with zero direct scalar values and independently counted child Properties. This introduces no generic Substance field. The retained Summary's word Revision means an Atom version, not a separate Revision entity.

