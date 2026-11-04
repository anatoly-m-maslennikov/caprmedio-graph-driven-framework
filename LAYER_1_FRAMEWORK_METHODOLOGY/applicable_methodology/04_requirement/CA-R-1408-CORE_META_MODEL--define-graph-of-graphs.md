---
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
  passive:
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Projection
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
version: 25
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1408
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1408-CORE_META_MODEL--define-graph-of-graphs.md
  source_atom_id: CA-R-1408
  source_atom_revision: 25
  source_sha256: cd8b86c2e7f9ffdd159a2745e64d102289d80cf7f3d7e5709f76a4fe62b4a057
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Graph of Graphs

## Claim

### Prose Claim


Graph of Graphs compositions and any generated overview Artifact.




The following interpretation is required when this governed concept is used:

a Graph of Graphs **means** a composition of CAPRMEDIO Graphs connected through graph-qualified typed references **or** shared source identities. secondary graphs **in** this composition remain Projections under CA-R-1471-CORE_META_MODEL-CORE-REQUIREMENT--keep-secondary-graphs-derived-from-source-authority, **and** their internal, cross-graph, **and** authoritative-source connections remain governed by CA-R-1472-CORE_META_MODEL-GENERAL-REQUIREMENT--admit-typed-secondary-graph-connections.

the composition does **not**, by itself, require another separately generated overview Artifact. **if** an overview is generated, its represented connections remain derived from the participating graphs **and** their sources **without** becoming another authority.

