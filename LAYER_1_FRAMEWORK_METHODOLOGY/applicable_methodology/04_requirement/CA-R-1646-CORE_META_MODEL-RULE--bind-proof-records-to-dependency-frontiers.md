---
atom_id: CA-R-1646
ref_id: CA-R-1646
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Quality <+ Traceability"
  dependencies:
  - CAPRMEDIO_MODEL <+ Term//Artifact
  - CAPRMEDIO_MODEL <+ Projection
  - CAPRMEDIO_MODEL <+ Carrier
tier: 3
status: Active
version: 41
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-R-1646-CORE_META_MODEL-RULE--bind-proof-records-to-dependency-frontiers.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1646-CORE_META_MODEL-RULE--bind-proof-records-to-dependency-frontiers.md
  source_atom_id: CA-R-1646
  source_atom_revision: 41
  source_sha256: ecef4e1572dc814a9b23eea9c136e2c7a4e11d570a63f2eaf9e1f47229419576
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Bind proof records to dependency frontiers

## Claim

### Prose Claim


governed proof records, their applicable inputs, and all selected Workflows, release policies, and version-control mechanisms.


**every** governed proof record **must** bind its observation **to** the exact applicable inputs under which it was produced.

- the binding includes the relevant Artifact **and** Implementation Revisions, configuration, evaluators, environments, **and** material inputs; CA-D-329 governs its representation.
- reliance on that observation for a current candidate requires a matching input binding **and** satisfaction of its additional governing invalidation conditions.
- a changed material input makes the affected proof stale for that candidate **until** the required checks run against the changed inputs. a missing **or** unresolved binding is unknown, **not** current.
- an unrelated change does **not** invalidate proof **unless** it changes the evaluated dependencies **or** satisfies an additional governing invalidation condition.
- retain the historical record unchanged. **not** (a recent timestamp **or** a refreshed Projection) alone proves currentness.
