---
atom_id: CA-R-1703
ref_id: CA-R-1703
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Projection/(.Form: Implementation Overview)'
  dependencies:
  - CAPRMEDIO_MODEL <+ Projection
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Term//Artifact
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Traceability
  - CAPRMEDIO_MODEL <+ Journal
  - CAPRMEDIO_MODEL <+ Package/Implementation
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
  - CAPRMEDIO_MODEL <+ Atom.Header.Role
tier: 1
status: Active
version: 40
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-R-1703-CORE_META_MODEL-RULE--use-implementation-overview-as-a-projection.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1703-CORE_META_MODEL-RULE--use-implementation-overview-as-a-projection.md
  source_atom_id: CA-R-1703
  source_atom_revision: 40
  source_sha256: fd66eae72b1201095d04fa6c3a3bc838a59876de9ae25325c733b55855f45f92
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Use Implementation Overview as a Projection

## Claim

### Prose Claim


Implementation Overview Projections.


an Implementation Overview is a non-authoritative Projection of what the current normative Atom frontier, native project targets, available provenance, **and** **any** registered implementation lineage sources show as implemented. its Implementation Bindings derive from the shared Project Journal under CA-R-1695; the current view does **not** replace the historical implementation event records retained **in** that Journal. the Atom Content Role axis does **not** apply **to** this Projection.

it **may** report realization coverage, source-to-target bindings, relevant commits, **and** unresolved implementation gaps. it is regenerated mechanically **or** rebuilt through governed reasoning from its declared source frontier. it is never an Atom **and** cannot replace the Journal, normative Atoms, native implementation, Operations evidence, **or** Verification.

the presence of this Projection does **not** require an internal Implementation Atom. storage, retention, **and** whether the Projection is committed **or** generated at runtime remain governed separately.

## Details

CAPRMEDIO represents the current view of project realization through an Implementation Overview Projection rather than an Implementation Atom.
