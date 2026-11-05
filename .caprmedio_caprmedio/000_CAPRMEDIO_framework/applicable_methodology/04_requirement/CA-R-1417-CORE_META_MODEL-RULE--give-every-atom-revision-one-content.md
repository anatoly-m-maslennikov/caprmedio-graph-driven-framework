---
atom_id: CA-R-1417
ref_id: CA-R-1417
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Content
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Content
tier: 1
status: Active
version: 33
updated_at: 2026-11-03 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-1417-CORE_META_MODEL-RULE--give-every-atom-revision-one-content.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1417-CORE_META_MODEL-RULE--give-every-atom-revision-one-content.md
  source_atom_id: CA-R-1417
  source_atom_revision: 33
  source_sha256: 6daea7dbd064d40ed028073d9f95bf22dd84d450f520bb6d4c0a399dd652be79
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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

