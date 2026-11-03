---
atom_id: CA-D-478
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom
  passive:
  - CAPRMEDIO <+ MODEL <+ Carrier/File
  - CAPRMEDIO <+ MODEL <+ Carrier/File.YAML Frontmatter
  - CAPRMEDIO <+ MODEL <+ Carrier/File.Main Content
version: 31
relations:
  delivery_for:
  - CA-R-1598
tier: 2
updated_at: 2026-11-02 00:55:09 +0400
role: Delivery
form: Policy
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-478-CORE_META_MODEL-ENG_DECISION--store-every-atom-property-in-one-internal-location.md
  source_atom_id: CA-D-478
  source_atom_revision: 31
  source_sha256: 181f993a26d7ab00bdcac7796da77bafc55f29d3748101e56eabe7d4553ee264
  original_relations_sha256: 843a624c507db49061abd0d25f3f76731df9f6dbfc291965068ed519395a75ca
---
## Summary

Store every Atom Property in one internal location

## Claim scope

Atom Property representation in an Atom Markdown File Carrier.

## Claim

Use YAML Frontmatter for an Atom's metadata properties. Use named Markdown
Main Content sections for `content.*` properties. Each applicable Atom Property
has one canonical internal location; its value is not duplicated between YAML
and Markdown.

This reusable Policy governs Atom representation. It does not create a Carrier
or a CARRIES fact for each property or section, and it does not change the
owning direction of an Atom-to-Atom Relation.

Qualified classifications are carried as ordinary metadata properties. For example, `Atom/(.Role := Concern)` selects the Atom's `role` value, and a qualified Form selects its `form` value; neither creates a nested Role object. Use the property names and canonical value encodings registered by the applicable D policy, including CA-D-657, rather than inventing a new field from the display path.

## Semantics

YAML and Markdown are carrier locations for different Atom properties, not
alternative authorities for the same value. A section's name identifies its
`content.*` property; a metadata property remains a YAML value.

## Details

This Policy incorporates
the reusable placement boundary supported by CA-D-357 without creating a
per-field representation entity.
