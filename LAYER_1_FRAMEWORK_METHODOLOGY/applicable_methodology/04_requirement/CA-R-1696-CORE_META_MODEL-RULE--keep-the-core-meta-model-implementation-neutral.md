---
atom_id: CA-R-1696
ref_id: CA-R-1696
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//CORE_META_MODEL
tier: 1
relations:
  child_of:
  - CA-M-447
  - CA-M-261
status: Active
version: 37
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-1696-CORE_META_MODEL-RULE--keep-the-core-meta-model-implementation-neutral.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1696-CORE_META_MODEL-RULE--keep-the-core-meta-model-implementation-neutral.md
  source_atom_id: CA-R-1696
  source_atom_revision: 37
  source_sha256: 5dc22a902a2bb5b108ef9fa2f7bc56ec6e5b401a73ecd8a860ba21e635005af6
  original_relations_sha256: daa221ee3824742de82fc1e74c79b2e49ba96d8d13faef8080c702793c699583
---
## Summary

Keep the Core Meta-Model implementation neutral

## Claim

### Prose Claim


CORE_META_MODEL authority and its reusable model invariants and expansion boundaries.


CORE_META_MODEL authority **must** define reusable model invariants **and** expansion boundaries **without** hidden dependence on a programming language, LLM provider **or** model, agent host, operating system, repository host, package manager, database, deployment platform, **or** other replaceable implementation mechanism.

mechanism-specific obligations belong **to** the Scope that owns the mechanism. Extensions **and** PROJECT_CONFIGURATION **may** expand the model for their bounded use **without** rewriting its governing Claims.

CORE_META_MODEL **may** name a mechanism **only** **when** the mechanism itself is the explicit Entity governed by the Claim, such as a Carrier format, portability boundary, **or** external constraint; this reference **must not** make that mechanism a hidden prerequisite of unrelated model Claims.
