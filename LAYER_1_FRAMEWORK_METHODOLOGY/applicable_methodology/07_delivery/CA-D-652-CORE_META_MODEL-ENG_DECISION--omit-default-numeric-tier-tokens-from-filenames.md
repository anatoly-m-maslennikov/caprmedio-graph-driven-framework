---
subjects:
  active: Atom.Tier
  passive:
  - Atom
  - Atom.Tier
  - Projection
version: 13
updated_at: 2026-11-02 00:18:22 +0400
relations:
  delivery_for:
  - CA-R-2504
  depends_on:
  - CA-D-651
  - CA-D-478
atom_id: CA-D-652
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 4
status: Active
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-652-CORE_META_MODEL-ENG_DECISION--omit-default-numeric-tier-tokens-from-filenames.md
  source_atom_id: CA-D-652
  source_atom_revision: 13
  source_sha256: 7d490bc3586d09c331b3943545b64a2541804bf55347127abd1d3d600649fc8a
  original_relations_sha256: 61d5d9b3b6559fc0663226667f6ffe52e28f3fc7ab432e1a8dbd1b1c3bdf782d
---
## Summary

Omit Default Numeric Tier Tokens from Filenames

## Claim scope

Atom filenames whose registered grammar omits the default numeric Tier token.

## Claim

an Atom filename **may** omit the default Tier `3` token only where the registered filename grammar explicitly defines that omission. The Atom **must** still carry its numeric Tier internally under CA-R-2504; omission **must not** add, remove, or alter an Atom Property, infer a Content Role or Type restriction, or change the represented source Properties in a Projection or other non-Atom Artifact. A Project Goal's explicit Tier `-1` grammar is evaluated before any ordinary default omission.
