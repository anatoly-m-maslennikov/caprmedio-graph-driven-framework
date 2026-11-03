---
subjects:
  active: Atom.Content
  passive:
  - Atom
  - Atom.Content
version: 31
updated_at: 2026-11-02 00:55:09 +0400
relations: {}
atom_id: CA-R-1417
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1417-CORE_META_MODEL-RULE--give-every-atom-revision-one-content.md
  source_atom_id: CA-R-1417
  source_atom_revision: 31
  source_sha256: e6e35d0653b097a70724dbc378f1a1b6358eef1da8e4c6373d8fabdad79a3dbf
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Give Every Atom Revision One Content

## Claim scope

The Content of each Atom version.

## Claim

Each Atom version **must** have exactly one Content portion.

## Semantics

Content is the Markdown portion whose natural-language meaning generally needs interpretation. Metadata properties use YAML. A complete RMED Content portion has its Claim as a direct Markdown value. A fenced CFEL expression may provide that value without prose. Do not create a separate Formal Claim child. Tools can extract sections or parse the supported formal syntax without proving all prose meaning.

One Content portion is a structured group with zero direct scalar values and independently counted child properties. This introduces no generic Substance field. The retained Summary's word Revision means an Atom version, not a separate Revision entity.
