---
atom_id: CA-M-382
ref_id: CA-M-382
container:
  scope_unit: CA-SU-17
role: Method
form: Eng Decision
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Source Retrieval"
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Governing Configuration
tier: 3
relations:
  depends_on:
  - CA-M-376
status: Active
version: 13
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-M-382-CONNECTOR_TOOLS-ENG_DECISION--construct-a-complete-configuration-read-adapter.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-17_FEATURE_CONNECTOR_TOOLS/05_method
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
author: Anatoly Maslennikov
---
# Summary

Construct a complete configuration read adapter

## Scope

construction of the complete Configuration Read operation on the shared TOML connector.

## Claim

**to** construct Configuration Read, the Implementer **must** refine CA-M-376:

- resolve the explicit logical target through the supplied Project/source/schema context **and** read permission; keep physical locations private. do **not** search for a fallback target, infer authority from a filename **or** invoke Modify.
- obtain complete exact source bytes **and** parse them with duplicate-key rejection. check the complete source against the supplied applicable schema **and** declared schema-version constraints; do **not** select **or** weaken the schema.
- bind the returned source bytes, parsed values **and** actual state evidence **to** the same observed source. reject a changed source **when** this consistency cannot be established; do **not** combine values from different reads.
- enforce supplied pins **and** historical source views exactly. return actual current evidence for unpinned Read **without** inventing an Atom Version **or** new retention guarantees.
- return CA-D-631's complete data **and** truthful common errors/effects. do **not** repair, normalize, persist, record a configuration revision **or** activate a runtime as a side effect of reading.

## Details

source acceptance **and** later functional verification are separate. this Method adds no transport, workflow wrapper, retry, publication **or** concurrency design.
