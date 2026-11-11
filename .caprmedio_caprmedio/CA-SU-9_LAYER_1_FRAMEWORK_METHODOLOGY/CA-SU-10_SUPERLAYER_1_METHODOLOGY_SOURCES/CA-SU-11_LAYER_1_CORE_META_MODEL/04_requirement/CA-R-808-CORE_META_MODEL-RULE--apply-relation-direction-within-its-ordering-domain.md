---
atom_id: CA-R-808
ref_id: CA-R-808
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation
  dependencies:
  - CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//Stored Governing RMED Relation Occurrences
  - CAPRMEDIO_MODEL <+ Atom.Header.Context.Tier
  - CAPRMEDIO_MODEL <+ Scope Unit
tier: 1
status: Active
version: 35
updated_at: 2026-11-04 09:19:08 +0400
carrier_destination:
  file:
    name: CA-R-808-CORE_META_MODEL-RULE--apply-relation-direction-within-its-ordering-domain.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Apply relation direction within its ordering domain

## Claim

### Prose Claim


declared relations.


**every** declared relation **must** satisfy the target position **and** ordering domain registered for its relation family. Stored governing RMED relation occurrences selected by CA-R-2148@10 **must** use the numeric Tier-and-Scope ordering in CA-R-2149: a same-Scope target **must** have a strictly lower numeric Tier, a target in a strict ancestor Scope Unit is accepted without Tier comparison, the exact one-way Project Configuration-to-Core Meta-Model logical-role prerequisite declared by CA-R-1218@31 is accepted without Tier comparison, and every other descendant **or** sibling target is forbidden. Temporal relations **must** use lifecycle succession, realization relations **must** use realization order, dependency relations **must** use dependency order, **and** **every** other admitted domain **must** use its own registered order. a universal upstream **or** downstream rule **must not** be inferred across different ordering domains, **and** an inverse-derived view **must not** create another declared edge.

## Details

For selected governing RMED occurrences, CA-R-2149 uses the Project Scope Unit resolved from the active Subject of an Atom with Form Goal as its ordering context. Ordinary endpoints still use their Local Scope Unit.
