---
subjects:
  active: Atom
  passive:
  - Atom.Content.Summary
  - Atom.ID
  - Atom.Status
  - Carrier/File
version: 23
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-480
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-480-CORE_META_MODEL-ENG_DECISION--keep-atom-addresses-consistent-with-carried-properties.md
  source_atom_id: CA-D-480
  source_atom_revision: 23
  source_sha256: bf0c3883b1c061c81a7c64322c874869bf592ce5a68684e04a7bff684edba270
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Keep Atom addresses consistent with carried Properties

## Claim scope

Atom Properties represented by a filename, matching directory name, or placement.

## Claim

**every** Atom Property represented by a filename, matching directory name, **or** placement **must** agree with its canonical internal value under the applicable Delivery encoding.

- compare resolved values using the registered encoding; a Summary Slug is checked against its Summary serialization, **not** against identical raw text.
- a mismatch is invalid **and** **must** be reported; the address **must not** silently override the value carried inside the Atom.
- agreement checking does **not** authorize rewriting the Atom **or** address. corrections require the applicable authorized change.
