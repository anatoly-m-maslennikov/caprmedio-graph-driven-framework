---
atom_id: CA-E-657
ref_id: CA-E-657
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Policy
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Atom.Header.Role
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Status'
tier: 2
status: Active
version: 8
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-E-657-CORE_META_MODEL-EVAL_POLICY--validate-type-qualified-status.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-657-CORE_META_MODEL-POLICY--validate-type-qualified-status.md
  source_atom_id: CA-E-657
  source_atom_revision: 8
  source_sha256: a547a75f46498642e62b70eae47cb0d295bd3f0bf640b761008dad898a3fefed
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Validate Type-Qualified Status

## Claim

### Prose Claim


Artifacts and their applicable qualified Status model.


the Evaluation **must** reject an Artifact **if** **any** applicable condition holds:

- **when** an explicitly defined Status model applies, its Status domain is resolved outside its complete qualified Type **or** Atom Content Role **and** Type path, its current Status cardinality **`!=1`**, its current Status is **not** an allowed value of that domain, a prior transition coexists as current Status metadata, **or** a second disposition axis duplicates Status.

**when** no explicitly defined Status model applies, absence of a Status is **not** a rejection.

the Evaluation **must not** substitute Active **or** Inactive for a missing, invalid, **or** ambiguous Status. an Artifact outside the applicable qualified Status model **must not** fail merely because it has no Status.
