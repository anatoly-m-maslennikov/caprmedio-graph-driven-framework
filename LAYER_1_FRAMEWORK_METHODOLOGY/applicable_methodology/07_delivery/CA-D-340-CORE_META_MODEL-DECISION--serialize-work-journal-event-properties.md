---
subjects:
  active: Carrier/File.Main Content
  passive:
  - Carrier
  - Journal
  - Event Record
  - Atom
  - Project
  - Projection
version: 33
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-D-340
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-340-CORE_META_MODEL-DECISION--serialize-work-journal-event-properties.md
  source_atom_id: CA-D-340
  source_atom_revision: 33
  source_sha256: 1e56b8315497858aa0decc3f958f7edd06fbfdb2f4a925a0406963b5036730c4
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize Work Journal Event Properties

## Claim scope

serialization **and** reading of supplied Work Journal Event representations.

## Claim

the Main Content of a Journal Carrier **must** preserve the properties actually supplied as observations through safe encoding; reading **must** return stored representations as recorded.

- preserve supplied identities, Types, action Kinds, Authors, times, session provenance, Scope, identifiers, filenames, paths **and** other values **when** present. do **not** invent missing values **or** rewrite them **to** satisfy current naming **or** classification rules.
- an Atom ID **or** other observed property is payload data, **not** a Project-conformance judgment, permission **or** proof of correct execution.
- do **not** impose required-field, event-identity, schema, digest, prior-history, chain, receipt, deduplication, retry **or** recovery admission **to** append/read.
- retain existing historical representations **and** bytes **without** migration, repair **or** synthetic baselines. ordinary serialization/read failure is reported truthfully, **not** converted into fabricated data.
