---
atom_id: CA-R-2278
ref_id: CA-R-2278
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity
tier: 1
status: Active
version: 4
updated_at: 2026-11-05 22:47:24 +0400
carrier_destination:
  file:
    name: CA-R-2278-CORE_META_MODEL-RULE--require-exactly-one-defining-requirement-per-model-entity.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2278-CORE_META_MODEL-RULE--require-exactly-one-defining-requirement-per-model-entity.md
  source_atom_id: CA-R-2278
  source_atom_revision: 4
  source_sha256: c478dfb6eb19b70ca9e60df134b17357d32fe7811860ae0b3677b382b2133445
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Require Exactly One Defining Requirement per Model Entity

## Claim

### Prose Claim

Each logical model Entity has exactly one canonical declaring Requirement with an admitted Declaration Form in the selected effective MODEL. Its governed Subject identifies the declared entity. This applies to Objects, Aspects, graph Relation types, CFEL descriptors, Carriers and their dependent Properties; a Scope Unit does not change an Entity's identity or declaring meaning. Additional scoped Requirements may constrain an Entity without becoming additional declaring owners.

A missing declaring Requirement or multiple effective declaring Requirements fails this rule. IS_DECLARED_BY identifies the qualified declaring Atom through its GOVERNS link. Qualification requires Requirement role and an admitted Declaration Form, including a specialized Declaration Form admitted by its governing Form Declaration. Count inherited Current Declarations and explicit local replacements after MODEL override resolution. A replaced Declaration remains available in its base MODEL and is not a second effective owner locally. Drafts and archives are not Current owners.

For / specialization, the narrower Declaration inherits applicable broader constraints and states its differences. For // instantiation, the instance follows its kind Declaration and states instance-specific facts. Reuse applicable base structure, Properties and constraints instead of copying them. Containment adds no inheritance. A Method Atom remains an Atom with Header.Role Method. Do not create new entities for every characteristic merely to multiply Atoms; equivalent Property headings denote one logical Entity.

This exact-one invariant concerns declaring owners of model entities, not a new Requirement for every runtime instance. A minimal inverse Declaration references its canonical counterpart instead of duplicating shared meaning; a qualified non-inverse derived view retains its qualification.
