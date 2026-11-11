---
subjects:
  active: 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Delivery/Type'
  passive:
  - CAPRMEDIO <+ MODEL <+ Carrier
version: 27
updated_at: 2026-11-02 00:55:09 +0400
relations: {}
atom_id: CA-D-402
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-402-CORE_META_MODEL-ENG_DECISION--serialize-delivery-type-tokens.md
  source_atom_id: CA-D-402
  source_atom_revision: 27
  source_sha256: fe044acb8d0a710ea73c58913bf63de8f7a113c9d5f070bd16521d40c8b2cae1
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize Delivery Type Tokens

## Claim scope

the serialization of Delivery Type tokens in a Delivery Atom File Carrier filename.

## Claim

a Delivery Atom File Carrier **must** serialize the following Type components within the Atom filename grammar governed by CA-D-283-CORE_META_MODEL-ENG_DECISION--serialize-project-owned-markdown-atom-filenames **and** CA-D-284-CORE_META_MODEL-ENG_DECISION--serialize-filename-token-case:

- Eng Policy: `ENG_POLICY`.
- Eng Decision: `ENG_DECISION`.
- Release Definition: `RELEASE_DEFINITION`.
- Environment Definition: `ENVIRONMENT_DEFINITION`.

these mappings govern filename representation; they do **not** rename a Type, admit a new Type, **or** prescribe a YAML Type value.

## Details

The YAML `form` field carries the Atom Form under CA-D-657; a filename Type token is only its carrier encoding, not a second Type or a Label. An explicit `label` field is the effective Label when present; when absent, the effective Label is derived from the Atom Type name under CA-R-2497. Do not infer Type from a filename token or from that derived Label.

Release Definition and Environment Definition remain outside PROGRAMMATIC and its declared descendants under CA-R-1665; CA-R-2123 governs the Method and Delivery Type restriction in that scope.
