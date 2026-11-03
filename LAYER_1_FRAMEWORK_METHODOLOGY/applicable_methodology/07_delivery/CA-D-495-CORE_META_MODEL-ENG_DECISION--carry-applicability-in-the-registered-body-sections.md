---
subjects:
  active: Atom.Content
  passive:
  - Atom.Content
  - Entity/Object/Continuant/Governing Objects/Atom.Target Scope Unit
  - Carrier/File
  - Entity/Object/Continuant/Governing Objects/Atom/Content Role
version: 25
updated_at: 2026-11-02 00:55:09 +0400
relations: {}
atom_id: CA-D-495
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-495-CORE_META_MODEL-ENG_DECISION--carry-applicability-in-the-registered-body-sections.md
  source_atom_id: CA-D-495
  source_atom_revision: 25
  source_sha256: 96fd508962c9ee5e8788a6096cf212ad534ab674b15fbcff3f3acde643a3df73
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Carry applicability in the registered body sections

## Claim scope

applicability restrictions of Claims carried by Markdown Atom Carriers.

## Claim

a Markdown Atom Carrier **must** carry the Claim's applicability **in** the registered body sections, **not** as a duplicate frontmatter value:

- for ordinary RMED layouts, carry applicability **in** Scope, followed by the qualified contribution **in** Claim **and** supporting information **in** Details, using the exact headings registered by CA-D-479.
- carry formal content in a CFEL fence within the Claim under CA-D-479. The Claim may contain CFEL without prose. Do not create a Formal Claim child or an operative frontmatter Claim.
- for other Content Roles, retain applicability **in** their registered primary content. this rule does **not** change their body-section layouts.
- an ordinary RMED Claim scope section **must** contain an applicability description, **not** just a copy of `current_scope_unit` **or** `claim_target_scope_unit`. those fields remain the carried structural references under CA-D-482.
- carry the applicability restrictions **=1** time. in the ordinary RMED layout, Claim **and** Details are read within Claim scope; do **not** maintain a second scope declaration **in** either section **or** frontmatter.

## Details

Scope identifies what the Claim applies **to**, including relevant conditions **and** exclusions. it does **not** select another structural target, change ownership, **or** introduce a separate Claim. a reference **to** the carried target is **not** a second authoritative copy of that target.
