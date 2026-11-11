---
atom_id: CA-R-1687
ref_id: CA-R-1687
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Quality <+ Traceability"
tier: 1
status: Active
version: 34
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-1687-CORE_META_MODEL-RULE--requirement-keep-provenance-separate-from-evidence.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1687-CORE_META_MODEL-RULE--requirement-keep-provenance-separate-from-evidence.md
  source_atom_id: CA-R-1687
  source_atom_revision: 34
  source_sha256: 8d79b8b52b0eb88398f12353bbcaf436e99059b76b393a9a9676bf926de6757f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Requirement — Keep provenance separate from evidence

## Claim

### Prose Claim


provenance and Evidence for governed claims and Implementations.


provenance establishes the origin, carrier identity, revision, sequence, **and** transformation history of a governed claim **or** Implementation. it does **not** by itself establish that the claim is correct, accepted, current, applicable, **or** sufficiently assured.

complete governed provenance remains owned under CA-R-1720. a storage-history record, Author identity, session identifier, signature, hash, **or** intact Carrier proves **only** the bounded historical fact it records. **none** of those facts becomes evidence for the carrier's semantic claim **without** a separate, explicit claim-bound Evidence relation.

Evidence used for reliance **must** identify the claim it supports, the relevant carrier **or** Journal Record, the producing **or** interpreting work **or** Method **when** material, **and** the applicable scope **and** time boundary. Verification remains a separate Evaluation conclusion. a claim, its carrier, **and** the work that created it **must not** silently evidence themselves.
