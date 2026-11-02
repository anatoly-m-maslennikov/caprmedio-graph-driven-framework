---
atom_id: CA-R-2278@1
content_role: Requirement
type: Rule
current_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
subjects:
  governs: Entity
relations: {}
version: 1
updated_at: 2026-10-29 17:09:55 +0400
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Require Exactly One Defining Requirement per Model Entity

## Claim

Each logical model Entity has exactly one canonical defining Requirement of Type Entity Definition. Its governed Subject identifies the defined entity. Relation Definition qualifies through the accepted specialized template without a subtype hierarchy. Additional scoped Requirements may constrain an Entity but are not additional Entity Definitions. This applies to Objects, Aspects, Graph Syntax, Carriers and their dependent properties; a Scope Unit does not change the Entity's identity or defining meaning.

A missing canonical Definition or multiple qualifying Definitions fails this requirement. Derived IS_DEFINED_BY identifies that one Definition. Do not create new entities for every characteristic or nuance merely to multiply Atoms; preserve one coherent Claim and report weak fits of the dedicated-Definition trial. Equivalent property headings denote one logical Entity.

For / specialization, the narrower Definition inherits the broader Definition and states only its differences. For // instantiation, the instance follows its kind Definition and states only instance-specific facts. Reuse the applicable base structure, properties and constraints instead of copying them. Containment > adds no inheritance. A Method Atom is an Atom with Content Role Method, not a repeated definition of Atom.

## Details

The Operator confirmed all 133 shared/formal starting cases and later clarified that Aspects also retain one canonical Definition. Scoped additional Rs remain allowed. The exact-one invariant concerns definitions of model entities, not one new R for every runtime instance. Derived counterpart templates reference the main direction briefly instead of copying its full meaning.
