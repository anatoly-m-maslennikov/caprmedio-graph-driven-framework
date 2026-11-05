---
atom_id: CA-D-652
ref_id: CA-D-652
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Tier
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Header.Tier
  - CAPRMEDIO_MODEL <+ Projection
tier: 4
relations:
  delivery_for:
  - CA-R-2706
  depends_on:
  - CA-D-651
  - CA-D-478
status: Active
version: 13
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-D-652-CORE_META_MODEL-DECISION--omit-default-numeric-tier-tokens-from-filenames.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-652-CORE_META_MODEL-ENG_DECISION--omit-default-numeric-tier-tokens-from-filenames.md
  source_atom_id: CA-D-652
  source_atom_revision: 13
  source_sha256: 2ce722e330f85fbaa79c4d1a3df64fd6590b5b606b48c7f56fe472b9532011f9
  original_relations_sha256: 349725a2fbf93b6eaa9d1fe14df2742e7ef0bb18d523c105b8ed7cb76d2f7f23
---
## Summary

Omit Default Numeric Tier Tokens from Filenames

## Claim

### Prose Claim


Atom filenames whose registered grammar omits the default numeric Tier token.


an Atom filename **may** omit the default Tier `3` token only where the registered filename grammar explicitly defines that omission. The Atom **must** still carry its numeric Tier internally under CA-R-2706; omission **must not** add, remove, or alter an Atom Property, infer a Content Role or Type restriction, or change the represented source Properties in a Projection or other non-Atom Artifact. A Project Goal's explicit Tier `-1` grammar is evaluated before any ordinary default omission.
