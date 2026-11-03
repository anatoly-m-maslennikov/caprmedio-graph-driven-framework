---
subjects:
  active: CFEL <+ Relation
version: 36
updated_at: 2026-11-02 19:44:26 +0400
relations:
  child_of:
  - CA-R-007
atom_id: CA-R-1697
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1697-CORE_META_MODEL-RULE--bind-traceability-to-exact-claims-and-revisions.md
  source_atom_id: CA-R-1697
  source_atom_revision: 36
  source_sha256: 1045441eecf9d0a43972dabdc4130d37cf92768168d0917b8fc374985e43ceb1
  original_relations_sha256: edef9085fddd1e905afd02423e8d88f5300a99b1f0a711703db5055e0c42a859
---
## Summary

Bind traceability to exact claims and revisions

## Claim scope

CAPRMEDIO traceability assertions.

## Claim

**every** CAPRMEDIO traceability assertion **must** identify the exact governed claim revision on which a receiving artifact, implementation target, evaluation use, delivery action, operational observation, **or** other governed result relies.

## Details

the trace **must** preserve the source identity **and** accepted Revision, the receiving identity **or** stable target locator, the typed relation between them, the bounded scope **and** use, **and** the provenance needed **to** replay that relation. a relation **to** an artifact ID **without** its relied-upon revision is insufficient **after** the Atom has more than one accepted Revision.

Traceability records relationships; it does **not** transfer authority **or** prove correctness, execution, delivery, **or** currentness. secondary storage history **may** preserve Carrier evidence, while governed Journals preserve semantic relationships independently of that secondary history.
