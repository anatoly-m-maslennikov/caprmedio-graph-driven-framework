---
subjects:
  active: Entity
  passive:
  - Entity
  - Entity/Object/Continuant/Governing Objects/Atom/Content Role
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Status'
version: 8
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-E-657
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Evaluation
form: Eval Policy
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-657-CORE_META_MODEL-POLICY--validate-type-qualified-status.md
  source_atom_id: CA-E-657
  source_atom_revision: 8
  source_sha256: 4578fdeb1ebd4518bd7c21a1eb3ccf603354ee9da6ef53c039c1e7f0c711f989
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Validate Type-Qualified Status

## Claim scope

Artifacts and their applicable qualified Status model.

## Claim

the Evaluation **must** reject an Artifact **if** **any** applicable condition holds:

- **when** an explicitly defined Status model applies, its Status domain is resolved outside its complete qualified Type **or** Atom Content Role **and** Type path, its current Status cardinality **`!=1`**, its current Status is **not** an allowed value of that domain, a prior transition coexists as current Status metadata, **or** a second disposition axis duplicates Status.

**when** no explicitly defined Status model applies, absence of a Status is **not** a rejection.

the Evaluation **must not** substitute Active **or** Inactive for a missing, invalid, **or** ambiguous Status. an Artifact outside the applicable qualified Status model **must not** fail merely because it has no Status.
