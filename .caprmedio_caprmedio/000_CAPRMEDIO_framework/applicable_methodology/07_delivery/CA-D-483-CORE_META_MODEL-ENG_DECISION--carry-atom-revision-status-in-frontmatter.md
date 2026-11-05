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
status: Active
version: 24
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-D-483-CORE_META_MODEL-DECISION--carry-atom-revision-status-in-frontmatter.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-483-CORE_META_MODEL-ENG_DECISION--carry-atom-revision-status-in-frontmatter.md
  source_atom_id: CA-D-483
  source_atom_revision: 24
  source_sha256: c5ffef23a4af6401a1205cbb0a322627bf353f83a32c16a7cce5ce65c1161d54
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Carry Atom Revision Status in frontmatter

## Claim

### Prose Claim


the Status property carried by an Atom Revision.


**every** Atom Revision **must** carry **`=1`** explicit `status` value **in** its own Markdown frontmatter.

- the value **must** belong **to** the applicable Content Role **and** Type Status model.
- placement **must** agree under CA-D-466 **and** its specific Delivery rules; it is **not** a second Status source.
- another Revision **or** a containing Hub **must not** override this Revision's carried Status.

- encode `status` as **=1** nonempty YAML string using the exact value admitted by the selected Status model. do **not** accept a list, null, **or** another Revision's value as this Revision's Status.
