---
atom_id: CA-R-2278
current_scope_unit: CORE_META_MODEL
status: Active
tier: 1
subjects:
  active: CAPRMEDIO <+ MODEL <+ Entity
relations: {}
version: 2
updated_at: 2026-11-02 00:18:22 +0400
claim_target_scope_unit: CORE_META_MODEL
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2278-CORE_META_MODEL-RULE--require-exactly-one-defining-requirement-per-model-entity.md
  source_atom_id: CA-R-2278
  source_atom_revision: 2
  source_sha256: b1b5644f86df72c2ca7910ab16fd5a31a790a993e63dd6d5efc4dd67a8149b5c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Require Exactly One Defining Requirement per Model Entity

## Claim

Each logical model Entity has exactly one canonical defining Requirement of Type Entity Definition. Its governed Subject identifies the defined entity. Relation Definition qualifies through the accepted specialized template without a subtype hierarchy. Additional scoped Requirements may constrain an Entity but are not additional Entity Definitions. This applies to Objects, Aspects, Graph Syntax, Carriers and their dependent properties; a Scope Unit does not change the Entity's identity or defining meaning.

A missing canonical Definition or multiple qualifying Definitions fails this requirement. Derived IS_DEFINED_BY identifies that one Definition. Do not create new entities for every characteristic or nuance merely to multiply Atoms; preserve one coherent Claim and report weak fits of the dedicated-Definition trial. Equivalent property headings denote one logical Entity.

For / specialization, the narrower Definition inherits the broader Definition and states only its differences. For // instantiation, the instance follows its kind Definition and states only instance-specific facts. Reuse the applicable base structure, properties and constraints instead of copying them. Containment > adds no inheritance. A Method Atom is an Atom with Content Role Method, not a repeated definition of Atom.

## Details

The Operator confirmed all 133 shared/formal starting cases and later clarified that Aspects also retain one canonical Definition. Scoped additional Rs remain allowed. The exact-one invariant concerns definitions of model entities, not one new R for every runtime instance. Derived counterpart templates reference the main direction briefly instead of copying its full meaning.
