---
atom_id: CA-R-1697
ref_id: CA-R-1697
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation
tier: 1
relations:
  child_of:
  - CA-R-007
status: Active
version: 36
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-1697-CORE_META_MODEL-RULE--bind-traceability-to-exact-claims-and-revisions.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1697-CORE_META_MODEL-RULE--bind-traceability-to-exact-claims-and-revisions.md
  source_atom_id: CA-R-1697
  source_atom_revision: 36
  source_sha256: fc285f979dacf6c2be3c3fb03c7e0897c9ecf1ef90bd179a91a5a11dd230c295
  original_relations_sha256: edef9085fddd1e905afd02423e8d88f5300a99b1f0a711703db5055e0c42a859
---
## Summary

Bind traceability to exact claims and revisions

## Claim

### Prose Claim


CAPRMEDIO traceability assertions.


**every** CAPRMEDIO traceability assertion **must** identify the exact governed claim revision on which a receiving artifact, implementation target, evaluation use, delivery action, operational observation, **or** other governed result relies.

## Details

the trace **must** preserve the source identity **and** accepted Revision, the receiving identity **or** stable target locator, the typed relation between them, the bounded scope **and** use, **and** the provenance needed **to** replay that relation. a relation **to** an artifact ID **without** its relied-upon revision is insufficient **after** the Atom has more than one accepted Revision.

Traceability records relationships; it does **not** transfer authority **or** prove correctness, execution, delivery, **or** currentness. secondary storage history **may** preserve Carrier evidence, while governed Journals preserve semantic relationships independently of that secondary history.
