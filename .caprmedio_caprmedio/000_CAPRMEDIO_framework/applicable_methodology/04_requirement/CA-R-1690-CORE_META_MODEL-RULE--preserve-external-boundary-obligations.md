---
atom_id: CA-R-1690
ref_id: CA-R-1690
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Governance Origin
tier: 1
status: Active
version: 33
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1690-CORE_META_MODEL-RULE--preserve-external-boundary-obligations.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1690-CORE_META_MODEL-RULE--preserve-external-boundary-obligations.md
  source_atom_id: CA-R-1690
  source_atom_revision: 33
  source_sha256: a352e5067edc34f9d2bd20f51bfdd5efc1340cb0e521fa13ddf43cfc31b7a078
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Preserve external boundary obligations

## Claim

### Prose Claim


identified external obligations.


an Operator-accepted DDL, file schema, API, protocol, host format, supported-platform interface, CI interface, dependency boundary, **or** comparable external obligation is represented by its primary semantic contribution **and** external Governance Origin.

- Content Role follows the Claim's primary contribution under CA-R-1531@20, independently of Governance Origin under CA-R-1701. an external origin does **not** by itself assign Requirement **or** **any** other Content Role.
- an obligation imposed by an identified external source retains external Governance Origin **and** pins the applicable source version **or** digest. its graph connections use typed Relations whose Carrier encoding is governed by CA-D-268; these Relations do **not** create another Governance Origin.
- Implementation **must** conform **to** the exact accepted obligation Revision it consumes **and** **must not** rewrite that obligation. a changed external source creates a new accepted Revision **when** the same obligation remains identifiable. a different obligation requires a new Atom **and** explicit predecessor **and** successor Atom IDs **in** the predecessor's archival Journal event, **not** a formal replacement Relation.
- existing Implementations remain bound **to** their consumed Revisions **until** lineage-impact review determines their disposition.

Requirement authority defines the external boundary **and** admitted Type values. Delivery authority governs Carrier names, identities, **and** Catalog representations. this separation does **not** reclassify those Carrier specifications as Requirements because their source is external.
