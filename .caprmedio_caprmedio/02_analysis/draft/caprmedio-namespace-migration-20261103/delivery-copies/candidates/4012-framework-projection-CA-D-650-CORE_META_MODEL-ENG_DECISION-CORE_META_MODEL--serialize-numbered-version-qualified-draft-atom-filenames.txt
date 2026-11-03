---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Carrier/File.Filename
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom.ID
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom.Version Number
version: 12
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-650
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-650-CORE_META_MODEL-ENG_DECISION-CORE_META_MODEL--serialize-numbered-version-qualified-draft-atom-filenames.md
  source_atom_id: CA-D-650
  source_atom_revision: 12
  source_sha256: b71f46f88ce4538b9a64aedef033d400c9557107e263c9966f03aa305a139d0a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize numbered version-qualified Draft Atom filenames

## Claim scope

Project-owned Draft Atom filename identity segments.

## Claim

A Draft Atom proposing a revision of an existing Atom **must** carry `atom_id: <canonical-ID>@<proposed-version>-draft`, where `<proposed-version>` is the proposed numeric Atom Version. Its filename **must** carry that exact marker once as the Atom-ID segment before the filename's mutable components under CA-D-283. Do **not** append another `@<version>` suffix to the basename. The Draft marker identifies the proposed revision; it does not replace or advance the Current Atom source before an admitted update.

New-Atom Draft markers continue to use the role-only form governed by CA-D-378; this rule does not add a version number to a new Atom's marker or change other filename components.

## Details

For an existing Atom, the proposed version follows the applicable revision rule, including the current-version-plus-one rule for an actual update. The owning role's `draft/` placement and remaining filename components continue to follow their applicable Delivery rules. Existing legacy Draft filenames are not normalized automatically.
