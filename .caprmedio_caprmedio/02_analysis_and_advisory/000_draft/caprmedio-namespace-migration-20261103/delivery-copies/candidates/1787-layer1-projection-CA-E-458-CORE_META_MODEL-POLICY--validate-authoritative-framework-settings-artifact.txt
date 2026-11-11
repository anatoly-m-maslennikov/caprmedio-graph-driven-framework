---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  passive:
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Governing Configuration
version: 35
updated_at: 2026-11-02 00:18:22 +0400
relations:
  evaluation_for:
  - CA-R-1402@27
  - CA-R-1430
  - CA-R-1429
  - CA-D-317
  - CA-D-358
  - CA-D-359
  - CA-D-360
  - CA-D-361
  - CA-R-1441
  - CA-M-279
atom_id: CA-E-458
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 6
role: Evaluation
form: Eval Policy
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-458-CORE_META_MODEL-POLICY--validate-authoritative-framework-settings-artifact.md
  source_atom_id: CA-E-458
  source_atom_revision: 35
  source_sha256: 4661ec3ed3ab8f2a1b277026c99d78dcba6127e3b63eea112d0b275f31462584
  original_relations_sha256: a95c38f963c816aed35c6d71c7ade4a56593d3be5fcbf8d9fd18ada3566f785b
---
## Summary

Validate Authoritative Framework Settings Artifact

## Claim scope

Framework Instance Settings.

## Claim

the Evaluation **must** reject Framework Instance Settings **if**

- it is treated as an Atom **or** Projection,
- has an Atom ID **or** Atom Content Role,
- resolves outside the current Project's registered instance directory,
- uses another Project's Settings Carrier,
- has other than **`=1`** authoritative TOML Carrier,
- **contains** Project initialization inputs **or** independently editable Project Structure,
- violates its foundational content boundary, applicable shared settings specifications, **or** applicable concrete field specifications **after** parameter resolution governed by CA-M-279,
- **or** lacks an exact current Revision, SHA-256 Digest, **and** Work Journal receipt admitted by CA-D-360.

## Details

for recovered baseline registration, the Evaluation **must** check the exact selected Project, Carrier path, lineage-derived logical Revision, **and** Digest binding required by CA-D-360. verify that registration leaves Settings bytes unchanged **and** records the actual observation time **and** evidence-backed observer Run **or** session. reject an absent **or** ambiguous binding, a stale Carrier Digest, a path-based Revision reset **or** guessed allocation, **or** a fabricated Settings write, past mutation, author, **or** history. an admitted baseline receipt **must not** replace any Settings schema **or** ownership check above **or** authorize another operation.
