---
atom_id: CA-D-483
ref_id: CA-D-483
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Status
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Header.Role
  - CAPRMEDIO_MODEL <+ Atom.Header.Form
  - CAPRMEDIO_MODEL <+ Carrier
tier: 3
status: active
version: 26
updated_at: 2026-11-09 00:51:00 +0400
carrier_destination:
  file:
    name: CA-D-483-CORE_META_MODEL-ENG_DECISION--carry-atom-revision-status-in-frontmatter.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-483-CORE_META_MODEL-ENG_DECISION--carry-atom-revision-status-in-frontmatter.md
  source_atom_id: CA-D-483
  source_atom_revision: 26
  source_sha256: fc23b9cb2d6a55f265672f9cdb46a182263cf9254bdf846f6786fea36d0971c4
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Carry Atom Revision Status in frontmatter

## Claim

### Prose Claim


the Status property carried by an Atom Revision.


Every Atom Revision carries exactly one explicit Status value at its declared Header path in its own Markdown frontmatter.

- the value **must** belong **to** the applicable Content Role **and** Type Status model.
- placement **must** agree under CA-D-466 **and** its specific Delivery rules; it is **not** a second Status source.
- another Revision **or** a containing Hub **must not** override this Revision's carried Status.

- Encode Status as one nonempty YAML string using the common named-value encoding. Its decoded value resolves to exactly one Status admitted by the applicable model. A list, null or another Revision’s value is invalid.
